import numpy as np
import pytest
from game import (
    create_board,
    drop_piece,
    is_valid_location,
    get_next_open_row,
    winning_move,
    get_valid_locations,
    PLAYER_PIECE,
    AI_PIECE,
)

def test_create_board_shape():
    board = create_board()
    assert board.shape == (6, 7)
    assert np.all(board == 0)

def test_drop_piece():
    board = create_board()
    drop_piece(board, 0, 0, PLAYER_PIECE)
    assert board[0][0] == PLAYER_PIECE

def test_is_valid_location():
    board = create_board()
    assert is_valid_location(board, 0) == True
    for row in range(6):
        drop_piece(board, row, 0, PLAYER_PIECE)
    assert is_valid_location(board, 0) == False

def test_get_next_open_row():
    board = create_board()
    drop_piece(board, 0, 0, PLAYER_PIECE)
    row = get_next_open_row(board, 0)
    assert row == 1

def test_winning_move_horizontal():
    board = create_board()
    for col in range(4):
        drop_piece(board, 0, col, PLAYER_PIECE)
    assert winning_move(board, PLAYER_PIECE)

def test_get_valid_locations():
    board = create_board()
    valid = get_valid_locations(board)
    assert len(valid) == 7
    for row in range(6):
        drop_piece(board, row, 0, PLAYER_PIECE)
    valid = get_valid_locations(board)
    assert 0 not in valid
