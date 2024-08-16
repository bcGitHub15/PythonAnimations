#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 20:55:59 2018

Three-slit phasor animation.
The blue lines are the phasors from the slits and the orange
line is the total. It's length is proportional to the brightness.
This version keeps the first slit as the reference so that it stays put.
It also plots (in green) the total intensity at each point in the pattern.

@author: bcollett
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

minmax = 2.5

fig, ax = plt.subplots()
ax.set_xlim(-1.5, minmax+2)
ax.set_ylim(-minmax, minmax)
ax.set_title("Animated Phasor Plot for Three Slits")
dtheta = 0.008

y = np.zeros(5)+ 100
x=np.array([0,1,2,3,4])
y1 = np.zeros(2)+100
x1=np.array([0,4])
#x2=np.zeros(10000)
#x2[2]=0.1
#y2=np.zeros(10000)-3
x2=[]
y2=[]
line1, = ax.plot(x, y,'o-')
line2, = ax.plot(x1, y1)
line3, =ax.plot(x2,y2)


def init():  # only required for blitting to give a clean slate.
    line1.set_xdata([0,0,0,0,0])
    line1.set_ydata([0,1,2,3,4])
    line2.set_xdata([0,0])
    line2.set_ydata([0,4])
    line3.set_xdata(x2)
    line3.set_ydata(y2)
    return line1,line2,line3


def animate(i):
    theta = dtheta * i
    c1 = np.cos(0)
    c2 = np.cos(theta)
    c3 = np.cos(2*theta)
    s1 = np.sin(0)
    s2 = np.sin(theta)
    s3 = np.sin(2*theta)
    ctot = c1+c2+c3
    stot = s1+s2+s3
    x2.append(theta/4-1.5)
    y2.append((ctot*ctot+stot*stot)/4)
#    x2[i+2]=theta/3
#    y2[i+2]=np.sqrt(ctot*ctot+stot*stot)-3
    line1.set_xdata([0, c1, c1+c2,c1+c2+c3, ctot])
    line1.set_ydata([0, s1, s1+s2,s1+s2+s3, stot])
    line2.set_xdata([0, ctot])
    line2.set_ydata([0, stot])
    line3.set_xdata(x2)
    line3.set_ydata(y2)
    return line1,line2,line3


ani = animation.FuncAnimation(
   fig, animate, init_func=init, interval=1, blit=False, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()