from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttb
from PIL import ImageTk, Image
import sys





window = ttb.Window()
window.title("login")
window.geometry("1200x800+360+100")
# window.state('zoomed')
window.resizable(0,0)
window.iconbitmap('hosp.ico')

left_frame = Frame(window, width=600, height=800)
# left_frame.pack()
left_frame.place(anchor=NW, relx=0.1, rely=0.1)
#place the image file location here
img = ImageTk.PhotoImage(Image.open(r"C:\Users\ankus\Desktop\New folder\1.jpg"))
bg_label = Label(left_frame, image = img)
bg_label.pack()

right_frame = Frame(window, width=600, height=800, background= 'white')
# right_frame.pack()
right_frame.place(x= 600, y=0)

Signin= Label(right_frame, text= "Sign in", font=("Microsoft YaHei UI Light", 23, "bold"), fg="cornflowerblue", bg="white")
Signin.config(fg="cornflowerblue", bg="white" )
Signin.place(relx=0.28, rely= 0.25, anchor=NW)
user_name = Entry(right_frame,width=20, font=("Microsoft YaHei UI Light", 12), fg="black", bg="white", border=0)
user_name.place(relx=0.3, rely=0.4, anchor= NW)
user_name.insert(0, "username")
password = Entry(right_frame,width=20, font=("Microsoft YaHei UI Light", 12), fg="black", bg="white", border=0, show="*")
password.place(relx=0.3, rely=0.5, anchor= NW)
password.insert(0, "password")

from page1 import doctor
from page2 import paitent
from page3 import apointment

def login ():
    if user_name.get() =="username" and password.get() == "password":
        global window1
        window1 = tk.Tk()
        window1.title("admin panel")
        window1.state("zoomed")
        window1.iconbitmap('hosp.ico')
        head1 = tk.Frame(window1, width= 1920, height=100)
        head1.place(x=0, y= 100, anchor=NW)
        head2 = tk.Frame(window1, width= 1920, height=200)
        head2.place(x=0, y= 300, anchor=NW)
        head3 = tk.Frame(window1, width= 1920, height=200)
        head3.place(x=0, y= 600, anchor=NW)        
        
        head_admin = tk.Label(head1, text= "Admin panel", font=("Microsoft YaHei UI Light", 23, "bold"), fg="cornflowerblue", bg="white")
        head_admin.config(fg='cornflowerblue', font=("Microsoft YaHei UI Light", 30, "bold"))
        head_admin.place(relx=0.5, rely=0.1, anchor=N)
        
        butt1 = tk.Button(head2, text="Doctor", border= 0, width= 90, height=10, command= lambda: doctor())
        butt1.place(x=100, y=0, anchor=NW)
        butt2 = tk.Button(head2, text="Appointments", border= 0, width= 90, height=10, command= apointment)
        butt2.place(x=1100, y=0, anchor=NW)

        butt3 = tk.Button(head3, text="Paitents", border= 0, width= 90, height=10, command= paitent)
        butt3.place(x=100, y=0, anchor=NW)
        butt4 = tk.Button(head3, text="Exit", border= 0, width= 90, height=10, command= lambda: window1.quit())
        butt4.place(x=1100, y=0, anchor=NW)

        window.destroy()
    else:
        messagebox.showerror("ERROR","Your Username and Password is Wrong")
        


sign_button= ttb.Button(right_frame, width=20 , text="Log in", command= lambda: login())
sign_button.place(x= 180, y=460)



window.mainloop()