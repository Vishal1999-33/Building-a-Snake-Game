#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

curses.initscr() # causes the first refresh operation to clear the screen.
win = curses.newwin(20, 60, 0, 0) # creates a new window(int nlines, int ncols, int begin_y, int begin_x)
win.keypad(True) # enabling keypad mode so that curses can read the multibyte escape sequence which terminal
              #returns in the form of special keys.
curses.noecho() # to turn off automatic echoing of keys to the screen, in order to be able
                #to read keys and only display them under certain circumstances.
curses.curs_set(0) #sets the appearance of the cursor based on the value of visibility:0: invisible 1: visible 2: very visible
win.border(0) #draw a border around the edges of the window.'0' used sets all the parameters to their default values.
win.nodelay(1) #in no-delay mode, -1 is returned if there is no input, else getch() waits until a key is pressed.

key = KEY_RIGHT  # initializing values
score = 0

snake = [[4,10], [4,9], [4,8]]  # initializing snake co-ordinates.
food = [10,20] # first food coordinates.

win.addch(food[0], food[1], '*') #painting at most n(1) characters of the string str at (y, x)(food[1],food[0]) with attributes attr(*).

while key != 27: # while Esc key is not pressed.
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ') # printing 'Score'
    win.addstr(0, 27, ' SNAKE ') # 'SNAKE' strings
    win.timeout(int(150 - (len(snake)/5 + len(snake)/10)%120))  # increases the speed of Snake as its length increases.
    
    prevKey = key # to save previously pressed key.
    event = win.getch() #to get a character.
    key = key if event == -1 else event 
    
    if key == ord(' '): # If SPACE BAR is pressed, wait for another one (Pause/Resume).
        key = -1                                                   
        while key != ord(' '):  #ord(character):represents integer that represents particular character.
            key = win.getch()
        key = prevKey
        continue
    
    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]: # if an invalid key is pressed
        key = prevKey
        
    # calculating the new coordinates of the head of the snake as len(snake) increases.This is taken care of later at [1].
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # If snake crosses the boundaries, make it enter from the other side
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

    # If snake runs over itself
    if snake[0] in snake[1:]: break

    if snake[0] == food: # when snake eats the food
        food = []
        score += 1
        while food == []:
            food = [randint(1, 18), randint(1, 58)] # calculating next food's coordinates
            if food in snake: food = []
        win.addch(food[0], food[1], '*')
    else:    
        last = snake.pop() # [1] if it does not eat the food, length decreases
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#') # increasing the length of snake.
    
curses.endwin()
print("\nScore - " + str(score))
print("Thank You For Playing")


# In[ ]:




