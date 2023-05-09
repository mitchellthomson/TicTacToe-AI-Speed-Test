import time
import random
import sys
from enum import Enum

class GameState(Enum):
    ONGOING = 0
    WON = 1
    TIED = 2

class Board:
    def __init__(self, size):
        self.size = size
        self.spots = {i: "-" for i in range(1, size * size + 1)}

    def reset(self):
        self.spots = {i: "-" for i in range(1, self.size * self.size + 1)}

    def draw(self):
        rows = [f"|{'||'.join(self.spots[i] for i in range(row * self.size + 1, (row + 1) * self.size + 1))}|" for row in range(self.size)]
        board_display = "\n".join(rows)
        print(board_display + "\n")

    def make_move(self, move, player_piece):
        self.spots[move] = player_piece

    def get_board_spots(self):
        return self.spots

    def is_spot_empty(self, index):
        return self.spots[index] == "-"


class Game:
    def __init__(self, board, win_length):
        self.board: Board = board
        self.win_length = win_length
        self.player = 0
        self.turn_count = 0
        self.simulate = 0
        self.game_start_time = 0
        self.start_time = 0
        self.game_times = []
        self.count = 0

    def end_game(self, win):
        self.simulate -= 1
        if win == 'tie':
            print("Game was a tie")
        else: 
            print("Winner is ", win)
        end_time = time.time()
        total_time = end_time - self.game_start_time
        self.game_times.append(total_time)
        if self.simulate > 0:
            self.reset()
        else:
            end_game_time = time.time()
            total_time = end_game_time - self.start_time
            average_time = sum(self.game_times) / len(self.game_times)
            print("Time for simulation = ", total_time)
            exit(1)

    def reset(self):
        self.board.reset()
        self.turn_count = 0
        self.game_start_time = time.time()
        self.run()

    def run(self):
        self.player = random.choice([0, 1])
        player_piece = 'x' if self.player == 0 else 'o'
        self.first_turn(player_piece)
        while True:
            self.board.draw()
            self.player = 1 - self.player
            player_piece = 'o' if self.player == 1 else 'x'
            self.cpu_turn(player_piece)
            self.turn_count += 1
            game_won = self.check_win()
            if game_won:
                self.board.draw()
                self.end_game(game_won)

    def first_turn(self, player_piece):
        move = random.randint(1, self.board.size * self.board.size)
        self.board.make_move(move, player_piece)
    
    def check_win(self):
        board_spots = self.board.get_board_spots()

        winning_conditions = self.generate_winning_conditions()

        for condition in winning_conditions:
            first_spot = board_spots[condition[0]]
            if first_spot != '-' and all(board_spots[i] == first_spot for i in condition):
                return first_spot
        
        empty_spots = 0
        for i in range(self.board.size):
            for j in range(self.board.size):
                empty_spots += 1 if(board_spots[i * self.board.size + j + 1] == '-') else 0
                
        if empty_spots ==0:
            return 'tie'

    def generate_winning_conditions(self):
        size = self.board.size
        win_len = self.win_length
        winning_conditions = []

        # Rows
        for row in range(size):
            for col in range(size - win_len + 1):
                condition = [row * size + col + i + 1 for i in range(win_len)]
                winning_conditions.append(condition)

        # Columns
        for col in range(size):
            for row in range(size - win_len + 1):
                condition = [(row + i) * size + col + 1 for i in range(win_len)]
                winning_conditions.append(condition)

        # Main diagonals
        for row in range(size - win_len + 1):
            for col in range(size - win_len + 1):
                condition = [(row + i) * size + col + i + 1 for i in range(win_len)]
                winning_conditions.append(condition)

        # Counter-diagonals
        for row in range(size - win_len + 1):
            for col in range(win_len - 1, size):
                condition = [(row + i) * size + col - i + 1 for i in range(win_len)]
                winning_conditions.append(condition)

        return winning_conditions
    
    def cpu_turn(self, player_piece):
        turn_time_start = time.time()
        best_score = -8000
        best_move = None

        for i in range(self.board.size):
            for j in range(self.board.size):
                board_spot_index = i * self.board.size +j + 1
                if self.board.spots[board_spot_index] == "-":
                    self.board.spots[board_spot_index] = player_piece
                    enemy_piece = 'x' if player_piece == 'o' else 'o'
                    score = self.mini_max(self.board, self.win_length, False, float('-inf'), float('inf'), enemy_piece)
                    self.board.spots[board_spot_index] = "-"

                    if score > best_score:
                        best_score = score
                        best_move = board_spot_index

        self.board.spots[best_move] = player_piece

    def mini_max(self, board, depth, is_maximizing, alpha, beta, playing_piece):
        self.count += 1
        oppsing_piece =  'x' if playing_piece == 'o' else 'o'
        win_check = self.check_win()
        player_piece = 'o' if self.player == 1 else 'x'
        enemy_piece = 'x' if player_piece == 'o' else 'o'

        if win_check == player_piece:
            return 100
        elif win_check == enemy_piece:
            return -100
        elif win_check == 'tie' or depth == 0: # either tie or no win state
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(board.size):
                for j in range(board.size):
                    board_spot_index = i * board.size +j +1
                    if board.spots[board_spot_index] == "-":
                        board.spots[board_spot_index] = playing_piece
                        score = self.mini_max(board, depth - 1, False, alpha, beta, oppsing_piece)
                        board.spots[board_spot_index] = "-"
                        best_score = max(best_score, score)
                        alpha = max(alpha, score)

                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(board.size):
                for j in range(board.size):
                    board_spot_index = i * board.size +j + 1
                    if board.spots[board_spot_index] == "-":
                        board.spots[board_spot_index] = playing_piece
                        score = self.mini_max(board, depth - 1, True, alpha, beta, oppsing_piece)
                        board.spots[board_spot_index] = "-"
                        best_score = min(best_score, score)
                        beta = min(beta, score)

                        if beta <= alpha:
                            break
            return best_score

def main():
    board_size = 3
    win_length = 3
    board = Board(board_size)
    game = Game(board, win_length)

    sys.setrecursionlimit(3000)
    game.simulate = 1
    game.start_time = time.time()
    game.run()

if __name__ == '__main__':
    main()
