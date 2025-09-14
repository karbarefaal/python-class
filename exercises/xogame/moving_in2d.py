import keyboard
import os
import time

def ground_maker(n):
    return [[' ' for _ in range(n)] for _ in range(n)]

ground = ground_maker(3)
len_ground = len(ground)
cursor_x, cursor_y = 0, 0

def play_ground():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len_ground):
        print(' ---' * len_ground)
        print('|', end=' ')
        for j in range(len_ground):
            if i == cursor_y and j == cursor_x:
                print('*', end=' | ')
            else:
                print(ground[i][j], end=' | ')
        print()
    print(' ---' * len_ground)

play_ground()

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
        time.sleep(0.2)  # debounce