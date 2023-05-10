import time
import random
import sys
from enum import Enum

class GameState(Enum):
    ONGOING = 0
    WON = 1
    TIED = 2

class Board:
    def __init__(self, size, win_length, spots=None):
        self.size = size
        self.win_length = win_length
        self.board_keys = range(1, size * size + 1)
        if spots is None:
            self.spots = {i: "-" for i in self.board_keys}
        else:
            self.spots = {k: spots[k] for k in spots}

    def clone(self):
        return Board(self.size, self.win_length, self.spots)
    
    def generate_winning_conditions(self):
        size = self.size
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

    def check_win(self):
        board_spots = self.spots

        winning_conditions = self.generate_winning_conditions()

        for condition in winning_conditions:
            first_spot = board_spots[condition[0]]
            if first_spot != '-' and all(board_spots[i] == first_spot for i in condition):
                return first_spot
        
        # Todo: this isn't a very efficient solution, improve
        empty_spots = 0
        for i in range(self.size):
            for j in range(self.size):
                empty_spots += 1 if(board_spots[i * self.size + j + 1] == '-') else 0
                
        if empty_spots ==0:
            return 'tie'

    def reset(self):
        self.spots = {i: "-" for i in range(1, self.size * self.size + 1)}

    def draw(self):
        rows = [f"|{'||'.join(self.spots[i] for i in range(row * self.size + 1, (row + 1) * self.size + 1))}|" for row in range(self.size)]
        board_display = "\n".join(rows)
        print(board_display + "\n")

    def make_move(self, move, player_piece):
        self.spots[move] = player_piece
    
    def clear_move(self, move):
        self.spots[move] = "-"

    def get_board_spots(self):
        return self.spots

    def get_board_keys(self):
        return range(1, self.size * self.size + 1)

    def is_spot_empty(self, index):
        return self.spots[index] == "-"

    def get_available_moves(self, player_piece):
        return [i for i in self.board_keys if self.is_spot_empty(i)]


class Agent:
    def __init__(self, playing_piece, enemy_piece):
        self.playing_piece = playing_piece
        self.enemy_piece = enemy_piece
    
    def run(self, board: Board):
        raise NotImplementedError('Abstract method')

class ScoringAgent(Agent):

    def score(self, board:Board, index:int):
        raise NotImplemented('Abstract method')

    def run(self, board: Board):
        best_score = float('-inf')
        best_move = None

        for i in board.board_keys:
            if board.is_spot_empty(i):
                score = self.score(board, i)
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

class MonteCarloAgent(Agent):
    def __init__(self, player_piece: str, enemy_piece: str, simulations: int = 200):
        super().__init__(player_piece, enemy_piece)
        self.simulations = simulations
        self.evals = {}

    def run(self, board: Board):
        start = time.time()
        evals = self.simulate(board, self.playing_piece)
        end = time.time()
        print(f"Time elapsed: {end - start}")

        best_move = None
        best_score = float('-inf')

        for move, score in evals.items():
            if score > best_score:
                best_move = move
                best_score = score

        return best_move

    def simulate(self, board: Board, player_piece: str) -> float:
        evals = {}
        for _ in range(self.simulations):
            player = player_piece
            sim_board = board.clone()
            simulated_moves = []
            moves = sim_board.get_available_moves(player)

            score = sim_board.size * sim_board.size

            while moves:
                attempt = random.choice(moves)
                sim_board.make_move(attempt, player)
                simulated_moves.append(attempt)

                result = sim_board.check_win()

                if result == player:
                    break

                score -= 1
                player = 'o' if player == 'x' else 'x'
                moves = sim_board.get_available_moves(player)

            first_move = simulated_moves[0]

            if player == result:
                score *= -1

            first_move_key = first_move # repr(first_move.spots)

            if first_move_key in evals:
                evals[first_move_key] += score
            else:
                evals[first_move_key] = score

        return evals


class TwoPlayerGame:
    def __init__(self, board, players: list[Agent]):
        self.board = board
        self.turn_count = 0
        self.simulate = 0
        self.game_start_time = 0
        self.start_time = 0
        self.game_times = []

        self.players = players

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
        player_index = random.choice([0, 1])
        self.first_turn(self.players[player_index])
        while True:
            self.board.draw()
            player_index = 1 - player_index
            player_action = self.players[player_index].run(self.board)
            self.board.make_move(player_action, self.players[player_index].playing_piece) # Todo: validate player move

            self.turn_count += 1

            game_won = self.board.check_win()
            if game_won:
                self.board.draw()
                self.end_game(game_won)

    def first_turn(self, player:Agent):
        move = random.choice(self.board.board_keys)
        self.board.make_move(move, player.playing_piece)
    

def main():
    board_size = 5
    win_length = 5
    board = Board(board_size, win_length)
    player_one = MonteCarloAgent('x', 'o')
    player_two = MonteCarloAgent('o', 'x')
    game = TwoPlayerGame(board, [player_one, player_two])

    sys.setrecursionlimit(3000)
    game.simulate = 1
    game.start_time = time.time()
    game.run()

if __name__ == '__main__':
    main()