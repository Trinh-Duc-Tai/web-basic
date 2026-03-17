# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
b = [2]
p1 = [[4,0],[4,1]]
p2 = [[4,3],[4,4]]
display.set_pixel(0, b[0], 9)
display.set_pixel(p1[0][0], p1[0][1], 9)
display.set_pixel(p1[1][0], p1[1][1], 9)
sleep(1500)
display.set_pixel(p2[0][0], p2[0][1], 9)
display.set_pixel(p2[1][0], p2[1][1], 9)
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
def pipe_run(pipe,toc_do,dem):
    if pipe[0][0] > 0:
        draw_pipe(pipe[0][0],pipe[0][1],pipe[1][0],pipe[1][1],0)
        pipe[0][0] -= 1
        pipe[1][0] -= 1
        draw_pipe(pipe[0][0],pipe[0][1],pipe[1][0],pipe[1][1],9)
        sleep(toc_do)
        if pipe[0][0] == 0:
            draw_pipe(pipe[0][0],pipe[0][1],pipe[1][0],pipe[1][1],0)
            pipe[0][0] = 4
            pipe[1][0] = 4
            draw_pipe(pipe[0][0],pipe[0][1],pipe[1][0],pipe[1][1],9)
            sleep(100)
        

toc_do = 1000
dem = 1
while True:
    # pipe move
    bird_control(b)
    pipe_run(p1,toc_do,dem)
    pipe_run(p2,toc_do,dem)
    dem += 1
    if dem % 5 == 0 and toc_do-200 > 0:
        toc_do -= 200
