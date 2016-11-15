#!/usr/bin/env python

import time

from sys import platform
if platform == "linux" or platform == "linux2":
    import unicornhat as unicorn

# Turns each pixel on in turn and updates the display.
# If you're using a Unicorn HAT and only half the screen lights up,
# edit this example and change 'unicorn.AUTO' to 'unicorn.HAT' below.


if platform == "linux" or platform == "linux2":
    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(1.0)
    width, height = unicorn.get_shape()

yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0,0,0)
gray = (150,150,150)

def show_color(color):
    if platform == "linux" or platform == "linux2":  
        for y in range(height):
            for x in range(width):
                unicorn.set_pixel(x, y, color[0], color[1], color[2])
        unicorn.show()

def team_color(team_num):
    if (team_num == 0):
        color = gray
    elif (team_num == 1):
        color = blue
    elif (team_num == 2):
        color = red
    else:
        color = yellow
    show_color(color)

def show_team_battle(team_num):
    for i in range(5):
        show_color(white)
        time.sleep(0.1)
        team_color(team_num)
        time.sleep(0.1)
        show_color(white)
        time.sleep(0.1)
        team_color(team_num)
        time.sleep(0.7)


def show_team_color(team_num):
    show_color(black)
    time.sleep(0.1)
    team_color(team_num)
    time.sleep(4.9)
