# Imports go at the top
from microbit import *
# Code in a 'while True:' loop repeats forever
# https://python.microbit.org/v/3/reference/logic
b = [2]
p1 = [[4,0],[4,1]]
display.set_pixel(0, b[0], 9)
display.set_pixel(p1[0][0], p1[0][1], 9)
display.set_pixel(p1[1][0], p1[1][1], 9)
sleep(80)

def draw_pipe(x1, y1, x2, y2, n):
    display.set_pixel(x1, y1, n)
    display.set_pixel(x2, y2, n)
def draw_bird(x,y,n):
    display.set_pixel(x, y, n)
def bird_control(b):
    # control bird
    if button_a.is_pressed() and (b[0]-1)> (-1):
        y = b[0]
        b[0] = b[0]-1
        draw_bird(0, y, 0)
        draw_bird(0, b[0], 9)
        
    elif button_b.is_pressed() and (b[0]+1)< 5:
        y = b[0]
        b[0] = b[0]+1
        draw_bird(0, y, 0)
        draw_bird(0, b[0], 9)

toc_do = 1000   
dem = 1
while True:
    # pipe move
    bird_control(b)
    if p1[0][0] > 0:
        draw_pipe(p1[0][0],p1[0][1],p1[1][0],p1[1][1],0)
        p1[0][0] -= 1
        p1[1][0] -= 1
        draw_pipe(p1[0][0],p1[0][1],p1[1][0],p1[1][1],9)
        sleep(toc_do)
        if p1[0][0] == 0:
            draw_pipe(p1[0][0],p1[0][1],p1[1][0],p1[1][1],0)
            p1[0][0] = 4
            p1[1][0] = 4
            draw_pipe(p1[0][0],p1[0][1],p1[1][0],p1[1][1],9)
            sleep(100)
        dem += 1
        if dem % 5 == 0 and toc_do-200 > 0:
            toc_do -= 200
    