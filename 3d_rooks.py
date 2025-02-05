import random

n = int(input("Enter the amount of rooks to be placed on the board: "))
r = 10000
c_count = 0
n_count = 0

# A function for an empty 3d chess board
def chess_board():
    board = [[["*" for _ in range(8)] for _ in range(8)] for _ in range(8)]
    return board

# A function that randomly places n amount of rooks on the 3d board
def rooks(board, n):
    rooks = 0
    while rooks < n:
        x = random.randrange(0, 8)  
        y = random.randrange(0, 8)  
        z = random.randrange(0, 8)
        
        if board[x][y][z] == "*":
            board[x][y][z] = "R"  
            rooks += 1  
    return board

# A function that checks the arrangement of these rooks
def arrangement(board):
    rooks = []  
    for x in range(8):
        for y in range(8):
            for z in range(8):
                if board[x][y][z] == "R": 
                   rooks.append((x, y, z))

    for i in range(len(rooks)):
        for j in range(i + 1, len(rooks)):
            x1, y1, z1 = rooks[i]
            x2, y2, z2 = rooks[j]
            if x1 == x2 and  y1 == y2 or x1 == x2 and z1 == z2 or y1 == y2 and z1 == z2:
                return True  
    return False  

# A function to repeat this r amount of times
def iterations(r, n, c_count, n_count):
    for _ in range(r):
        board = chess_board()  
        board = rooks(board, n) 
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
print("When", n,  "rooks are randomly placed on a 3d chess board:")
print(HORIZONTAL_LINE)
print("   ", "Arrangement", "     ", "%")
print(HORIZONTAL_LINE)
print("   ", f"Challenging       {challenging_percent:.2f}", "%")
print("   ", f"Non Challenging   {non_challenging_percent:.2f}", "%")
print(HORIZONTAL_LINE)
