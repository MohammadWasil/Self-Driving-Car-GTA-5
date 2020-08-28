# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:05:43 2020

@author: wasil
"""
# Code: https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

import ctypes
import time

import Download_Direct_Keys
from Download_Direct_Keys import Direct_Keys

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

accelerate = 'DIK_W'
back = 'DIK_S'
left = 'DIK_A'
right = 'DIK_D'
space = 'DIK_SPACE'

W = Download_Direct_Keys.direct_key_dictionary[accelerate]
S = Download_Direct_Keys.direct_key_dictionary[back]
A = Download_Direct_Keys.direct_key_dictionary[left]
D = Download_Direct_Keys.direct_key_dictionary[right]
SPACE = Download_Direct_Keys.direct_key_dictionary[space]


# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
while (True):

    PressKey(W)
    time.sleep(2)
    ReleaseKey(W)
    time.sleep(2)
