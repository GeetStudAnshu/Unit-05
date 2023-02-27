from tkinter import *
import mysql.connector as MySQLDb
import tkinter.messagebox

# GUI Window
root = Tk()
root.geometry("600x400")
root.title("SQL CRUD Operations")

# GUI Widgets
id = Label(root, text="User ID:")
id.place(x=20, y=50)
idE = Entry(root)
idE.place(x=100, y=50)
name = Label(root, text="Enter Name:")
name.place(x=20, y=80)
nameE = Entry(root)
nameE.place(x=100, y=80)
email = Label(root, text="Enter Email:")
email.place(x=20, y=110)
emailE = Entry(root)
emailE.place(x=100, y=110)

# GUI Button Functions
def Insert():
    id = idE.get()
    name = nameE.get()
    email = emailE.get()

    if (id == "" or name == "" or email == ""):
        tkinter.messagebox.showinfo("ALERT", "Please enter all fields")
    else:
        con = MySQLDb.connect(host="localhost", user="root", password="",
                            database="userinfo")
        cursor = con.cursor()
        cursor.execute("insert into udata values(" + id + ", '" + name + "', '" + email + "')")
        cursor.execute("commit")
        tkinter.messagebox.showinfo("Status", "Successfully Inserted")
        con.close()

def View():
    if (idE.get() == ""):
        tkinter.messagebox.showinfo("Alert", "ID is required to fetch data")
    else:
        con = MySQLDb.connect(host="localhost", user="root", password="",
                              database="userinfo")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM udata where id="+idE.get()+"")
        rows = cursor.fetchall()

        for row in rows:
            nameE.insert(0, row[1])
            emailE.insert(0, row[2])
        con.close()

def Update():
    if(idE.get() == ""):
        tkinter.messagebox.showinfo("Alert!", "ID is required!")
    else:
        con = MySQLDb.connect(host="localhost", user="root", password="", database="userinfo")
        cursor = con.cursor()
        cursor.execute("UPDATE udata SET name='"+nameE.get()+"', email='"+emailE.get()+"' WHERE id="+idE.get()+"")
        cursor.execute("commit")
        tkinter.messagebox.showinfo("Success", "Data Updated Successfully!")
        con.close()

def Delete():
    if(idE.get() == ""):
        tkinter.messagebox.showinfo("Alert!", "ID is required!")
    else:
        con = MySQLDb.connect(host="localhost", user="root", password="", database="userinfo")
        cursor = con.cursor()
        cursor.execute("DELETE from udata where id="+idE.get()+"")
        cursor.execute("commit");

        idE.delete(0, 'end')
        nameE.delete(0, 'end')
        emailE.delete(0, 'end')
        tkinter.messagebox.showinfo("Success!", "Data Deleted Successfully!")
        con.close()

btnInsert = Button(root, text="Insert", command=Insert)
btnInsert.place(x=20, y=150)
btnView = Button(root, text="View", command=View)
btnView.place(x=70, y=150)
btnUpdate = Button(root, text="Update", command=Update)
btnUpdate.place(x=120, y=150)
btnDelete = Button(root, text="Delete", command=Delete)
btnDelete.place(x=180, y=150)


root.mainloop()

