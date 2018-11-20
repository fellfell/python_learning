# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 09:01:28 2018

@author: ho
"""

import tkinter as tk

import string

import random

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")


window = tk.Tk()
window.title('letters learning')
window.geometry('600x600')

string.letters='abcdefghijklmnopqrstuvwxyz'

letter = 'a'
var_l = tk.StringVar(value='A  a')
var_b = tk.StringVar(value='NEXT')


l = tk.Label(window, textvariable=var_l, font=('Bradley Hand ITC', 200))
l.pack()

def hit_me(): 
    global letter
    random_letter = random.choice(string.letters)
    random_letter_big = random_letter.upper()
    letter =  random_letter
    to_show = random_letter_big + '  ' + random_letter
    var_l.set(to_show)
    
def speak_letter():
    speak.Speak(letter)
        
b = tk.Button(window, textvariable=var_b, width=15, height=6, command=hit_me )
b.pack()

b_read = tk.Button(window, text="read", width=15, height=6, command=speak_letter )
b_read.pack()

window.mainloop()



