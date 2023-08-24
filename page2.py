from tkinter import *
from tkinter import ttk
import mysql.connector
import sqlite3
from tkinter import messagebox

from PIL import ImageTk, Image


def paitent():
    global window3
    window3 = Tk()
    window3.title("Paitent")
    # window.geometry("1200x800+360+100")
    window3.state('zoomed')
    window3.resizable(0,0)
    window3.iconbitmap('hosp.ico')
    global img
    img = ImageTk.PhotoImage(Image.open(r"C:\Users\ankus\Desktop\New folder\3.jpg"))
    bg_label = Label(window3, image = img)
    bg_label.place(x=0, y=0, anchor=NW)
    lb=Label(window3,text="MANAGE PAITENT",font=("", 40, "bold"))
    lb.place(relx=0.5, rely=0.1, anchor=N)    
    
    global e1,e2,e3,e4
    e1=Entry(window3,textvar="Name",width=20,font=("Microsoft YaHei UI Light", 23, "bold"))
    e1.place(relx=0.2, rely=0.3, anchor=N)
    e1.insert(0, "Paitent's Name")
    e2=Entry(window3,textvar="specialization",width=20,font=("Microsoft YaHei UI Light", 23, "bold"))
    e2.place(relx=0.2, rely=0.4, anchor=N)
    e2.insert(0, "Gender")
    e3=Entry(window3,textvar="contact",width=20,font=("Microsoft YaHei UI Light", 23, "bold"))
    e3.place(relx=0.2, rely=0.5, anchor=N)
    e3.insert(0, "Contact No.")
    e4=Entry(window3,textvar="address",width=20,font=("Microsoft YaHei UI Light", 23, "bold"))
    e4.place(relx=0.2, rely=0.6, anchor=N)
    e4.insert(0, "Address")

    back_but=Button(window3,text="BACK",font=('calibre',18,'bold'),width=15, command= lambda : back())                         #back button
    back_but.place(x=0,y=1)
    sub_but=Button(window3,text="SUBMIT",bg="orange",font=('calibre',15,'bold'),width=15,bd=5, command= submit)
    sub_but.place(relx=0.2, rely=0.7, anchor=N)
    del_but=Button(window3,text="DELETE",bg="orange",font=('calibre',15,'bold'),width=15,bd=5, command= delete)
    del_but.place(relx=0.2, rely=0.75, anchor=N)
    del_but=Button(window3,text="SHOW",bg="orange",font=('calibre',15,'bold'),width=15,bd=5, command= show)
    del_but.place(relx=0.2, rely=0.8, anchor=N) 
    men = OptionMenu(window3)
    
   


def back():
    window3.destroy()
    
def show():
    global window6
    window6=Tk()
    window6.geometry('1000x470+770+320')
    window6.resizable(0,0)
    global tree
    tree=ttk.Treeview(window6,column=(1,2,3,4),show="headings",height=15)
    tree.column("1",width=200)
    tree.column("2",width=200)
    tree.column("3",width=200)
    tree.column("4",width=200)

    tree.heading(1,text="Paitent Name")
    tree.heading(2,text="Gender")
    tree.heading(3,text="Contact")
    tree.heading(4,text="Address")
    tree.place(relx=0.1,rely=0.2, anchor=NW)
    lb=Label(window6,text="List Of Paitent",font=('calibre',30,'bold'))
    lb.place(relx=0.5, rely=0.03, anchor=N)


    try:
        conn=sqlite3.connect('hospital.db')
        cur=conn.cursor()
        query= f"SELECT * FROM Paitent"
        cur.execute(query)
        data=cur.fetchall()
        # print(data[0])
        tree.delete(*tree.get_children())
        for i in data:
            tree.insert("","end",values=i)
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print(f"Error fetching data: {error}")


def delete():        
    delete=messagebox.askyesno("Delete","Are you sure to delete this Data")
    
    if delete == TRUE:
        
        curritm =tree.focus()
        values= tree.item(curritm, "values")
        # print(values[0])
        condition = f'''PaitentName = "{values[0]}";'''
        conn=sqlite3.connect("hospital.db")
        cur=conn.cursor()
        sql= f'''DELETE FROM Paitent WHERE {condition} '''
        cur.execute(sql)
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted"," data is Deleted")
        window6.destroy()
        


    else:
        messagebox.showinfo("Not Deleted", "No data is being deleted")
        
def submit():
    if e1.get() == "" or e3.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
    else:        
        conn=sqlite3.connect("hospital.db")
        table_query='''CREATE TABLE IF NOT EXISTS Paitent (PaitentName TEXT, Gender TEXT,Contact INT, Address TEXT)'''
        conn.execute(table_query)
        data_query='''INSERT INTO Paitent (PaitentName, Gender,Contact, Address) values (?,?,?,?)'''
        data_tuple=(
            e1.get(),
            e2.get(),
            e3.get(),
            e4.get())
    cur=conn.cursor()
    cur.execute(data_query,data_tuple)
    conn.commit()
    conn.close        