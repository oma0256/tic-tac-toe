import random
from utils.winner import get_winner


def get_ai_or_human_winning_choice(mark, board, possible_choices):
    """
    Function that returns a choice if made the ai or player would win
    otherwise nothing is returned
    Args:
        mark(str): symbol used to mark the board either X or O
    Returns:
        int: choice that the ai should play next
    """
    duplicate_board = [[i for i in row] for row in board]
    counter = 0
    random.shuffle(possible_choices)
    for choice in possible_choices:
        duplicate_board[(choice - 1) // 3][(choice - 1) % 3] = mark
        winner = get_winner(duplicate_board)
        counter += 1
        if winner is not None:
            return choice
        else:
            duplicate_board = [[i for i in row] for row in board]


def get_ai_or_human_fork_choice(mark, board, possible_choices):
    """
    Function that checks if an ai or player can create a fork
    Args:
        mark(str): Symbol to mark the board with either X or O
    Returns:
        int: move to create a fork for user or ai
    """
    duplicate_board = [[i for i in row] for row in board]
    random.shuffle(possible_choices)
    for choice in possible_choices:
        duplicate_board[(choice - 1) // 3][(choice - 1) % 3] = mark
        duplicate_possible_choices = [choice for choice in possible_choices]
        duplicate_possible_choices.remove(choice)
        winning_moves = 0
        random.shuffle(duplicate_possible_choices)
        for i in duplicate_possible_choices:
            new_duplicate_board = [[i for i in row] for row in duplicate_board]
            new_duplicate_board[(i - 1) // 3][(i - 1) % 3] = mark
            winner = get_winner(new_duplicate_board)
            if winner:
                winning_moves += 1
        if winning_moves >= 2 and mark == "X":
            return choice
        elif winning_moves >= 1 and mark == "O":
            return choice
        else:
            duplicate_board = [[i for i in row] for row in board]
