import random

n = int(input("Enter the amount of queens to be placed on the board: "))
r = 10000
c_count = 0
n_count = 0

# A function for an empty chess board
def chess_board():
    board = [["*" for _ in range(8)] for _ in range(8)]
    return board

# A function that randomly places n amount of queens on the board
def queens(board, n):
    queens = 0
    while queens < n:
        x = random.randrange(0, 8)  
        y = random.randrange(0, 8)  
        
        if board[x][y] == "*":
            board[x][y] = "Q"  
            queens += 1  
    return board

# A function that checks the arrangement of these queens
def arrangement(board):
    queens = []  
    for x in range(8):
        for y in range(8):
            if board[x][y] == "Q": 
                queens.append((x, y))

    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2: 
                return True  
    return False  

# A function to repeat this r amount of times
def iterations(r, n, c_count, n_count):
    for _ in range(r):
        board = chess_board()  
        board = queens(board, n) 
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
print("When", n,  "queens are randomly placed on a chess board:")
print(HORIZONTAL_LINE)
print("   ", "Arrangement", "     ", "%")
print(HORIZONTAL_LINE)
print("   ", f"Challenging       {challenging_percent:.2f}", "%")
print("   ", f"Non Challenging   {non_challenging_percent:.2f}", "%")
print(HORIZONTAL_LINE)

