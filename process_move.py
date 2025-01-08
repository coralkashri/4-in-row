import sys

def load_board():
    with open("README.md", "r") as f:
        lines = f.readlines()
    # Extract board lines
    lines_before = []
    lines_after = []
    
    before_board = True
    for line in lines:
        if any(x in line for x in ["⚪", "🔴", "🟡"]):
               before_board = False
               board.insert(line.strip().split())
        else:
            if before_board:
                lines_before.insert(line)
            else:
                lines_after.insert(line)
    return (board, lines_before, lines_after)

def save_board(board, lines_before, lines_after):
    with open("README.md", "w") as f:
        for line in lines_before:
            f.write(line)
        #f.write("1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣\n")
        for row in board:
            f.write(" ".join(row) + "\n")
        for line in lines_after:
            f.write(line)

def drop_piece(board, column, piece):
    for row in reversed(board):
        if row[column] == "⚪":
            row[column] = piece
            return True
    return False

if __name__ == "__main__":
    comment = sys.argv[1]
    user = sys.argv[2]

    (board, before, after) = load_board()
    column = int(comment.split()[1]) - 1  # Parse `drop X` input
    piece = "🔴" if user == "player1" else "🟡"

    if not drop_piece(board, column, piece):
        print("Column full. Move invalid.")
        sys.exit(1)

    save_board(board, before, after)
