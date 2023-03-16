from tkinter import * #to import tkinter library
import mysql.connector as MySQLDb #to use mysql as MySQLdb
import tkinter.messagebox #to use messagebox
import matplotlib.pyplot as plt #to use matplotlib graph plotting 

# GUI Window
root = Tk()
root.geometry("250x250")
root.title("SQL CRUD Operations using GUI and Map Plotting")

# GUI Widgets
name = Label(root, text="Fruit Name:")
name.place(x=20, y=50)
nmE = Entry(root)
nmE.place(x=100, y=50)
taste = Label(root, text="Fruit Taste:")
taste.place(x=20, y=80)
tstE = Entry(root)
tstE.place(x=100, y=80)
price = Label(root, text="Fruit Price:")
price.place(x=20, y=110)
prE = Entry(root)
prE.place(x=100, y=110)

# GUI Button Functions
def Insert():
    name = nmE.get()
    taste = tstE.get()
    price = prE.get()

    if (name == "" or taste == "" or price == ""):
        tkinter.messagebox.showinfo("ALERT", "Please enter all fields")
    else:
        con = MySQLDb.connect(host="localhost", user="root", password="",
                            database="fshop")
        cursor = con.cursor()
        cursor.execute("insert into fruits values('" + name + "', '" + taste + "', '" + price + "')")
        cursor.execute("commit")
        nmE.delete(0, 'end')
        tstE.delete(0, 'end')
        prE.delete(0, 'end')
        tkinter.messagebox.showinfo("Status", "Successfully Inserted")
        con.close()

def View():
    if (nmE.get() == ""):
        tkinter.messagebox.showinfo("Alert", "Name is required to fetch data")
    else:
        con = MySQLDb.connect(host="localhost", user="root", password="",
                              database="fshop")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM fruits where name='"+nmE.get()+"'")
        rows = cursor.fetchall()
        nmE.delete(0, 'end')
        tstE.delete(0, 'end')
        prE.delete(0, 'end')
        for row in rows:
            nmE.insert(0, row[0])
            tstE.insert(0, row[1])
            prE.insert(0, row[2])
        con.close()

def Update():
    if(nmE.get() == ""):
        tkinter.messagebox.showinfo("Alert!", "ID is required!")
    else:
        con = MySQLDb.connect(host="localhost", user="root", password="", database="fshop")
        cursor = con.cursor()
        cursor.execute("UPDATE fruits SET taste='"+tstE.get()+"', price='"+prE.get()+"' WHERE name='"+nmE.get()+"'")
        cursor.execute("commit")
        tkinter.messagebox.showinfo("Success", "Data Updated Successfully!")
        nmE.delete(0, 'end')
        tstE.delete(0, 'end')
        prE.delete(0, 'end')
        con.close()

def Delete():
    if(nmE.get() == ""):
        tkinter.messagebox.showinfo("Alert!", "ID is required!")
    else:
        con = MySQLDb.connect(host="localhost", user="root", password="", database="fshop")
        cursor = con.cursor()
        cursor.execute("DELETE from fruits where name='"+nmE.get()+"'")
        cursor.execute("commit")

        nmE.delete(0, 'end')
        tstE.delete(0, 'end')
        prE.delete(0, 'end')
        tkinter.messagebox.showinfo("Success!", "Data Deleted Successfully!")
        con.close()
#crud operations end, plotting functions start
def BarChart():
    con = MySQLDb.connect(host="localhost", user="root", password="",
                              database="fshop")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM fruits")
    rows = cursor.fetchall()
    name = []
    taste = []
    price = []
    for r in rows:
        name.append(r[0])
        price.append(r[2])
    
    plt.bar(name, price)
    plt.ylim(0, 150)
    plt.xlabel("Name of Fruits")
    plt.ylabel("Price of Fruits")
    plt.title("Froot Ki Dukaan")
    plt.show()
    con.close()

def PieChart():
    mydb = MySQLDb.connect(host="localhost",user="root",password="",database="fshop")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT taste, COUNT(*) FROM fruits GROUP BY taste")
    results = mycursor.fetchall()
    tastes = [result[0] for result in results]
    counts = [result[1] for result in results]
    sour_index = tastes.index('Sour')
    sweet_index = tastes.index('Sweet')
    sour_count = counts[sour_index]
    sweet_count = counts[sweet_index]
    labels = ['Sour', 'Sweet']
    sizes = [sour_count, sweet_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Number of Fruits by Taste')
    plt.show()
    mydb.close()

#functions relevant to buttons end, buttons section start
btnInsert = Button(root, text="Insert", command=Insert)
btnInsert.place(x=20, y=150)
btnView = Button(root, text="View", command=View)
btnView.place(x=70, y=150)
btnUpdate = Button(root, text="Update", command=Update)
btnUpdate.place(x=120, y=150)
btnDelete = Button(root, text="Delete", command=Delete)
btnDelete.place(x=180, y=150)
btnGraph1 = Button(root, text="Bar Chart", command=BarChart)
btnGraph1.place(x=20, y=180, width=80)
btnGraph2 = Button(root, text="Pie Chart", command=PieChart)
btnGraph2.place(x=110, y=180, width=80)

root.mainloop() #print the gui widget window (for output)
