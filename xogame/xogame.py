import keyboard
import os
import time

def ground_maker(n):
    ground = []
    for i in range(n):
        ground.append([])
        for j in range(n):
            ground[i].append(' ')
    return ground

ground = ground_maker(3)
len_ground = len(ground)
cursor_x,cursor_y = 0,0

def play_ground():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len_ground):
        for x in range(len_ground):
            print(' ---',end='')
        print()
        print('|',end=' ')
        for j in range(len_ground):
            if i == cursor_y and j == cursor_x:
                if ground[i][j] != 'X' or ground[i][j] != 'O':
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

play_ground()

<<<<<<< HEAD
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        moved = False
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
        elif event.name == 'x' and ground[cursor_y][cursor_x] == '?':
            ground[cursor_y][cursor_x] = 'X'
            print(ground[cursor_y][cursor_x])
            moved = True
        elif event.name == 'o' and ground[cursor_y][cursor_x] == '?':
            ground[cursor_y][cursor_x] = 'O'
            play_ground()
        elif event.name == 'esc':
            print('Done!')
            break
=======
def my_game():
    while True:
        moved = False
        if keyboard.is_pressed('left'):
            if cursor_x > 0:
                cursor_x -= 1
                moved = True
        elif keyboard.is_pressed('right'):
            if cursor_x < len_ground - 1:
                cursor_x += 1
                moved = True
        elif keyboard.is_pressed('up'):
            if cursor_y > 0:
                cursor_y -= 1
                moved = True
        elif keyboard.is_pressed('down'):
            if cursor_y < len_ground - 1:
                cursor_y += 1
                moved = True
        if moved:
            play_ground()
            time.sleep(0.3)  # debounce
            
my_game()





    # if event.event_type == keyboard.KEY_DOWN:
    #     if event.name == 'esc':
    #         print('Done!')
    #         exit()
>>>>>>> f0e580650a043662358422b3872d9a5f0af8dc0e

        if moved:
            
            play_ground()
            time.sleep(0.1)
            
