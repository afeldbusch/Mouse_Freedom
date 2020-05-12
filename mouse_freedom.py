# -*- coding: utf-8 -*-
"""
Mouse Freedom: This program moves the mouse through sticky corners in Windows 10
"""

from ctypes import Structure, c_long, byref
import ctypes
user32 = ctypes.windll.user32

monSize1 = {'mon1_x':1920, 'mon1_y':1080, 'mon2_x':1920, 'mon2_y':1080}
monSize2 = {'mon1_x':1366, 'mon1_y':768, 'mon2_x':1360, 'mon2_y':768}


class POINT(Structure):
    _fields_ = [('x', c_long),('y',c_long)]
    

def queryMousePos():
    pt = POINT()
    user32.GetCursorPos(byref(pt))
    return {"x": pt.x, "y": pt.y}


def moveMouse():

    pos = queryMousePos()

    if pos['x'] == monSize['mon1_x']-1 and pos['y'] <=4:
        user32.SetCursorPos(monSize['mon1_x']+1, pos['y'])
        
    if pos['x'] == monSize['mon1_x']-1 and pos['y'] >= min(monSize['mon1_y']-5,monSize['mon2_y']):
        user32.SetCursorPos(monSize['mon1_x']+1, min(pos['y'],monSize['mon2_y']))
        
    if pos['x'] == monSize['mon1_x'] and pos['y'] <= 4:
        user32.SetCursorPos(monSize['mon1_x']-2, pos['y'])
        
    if pos['x'] == monSize['mon1_x'] and pos['y'] >= min(monSize['mon1_y']-5,monSize['mon2_y']):
        user32.SetCursorPos(monSize['mon1_x']-2, min(pos['y'],monSize['mon2_y']))     
        


if __name__ == "__main__":
    print("""Mouse Freedom: This script helps move mouse from one monitor to the next
on a multiple monitor setup. Verify your monitor config matches below, or edit in the script
to match your config.
          
Keep this window open!!!\n""")
    print("""1: 2x 1920x1080 monitors
2: 1366x768 as primary (left), 1360x768 as secondary (right)
What screen config do you want to use: 1 or 2\n""")
    screen_config = input()
    if screen_config == '1':
        monSize = monSize1
        print('Config 1 active')
    elif screen_config == '2':
        monSize = monSize2
        print('Config 2 active')
    else:
        print('Config not supported yet')
        
    while True:
        moveMouse()
