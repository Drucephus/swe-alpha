def get_board()
    # Get user input for Sudoku puzzle ('.' denotes empty cells)
    board = []
    print("Enter the Sudoku puzzle row by row (use '.' for empty cells):")
    for i in range(9):
        row_input = input(f"Row {i + 1}: ").strip()
        if len(row_input) != 9 or not all(c.isdigit() or c == '.' for c in row_input):
            print("Invalid input. Each row must contain exactly 9 characters, either digits or '.'.")
            return
        row = [int(c) if c != '.' else 0 for c in row_input]
        board.append(row)
    return board


def print_board(board):
    """Function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def main()
    """Main function."""
    board = get_board()
    print_board(board)

if __name__ == "__main__":
    main()
