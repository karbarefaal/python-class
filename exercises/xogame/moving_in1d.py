import keyboard
import os
import time

ground = [' '] * 10
pos = 5
ground[pos] = '*'
def print_ground():
    """
    os.system() runs a command as if you typed it in the terminal/command prompt.
    os.name returns the name of the operating system:
    'nt' means Windows.
    Other values (like 'posix') mean Linux/Mac.
    'cls' is the command to clear the screen in Windows Command Prompt.
    'clear' is the command to clear the screen in Linux/Mac terminals.
    The line chooses 'cls' if running on Windows, otherwise 'clear'.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(''.join(ground))

print_ground()
while True:
    if keyboard.is_pressed('left'):
        if pos > 0:
            ground[pos] = ' '
            pos -= 1
            ground[pos] = '*'
            print_ground()
            time.sleep(0.2)  # debounce