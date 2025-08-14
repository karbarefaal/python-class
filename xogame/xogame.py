import keyboard
import os
import time
import random



def ground_maker(n):
    ground = []
    for i in range(n):
        ground.append([])
        for j in range(n):
            ground[i].append(' ')
    return ground

def play_ground(cursor_x,cursor_y,put_sth= False):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len_ground):
        print(' ---' * 3)
        print('|',end=' ')
        for j in range(len_ground):
            if ground[i][j] in ["X","O"]:
                if not put_sth:
                    print(ground[i][j],'|',end= ' ')
                elif put_sth:
                    while not is_draw(ground):
                        rand_x = random.randint(0,2)
                        rand_y = random.randint(0,2)
                        if ground[rand_x][rand_y] == " ":
                            ground[rand_x][rand_y] = "O"
                            print(ground[i][j],'|',end= ' ')
                            put_sth = False
                            break
                    else:
                        game_result(ground)

            else:
                if i == cursor_y and j == cursor_x:

                    ground[i][j] = '?'
                    print(ground[i][j],'|',end= ' ')

                else:
                    ground[i][j] = ' '
                    print(ground[i][j],end=' ')
                    print('|',end= ' ')
        print()
    for x in range(len_ground):
        print(' ---',end='')
    print()

def game_result(list: list):
    for i in range(len(list)):
        # for columns
        if all(row[i] == "X" for row in list):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You won!")
            exit()
        elif all(row[i] == "O" for row in list):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You lost!")
            exit()
        # for rows
        # for j in list[i]:
        elif all(j == "X" for j in list[i]):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You won!")
            exit()
        # for j in list[i]:
        elif all(j == "O" for j in list[i]):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You lost!")
            exit()

        # for diagon
        elif all(list[i][i] == "X" for i in range(len(list))):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You won!")
            exit()
        elif all(list[i][i] == "O" for i in range(len(list))):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You lost!")
            exit()

        # for anti-diagon
        elif all(list[len(ground) -i -1][i] == "X" for i in range(3)):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You won!")
            exit()
        elif all(list[len(ground) - i -1][i] == "O" for i in range(3)):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You lost!")
            exit()
    # Draw
    if is_draw(list):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Draw!")
        exit()    

def is_draw(list):
    for row in list:
        for cell in row:
            if cell == ' ' or cell == '?':
                return False
    return True

def keyboard_play(cursor_x,cursor_y):
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            moved = False
            put_sth = False
            if event.name == 'left' and cursor_x > 0:
                cursor_x -= 1
                moved = True
            elif event.name == 'right' and cursor_x < len_ground - 1:
                cursor_x += 1
                moved = True
            elif event.name == 'up' and cursor_y > 0:
                cursor_y -= 1
                moved = True
            elif event.name == 'down' and cursor_y < len_ground - 1:
                cursor_y += 1
                moved = True
            elif event.name == 'space' and ground[cursor_y][cursor_x] == '?':
                ground[cursor_y][cursor_x] = 'X'
                moved = True
                put_sth = True
            # elif event.name == 'o' and ground[cursor_y][cursor_x] == '?':
            #     ground[cursor_y][cursor_x] = 'O'
            #     moved = True
            #     put_sth = True
            elif event.name == 'esc':
                print('Done!')
                break
            if moved:
                if put_sth == False:
                    play_ground(cursor_x,cursor_y)
                else:
                    time.sleep(0.2)
                    play_ground(cursor_x,cursor_y,put_sth)
                    time.sleep(0.5)

                    put_sth = False
                    game_result(ground)


if __name__ == "__main__":
    ground = ground_maker(3)
    cursor_x,cursor_y = 0,0
    len_ground = len(ground)
    play_ground(cursor_x,cursor_y)
    keyboard_play(cursor_x,cursor_y)

            
