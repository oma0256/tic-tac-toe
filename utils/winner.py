def get_winner(board):
    """
    Function to return thr winning mark
    Args:
        board(list): The current state of the board
    Returns:
        str: The mark of the winner either X or O
    """
    winner = None
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":  # noqa
            winner = board[i][0]
            break
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":  # noqa
            winner = board[0][i]
            break
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        winner = board[0][0]
    return winner
