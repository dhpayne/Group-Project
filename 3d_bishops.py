import random

n = int(input("Enter the amount of bishops to be placed on the board: "))
r = 10000
c_count = 0
n_count = 0

# A function for an empty 3d chess board
def chess_board():
    board = [[["*" for _ in range(8)] for _ in range(8)] for _ in range(8)]
    return board

# A function that randomly places n amount of bishops on the 3d board
def bishops(board, n):
    bishops = 0
    while bishops < n:
        x = random.randrange(0, 8)  
        y = random.randrange(0, 8)  
        z = random.randrange(0, 8)
        
        if board[x][y][z] == "*":
            board[x][y][z] = "B"  
            bishops += 1  
    return board

# A function that checks the arrangement of these bishops
def arrangement(board):
    bishops = []  
    for x in range(8):
        for y in range(8):
            for z in range(8):
                if board[x][y][z] == "B": 
                   bishops.append((x, y, z))

    for i in range(len(bishops)):
        for j in range(i + 1, len(bishops)):
            x1, y1, z1 = bishops[i]
            x2, y2, z2 = bishops[j]
            if abs(x1 - x2) == abs(y1 - y2) and z1 == z2 \
            or abs(x1 - x2) == abs(z1 - z2) and y1 == y2 \
            or abs(y1 - y2) == abs(y1 - y2) and x1 == x2 \
            or abs(x1 - x2) == abs(y1 - y2) == abs(z1 - z2):
                return True  
    return False  

# A function to repeat this r amount of times
def iterations(r, n, c_count, n_count):
    for _ in range(r):
        board = chess_board()  
        board = bishops(board, n) 
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
print("When", n,  "bishops are randomly placed on a 3d chess board:")
print(HORIZONTAL_LINE)
print("   ", "Arrangement", "     ", "%")
print(HORIZONTAL_LINE)
print("   ", f"Challenging       {challenging_percent:.2f}", "%")
print("   ", f"Non Challenging   {non_challenging_percent:.2f}", "%")
print(HORIZONTAL_LINE)

