from utils.winner import get_winner


def check_winner(board):
    """
    Function that prints winner of the game
    Args:
        board(list): Current state of the board
    """
    winner = get_winner(board)
    if winner:
        print(f"Game Over, You Win") if winner == "X" else print("Game Over, You Loose")  # noqa
    return winner


def check_draw(winner, board):
    """
    Function that checks if the game is a tie
    """
    if not winner and all("_" not in row for row in board):
        print("Game Over, game is a tie")
        return True


def is_game_over(board):
    """
    Function that checks if the game has a winner or there's a tie
    Returns:
        boolean: True if the game has a winner or it's a tie otherwise
                False
    """
    winner = check_winner(board)
    draw = check_draw(winner, board)
    return True if winner or draw else False
