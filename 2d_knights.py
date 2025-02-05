import random

n = int(input("Enter the amount of knights to be placed on the board: "))
r = 10000
c_count = 0
n_count = 0

# A function for an empty chess board
def chess_board():
    board = [["*" for _ in range(8)] for _ in range(8)]
    return board

# A function that randomly places n amount of knights on the board
def knights(board, n):
    knights = 0
    while knights < n:
        x = random.randrange(0, 8)  
        y = random.randrange(0, 8)  
        
        if board[x][y] == "*":
            board[x][y] = "N"  
            knights += 1  
    return board

# A function that checks the arrangement of these knights
def arrangement(board):
    knights = []  
    for x in range(8):
        for y in range(8):
            if board[x][y] == "N": 
                knights.append((x, y))

    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    for i in range(len(knights)):
        for j in range(i + 1, len(knights)):
            x1, y1 = knights[i]
            x2, y2 = knights[j]
            if (x1 - x2, y1 - y2) in knight_moves:
                return True 
    return False

# A function to repeat this r amount of times
def iterations(r, n, c_count, n_count):
    for _ in range(r):
        board = chess_board()  
        board = knights(board, n) 
        if arrangement(board):  
            c_count += 1 
        else:
            n_count += 1 
    return c_count, n_count  

c_count, n_count = iterations(r, n, c_count, n_count)

# Print results in a table
HORIZONTAL_LINE = "------------------------------"
challenging_percent = (c_count / r * 100)
non_challenging_percent = (n_count / r) * 100
print("When", n,  "knights are randomly placed on a chess board:")
print(HORIZONTAL_LINE)
print("   ", "Arrangement", "     ", "%")
print(HORIZONTAL_LINE)
print("   ", f"Challenging       {challenging_percent:.2f}", "%")
print("   ", f"Non Challenging   {non_challenging_percent:.2f}", "%")
print(HORIZONTAL_LINE)
