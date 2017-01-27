#!/usr/bin/env python

import time
from sys import platform

redPin = 25
greenPin = 24
bluePin = 23

if platform == "linux" or platform == "linux2":
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(redPin, GPIO.OUT)
    GPIO.setup(greenPin, GPIO.OUT)
    GPIO.setup(bluePin, GPIO.OUT)

    redPWM = GPIO.PWM(redPin,100)
    greenPWM = GPIO.PWM(greenPin,100)
    bluePWM = GPIO.PWM(bluePin,100)

    yellow = (0,0,100)
    red = (0,100,100)
    blue = (100, 100, 0)
    white = (0,0,0)
    black = (100,100,100)
    gray = (50,50,50)

    redPWM.start(black[0])
    greenPWM.start(black[1])
    bluePWM.start(black[2])

def show_color(color):
    if platform == "linux" or platform == "linux2":  
        redPWM.ChangeDutyCycle(color[0])
        greenPWM.ChangeDutyCycle(color[1])
        bluePWM.ChangeDutyCycle(color[2])

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
    for i in range(10):
        show_color(white)
        time.sleep(0.1)
        team_color(team_num)
        time.sleep(0.1)
        show_color(white)
        time.sleep(0.1)
        team_color(team_num)
        time.sleep(0.7)

def show_team_color(team_num):
    team_color(team_num)
    time.sleep(10)

def shutdown():
    redPWM.stop
    greenPWM.stop
    bluePWM.stop
    GPIO.cleanup()
