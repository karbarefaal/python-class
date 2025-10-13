def check_winner(board):
    # == for row
    n = len(board)
    count = 0
    for i in range(n):
        if count == 3:
            print("You win in row")
            return "X"
        else:
            count = 0
        for j in range(n):
            if board[i][j] == "X":
                count += 1
    # == for column
    for i in range(n):
        count = 0
        for j in range(n):
            if board[j][i] == "X":
                count += 1
        if count == 3:
            print("You win in column")
            return "X"
    # == for main diagonal
    count = 0
    for i in range(n):
        if board[i][i] == "X":
            count += 1
    
    minor_diagonal = 0
    if count == 3:
        print("You win in main diagonal")
        return "X"
    # == for minor diagonal
    for i in range(n):
        if board[i][n-i-1] == "X":
            minor_diagonal += 1
    if minor_diagonal == 3:
        print("You win minor diagonal")
        return "X"
    #==================draw check===========================
    count = 0
    for i in my_list:
        if "" not in i:
            count += 1
        else:
            print("please play the game")
            return "No winner"
        if count == 3:
            print("Nobody wins")
            return "Nobody wins"
#==============================================================
count = 0
my_list = []
for i in range(3):
    for j in range(3):
        count += 1
        print(count,end="\t")
    print()
player1 = input("player1: please choose a number with X: ")
player2 = input("player2: please choose a number with O: ")

my_list = [["","bdvb","fds"],["fd","fds","vfsdv"],["fsdaf","fds","fdas"]]
check_winner(my_list)