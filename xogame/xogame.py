import keyboard

ground = [['?','?','?'],['?','?','?'],['?','?','?']]
len_ground_x = len(ground)
# cursor_x,cursur_y = 0,0
# len_ground_y = len(ground[0])
# print(len_ground_x,len_ground_y)

def play_ground():
    for i in range(0,len_ground_x):
        for x in range(0,len_ground_x):
            print(' ---',end='')
        print()
        print('|',end=' ')
        for j in range(0,len_ground_x):
            # if i == cursur_y and j == cursor_x:
            print(ground[i][j],end=' ')
            print('|',end= ' ')
        print()
    for x in range(0,len_ground_x):
        print(' ---',end='')
    print()

play_ground()

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'esc':
            print('Done!')
            exit()
        elif event.name == 'left':
            pass


