from random import randrange
from typing import Optional

ROW_COLUMN_COUNT: int = 3


def display_board(board: list[list[str]]) -> None:
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for row in range(ROW_COLUMN_COUNT):
        print("|       |       |       |")
        s: str = "|"
        for col in range(ROW_COLUMN_COUNT):
            field_index: int = (row * ROW_COLUMN_COUNT) + col
            f: str = f"{ board[row][col] if board[row][col] else field_index + 1}"
            s += f"   {f}   |"

        print(s)
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board: list[list[str]], prefix: Optional[str] = None) -> None:
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    move: str = input(f"{prefix} Enter your move [1 - 9]: ")

    if not move.isdigit():
        return enter_move(board, "No digit.")

    _move = int(move)

    if not (_move >= 1 and _move <= 9):
        return enter_move(board, "Invalid range.")

    field_index: int = _move - 1
    row: int = int(abs(field_index / ROW_COLUMN_COUNT))
    col: int = int(field_index % 3)

    if board[row][col] != "":
        return enter_move(board, "Already in use.")

    board[row][col] = "O"


def make_list_of_free_fields(board: list[list[str]]) -> list[tuple[int, int]]:
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields: list[tuple[int, int]] = []

    for row in range(ROW_COLUMN_COUNT):
        for col in range(ROW_COLUMN_COUNT):
            if board[row][col] == "":
                free_fields.append((row, col))

    return free_fields


def check_row_victory_for(board: list[list[str]], row: int, sign: str) -> bool:
    won_by_row: bool = True

    for col in range(ROW_COLUMN_COUNT):
        won_by_row = won_by_row and board[row][col] == sign

    return won_by_row


def check_col_victory_for(board: list[list[str]], col: int, sign: str) -> bool:
    won_by_col: bool = True

    for row in range(ROW_COLUMN_COUNT):
        won_by_col = won_by_col and board[row][col] == sign

    return won_by_col


def victory_for(board: list[list[str]], sign: str) -> bool:
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    # checks every row / column index
    for row_or_col in range(ROW_COLUMN_COUNT):
        # row 0 to 2
        if check_row_victory_for(board, row_or_col, sign):
            return True

        # column 0 to 2
        if check_col_victory_for(board, row_or_col, sign):
            return True

    # top left to bottom right
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    # bottom left to top right
    if board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return True

    return False


def draw_move(board: list[list[str]]):
    # The function draws the computer's move and updates the board.
    free_fields: list[tuple[int, int]] = make_list_of_free_fields(board)
    computer_move: int = randrange(len(free_fields))
    row, col = free_fields[computer_move]
    board[row][col] = "X"


def init_board() -> list[list[str]]:
    return [
        ["", "", ""],
        ["", "X", ""],
        ["", "", ""],
    ]


def game_is_running(board) -> bool:
    o_has_won: bool = victory_for(board, "O")
    x_has_won: bool = victory_for(board, "X")
    fields_free: bool = len(make_list_of_free_fields(board)) > 0

    return fields_free and not o_has_won and not x_has_won


def print_winner(board) -> None:
    o_has_won: bool = victory_for(board, "O")
    x_has_won: bool = victory_for(board, "X")

    winner: str = "no one"

    if o_has_won:
        winner = "O"

    if x_has_won:
        winner = "X"

    print(f"{winner} has won!")


def main():
    board: list[list[str]] = init_board()

    while game_is_running(board):
        display_board(board)
        enter_move(board)
        display_board(board)

        if game_is_running(board) == True:
            draw_move(board)
            display_board(board)

    print_winner(board)


if __name__ == "__main__":
    main()
