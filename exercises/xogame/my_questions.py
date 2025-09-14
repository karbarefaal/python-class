# list = [[1,1,1],[1,0,0],[1,0,0]]
# if all(element == 1 for element in list[0]):
#     print(True)
lst = [[1,1,0],
       [1,0,0],
       [1,1,0]]

# col_index = 0
value = 1
# if all(row[col_index] == value for row in lst if len(row) > col_index):
#     print(True)
if all(row[i] == "X" for row in list):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You won!")
            exit()
else: print(False)


# if any all