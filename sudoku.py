import random

def create_board(height, width):
    board = [[(i + k) % 9 + 1 for i in range(1, height + 1)] for k in range(width)]
    random.shuffle(board)
    board = [[board[x][y] for x in range(9)] for y in range(9)]
    random.shuffle(board)
    return board

def print_board(board):
    for row in board:
        print(row)


board = create_board(9, 9)
# print_board(board)
def remove_numbers(board, remove_amount):
    h, w, r = len(board), len(board[0]), []
    spaces = [[x, y] for x in range(h) for y in range(w)]
    for k in range(remove_amount):
        r = random.choice(spaces)
        board[r[0]][r[1]] = 0
        spaces.remove(r)
    return board

board = remove_numbers(board, 40)
print_board(board)