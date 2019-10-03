import random

board = [["_", "_", "_"] for _ in range(3)]
possible_choices = list(range(1, 10))
is_playing = True
first_player = input("Do you want to play first[y/n]: ")
user_turn = True if first_player == "y" else False


def display_board():
    """
    Function to display the game board in terminal
    """
    for row in board:
        print(row)

display_board()


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
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            winner = board[i][0]
            break
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board[0][i]
            break
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        winner = board[0][0]
    return winner


def get_ai_or_human_winning_choice(mark):
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
        if choice == 8:
            print(duplicate_board)
        winner = get_winner(duplicate_board)
        counter += 1
        if winner is not None:
            return choice
        else:
            duplicate_board = [[i for i in row] for row in board]


def get_ai_or_human_fork_choice(mark):
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


def get_ai_choice():
    """
    Funtion that returns the ai's next move to either win or block a
    player from winning
    Returns:
        int: Which part on the board the ai should play
    """
    # gets a choice an ai would win if they played it
    ai_win_move = get_ai_or_human_winning_choice("O")
    if ai_win_move:
        return ai_win_move

    # gets a choice a player would win if they played it then ai blocks
    player_win_move = get_ai_or_human_winning_choice("X")
    if player_win_move:
        return player_win_move

    # gets a choice if an ai played it could lead to a win on their next
    # try
    ai_fork_move = get_ai_or_human_fork_choice("O")
    if ai_fork_move:
        return ai_fork_move

    # gets a choice if an player played it could lead to a win on their
    # next try
    player_fork_move = get_ai_or_human_fork_choice("X")
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


def make_choice():
    """
    Function that makes a choice to be played either by allowing a user
    to input their choice or selecting a choice for the ai
    Returns:
        int: the next move to be played either by the user or ai
    """
    global user_turn
    if user_turn:
        choice = int(input("Please select a number between 1 and 9: "))
        if choice not in possible_choices:
            raise Exception
    else:
        choice = get_ai_choice()
    possible_choices.remove(choice)
    user_turn = not user_turn
    return choice


def check_winner(board):
    """
    Function that prints winner of the game
    Args:
        board(list): Current state of the board
    """
    winner = get_winner(board)
    if winner:
        print(f"You Win") if winner == "X" else print("You Loose")
    return winner


def check_draw(winner):
    """
    Function that checks if the game is a tie
    """
    if not winner and all("_" not in row for row in board):
        print("Game is a tie")
        return True


def is_game_over():
    """
    Function that checks if the game has a winner or there's a tie
    Returns:
        boolean: True if the game has a winner or it's a tie otherwise
                 False
    """
    winner = check_winner(board)
    draw = check_draw(winner)
    return True if winner or draw else False


while is_playing:
    """
    A loop that keeps the game running until there's a winner or a tie
    """
    try:
        mark = "X" if user_turn else "O"
        choice = make_choice()
        board[(choice - 1) // 3][(choice - 1) % 3] = mark
        display_board()
        is_playing = not is_game_over()
    except:
        print("Please select a number between 1 and 9 that is not yet marked")
