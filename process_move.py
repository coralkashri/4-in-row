import sys

def load_board():
    with open("README.md", "r") as f:
        lines = f.readlines()
    # Extract board lines
    board = [line.strip().split() for line in lines[1:7]]
    return board

def save_board(board):
    with open("README.md", "w") as f:
        f.write("1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣\n")
        for row in board:
            f.write(" ".join(row) + "\n")

def drop_piece(board, column, piece):
    for row in reversed(board):
        if row[column] == "⚪":
            row[column] = piece
            return True
    return False

if __name__ == "__main__":
    comment = sys.argv[1]
    user = sys.argv[2]

    board = load_board()
    column = int(comment.split()[1]) - 1  # Parse `drop X` input
    piece = "🔴" if user == "player1" else "🟡"

    if not drop_piece(board, column, piece):
        print("Column full. Move invalid.")
        sys.exit(1)

    save_board(board)
