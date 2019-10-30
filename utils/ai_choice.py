import random
from utils.possible_moves import (get_ai_or_human_fork_choice,
                                  get_ai_or_human_winning_choice)


def get_ai_choice(board, possible_choices):
    """
    Funtion that returns the ai's next move to either win or block a
    player from winning
    Returns:
        int: Which part on the board the ai should play
    """
    # gets a choice an ai would win if they played it
    ai_win_move = get_ai_or_human_winning_choice("O", board, possible_choices)
    if ai_win_move:
        return ai_win_move

    # gets a choice a player would win if they played it then ai blocks
    player_win_move = get_ai_or_human_winning_choice(
        "X", board, possible_choices)
    if player_win_move:
        return player_win_move

    # gets a choice if an ai played it could lead to a win on their next
    # try
    ai_fork_move = get_ai_or_human_fork_choice("O", board, possible_choices)
    if ai_fork_move:
        return ai_fork_move

    # gets a choice if an player played it could lead to a win on their
    # next try
    player_fork_move = get_ai_or_human_fork_choice(
        "X", board, possible_choices)
    if player_fork_move:
        return player_fork_move

    center_choice = 5
    if center_choice in possible_choices:
        return center_choice

    corner_choices = [1, 3, 7, 9]
    random.shuffle(possible_choices)
    for choice in possible_choices:
        if choice in corner_choices:
            return choice

    edge_choices = [2, 4, 6, 8]
    random.shuffle(possible_choices)
    for choice in possible_choices:
        if choice in edge_choices:
            return choice
