"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves_possible = set()

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item is None:
                moves_possible.add((i, j))

    return moves_possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    user_move = player(board)
    copy_board = deepcopy(board)
    i, j = action

    if board[i][j] is not None:
        raise Exception
    else:
        copy_board[i][j] = user_move

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for user in (X, O):
        for row in board:
            if row == [user]*3:
                return user

        for i in range(3):
            col = [board[x][i] for x in range(3)]
            if col == [user]*3:
                return user

        if [board[i][i] for i in range(0, 3)] == [user]*3:
            return user

        elif [board[i][~i] for i in range(0, 3)] == [user]*3:
            return user

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_user = winner(board)

    if winning_user == X:
        return 1
    elif winning_user == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def maxima(board):
        ideal_move = ()
        if terminal(board):
            return utility(board), ideal_move
        else:
            k = -5
            for action in actions(board):
                min_value = minima(result(board, action))[0]
                if min_value > k:
                    k = min_value
                    ideal_move = action
            return k, ideal_move

    def minima(board):
        ideal_move = ()
        if terminal(board):
            return utility(board), ideal_move
        else:
            k = 5
            for action in actions(board):
                max_value = maxima(result(board, action))[0]
                if max_value < k:
                    k = max_value
                    ideal_move = action
            return k, ideal_move

    current_user = player(board)

    if terminal(board):
        return None
    if current_user == "X":
        return maxima(board)[1]
    else:
        return minima(board)[1]