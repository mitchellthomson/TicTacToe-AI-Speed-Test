import pytest
from alphaBeta import Board, Game

def create_board(board_dict={}, board_size=3) -> Board:
    board = Board(board_size)
    for key, value in board_dict.items():
        board.spots[key] = value
    return board

def create_game(board, win_length=3) -> Game:
    return Game(board, win_length)



class TestCheckWin:
    def test_empty_board(self):
        board_spots = {1 : "-",2 : "-",3 : "-",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
        assert create_game(create_board(board_spots)).check_win() is None

    def test_horizontal_win_x(self):
        board_spots = {1 : "x",2 : "x",3 : "x",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
        assert create_game(create_board(board_spots)).check_win() == "x"

    def test_veritical_win_x(self):
        board_spots = {1 : "x",2 : "-",3 : "-",4 : "x",5 : "-",6 : "-",7 : "x",8 : "-",9 : "-",}
        assert create_game(create_board(board_spots)).check_win() == "x"

    def test_diagonal_win_x(self):
        board_spots = {1 : "x",2 : "-",3 : "-",4 : "-",5 : "x",6 : "-",7 : "-",8 : "-",9 : "x",}
        assert create_game(create_board(board_spots)).check_win() == "x"
    
    def test_horizontal_win_o(self):
        board_spots = {1 : "o",2 : "o",3 : "o",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
        assert create_game(create_board(board_spots)).check_win() == "o"

    def test_veritical_win_o(self):
        board_spots = {1 : "o",2 : "-",3 : "-",4 : "o",5 : "-",6 : "-",7 : "o",8 : "-",9 : "-",}
        pass
        assert create_game(create_board(board_spots)).check_win() == "o"
        
    def test_diagonal_win_o(self):
        board_spots = {1 : "o",2 : "-",3 : "-",4 : "-",5 : "o",6 : "-",7 : "-",8 : "-",9 : "o",}
        pass
        assert create_game(create_board(board_spots)).check_win() == "o"

    def test_no_win(self):
        board_spots = {1 : "o",2 : "-",3 : "-",4 : "x",5 : "-",6 : "-",7 : "x",8 : "-",9 : "o",}
        assert create_game(create_board(board_spots)).check_win() is None
        pass

    def test_tied_turn_count(self):
        board_spots = {1 : "o",2 : "o",3 : "x",4 : "x",5 : "x",6 : "o",7 : "o",8 : "x",9 : "x",}
        assert create_game(create_board(board_spots)).check_win() == "tie"

    def test_tied(self):
        board_spots = {1 : "o",2 : "o",3 : "x",4 : "x",5 : "x",6 : "o",7 : "o",8 : "x",9 : "x",}
        assert create_game(create_board(board_spots)).check_win() == "tie"

class TestCpuTurn:

    def test_one_step_to_victory_x(self):
        # x x -
        # o o x
        # o - -
        board_spots = {1 : "x",2 : "x",3 : "-",4 : "o",5 : "o",6 : "x",7 : "x",8 : "-",9 : "-",}
        board = create_board(board_spots)
        create_game(board).cpu_turn('x')
        assert board.spots[3] == "x"

    def test_one_step_to_victory_o(self):
        # o o -
        # x x o
        # x - -
        board_spots = {1 : "o",2 : "o",3 : "-",4 : "x",5 : "x",6 : "o",7 : "o",8 : "-",9 : "-",}
        board = create_board(board_spots)
        create_game(board).cpu_turn('o')
        assert board.spots[3] == "o"

    def test_one_step_tie_x(self):
        # x x o
        # o o x
        # - o x
        board_spots = {1 : "x",2 : "x",3 : "o",4 : "o",5 : "o",6 : "x",7 : "-",8 : "o",9 : "x",}
        board = create_board(board_spots)
        create_game(board).cpu_turn('x')
        assert board.spots[7] == "x"

    def test_one_step_tie_o(self):
        # o o x
        # x x o
        # - x o
        board_spots = {1 : "o",2 : "o",3 : "x",4 : "x",5 : "x",6 : "o",7 : "-",8 : "x",9 : "o",}
        board = create_board(board_spots)
        create_game(board).cpu_turn('o')
        assert board.spots[7] == "o"
