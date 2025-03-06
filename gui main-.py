# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

from tkinter import *
import tkinter as tk
#from tkvideo import tkvideo

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import sqlite3
#import tfModel_test as tf_test
global fn
fn=""


root=tk.Tk()

root.title("Employee TurnOver Prediction")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
bg= Image.open(r"img1.jpg")

bg.resize((2000,600),Image.ANTIALIAS)
#print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=100, relwidth=1, relheight=1)
#bg_lb2 = tk.Label(root,image.open("logo.jpg")
#img=ImageTk.PhotoImage(Image.open("logo.jpg"))
#img_lbl=tk.Label(root,image=img,borderwidth = 0, highlightthickness = 0)
#img_lbl.place(x=100, y=20)
#img1=ImageTk.PhotoImage(Image.open("img2.jpg"))

#img2=ImageTk.PhotoImage(Image.open("img4.jpeg"))

#img3=ImageTk.PhotoImage(Image.open("img3.jpeg"))

logo_label=tk.Label()
logo_label.place(x=100,y=200)

x = 1


# def move():
# 	global x
# 	if x == 4:
# 		x = 1
# 	if x == 1:
# 		logo_label.config(image=img1)
# 	elif x == 2:
# 		logo_label.config(image=img2)
# 	elif x == 3:
# 		logo_label.config(image=img3)
# 	x = x+1
# 	root.after(2000, move)

# calling the function
#move()
#

w = tk.Label(root, text="Employee TurnOver Prediction",width=25,background="#454b1b",foreground="white",height=2,font=("Times new roman",25,"bold") )
w.place(x=520,y=10)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#454b1b")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


#wlcm=tk.Label(root,text="Music Recommendation System Using Machine Learning",width=90,height=3,background="#C4A484", foreground="white",font=("Times new roman",22,"bold"))
#wlcm.place(x=0,y=620)




d2=tk.Button(root,text="Login",command=Login,width=25,height=2,bd=0,background="#454b1b",foreground="white",font=("Times new roman",17,"bold"))
d2.place(x=600,y=300)


d3=tk.Button(root,text="Register",command=Register,width=25,height=2,bd=0,background="#454b1b",foreground="white",font=("Times new roman",17,"bold"))
d3.place(x=600,y=400)



root.mainloop()