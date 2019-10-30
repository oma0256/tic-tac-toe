from utils.game_over import is_game_over
from utils.winner import get_winner
from utils.ai_choice import get_ai_choice

is_playing = True
while is_playing:
    board = [["_", "_", "_"] for _ in range(3)]
    possible_choices = list(range(1, 10))
    current_game = True
    first_player = input("Do you want to play first[y/n]: ")
    user_turn = True if first_player == "y" else False

    def display_board():
        """
        Function to display the game board in terminal
        """
        for row in board:
            print(row)

    display_board()

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
            choice = get_ai_choice(board, possible_choices)
        possible_choices.remove(choice)
        user_turn = not user_turn
        return choice

    while current_game:
        """
        A loop that keeps the game running until there's a winner or a tie
        """
        try:
            mark = "X" if user_turn else "O"
            choice = make_choice()
            board[(choice - 1) // 3][(choice - 1) % 3] = mark
            display_board()
            print("\n")
            current_game = not is_game_over(board)
            if not current_game:
                continue_playing = \
                    input("Do you want to play another game[y/n]: ")
                if continue_playing.lower() != 'y':
                    is_playing = False
        except Exception:
            print("Please select a number between 1 and 9 that is not yet marked")  # noqa
