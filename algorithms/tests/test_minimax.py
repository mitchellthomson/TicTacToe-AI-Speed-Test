import pytest
from algorithms.minimax import checkWin

class TestCheckWin:
    def test_empty_board(self):
        board = {1 : "-",2 : "-",3 : "-",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
        assert checkWin(board) is None

    def test_horizontal_win_x(self):
        board = {1 : "x",2 : "x",3 : "x",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
        assert checkWin(board) == "x"

    def test_veritical_win_x(self):
        board = {1 : "x",2 : "-",3 : "-",4 : "x",5 : "-",6 : "-",7 : "x",8 : "-",9 : "-",}
        assert checkWin(board) == "x"

    def test_diagonal_win_x(self):
        board = {1 : "x",2 : "-",3 : "-",4 : "-",5 : "x",6 : "-",7 : "-",8 : "-",9 : "x",}
        assert checkWin(board) == "x"

    def test_horizontal_win_o(self):
        board = {1 : "o",2 : "o",3 : "o",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
        assert checkWin(board) == "o"

    def test_veritical_win_o(self):
        board = {1 : "o",2 : "-",3 : "-",4 : "o",5 : "-",6 : "-",7 : "o",8 : "-",9 : "-",}
        pass
        assert checkWin(board) == "o"

    def test_diagonal_win_o(self):
        board = {1 : "o",2 : "-",3 : "-",4 : "-",5 : "o",6 : "-",7 : "-",8 : "-",9 : "o",}
        pass
        assert checkWin(board) == "o"

    def test_no_win(self):
        board = {1 : "o",2 : "-",3 : "-",4 : "x",5 : "-",6 : "-",7 : "x",8 : "-",9 : "o",}
        assert checkWin(board) is None
        pass

    def test_tied(self):
        board = {1 : "o",2 : "o",3 : "x",4 : "x",5 : "x",6 : "o",7 : "o",8 : "x",9 : "x",}
        assert checkWin(board, 9) == "Tie"