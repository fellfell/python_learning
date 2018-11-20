# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:42:34 2018

@author: ho
"""
import tkinter as tk


window = tk.Tk()
window.title('letters learning')
window.geometry('600x600')


l = tk.Label(window, text='test', bg='red',width=8,font=('',150))
l.pack()


def do_job_green():
    l.config(bg='green')
def do_job_yellow():
    l.config(bg='yellow') 
def do_job_white():
    l.config(bg='white')  
def do_job_1():
    l.config(text='1')
def do_job_2():
    l.config(text='2')
def do_job_3():
    l.config(text='3')
    
    
menubar = tk.Menu(window)

menu_A = tk.Menu(menubar, tearoff=1)
menubar.add_cascade(label='menu_A',menu=menu_A)
menu_A.add_command(label='A_green', command=do_job_green)
menu_A.add_command(label='A_yellow', command=do_job_yellow)
menu_A.add_command(label='A_white', command=do_job_white)

menu_B = tk.Menu(menubar, tearoff=1)
menubar.add_cascade(label='menu_B',menu=menu_B)
menu_B.add_command(label='B_1', command=do_job_1)
menu_B.add_command(label='B_2', command=do_job_2)
menu_B.add_command(label='B_3', command=do_job_3)


window.config(menu=menubar)





window.mainloop()
