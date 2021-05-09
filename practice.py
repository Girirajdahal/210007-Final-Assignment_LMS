from tkinter import*
from PIL import ImageTk,Image
import sqlite3

# #Create the database or connect to one
# main_database = sqlite3.connect("library_management_system.db")
#
# #Creating cursor
# m = main_database.cursor()
#
# #createing table for login and signup
# m.execute("""CREATE TABLE login_and_signup(
#     first_name text,
#     last_name text,
#     email_id text,
#     username text,
#     password text
#     )""")
#
# main_database.commit()
# main_database.close()


# #Create the database or connect to one
# main_database = sqlite3.connect("add_a_book.db")
#
# #Creating cursor
# m = main_database.cursor()
#
# #createing table for add a book
# m.execute("""CREATE TABLE main_database(
#     name text,
#     book_id integer,
#     author text,
#     status text,
# )""")




def login():


    signin = Toplevel()

    # size of screen
    signin.geometry("1920x1080")
    # title of project
    signin.title("Library Management System")

    signin.configure(bg="#e1e5ea")

    frame = Frame(signin, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame.grid(row=0, column=0, padx=430, pady=200)

    # keeping title
    label = Label(frame, text="Please Enter the details", bg="#a7bbc7", fg="black", font=("Times New Roman", 40))
    label.grid(row=0, column=0, columnspan=2, padx=108, pady=30)
    # Keeping Lables and entries that makes form of the login page
    username = Label(frame, text="Username", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    username.grid(row=1, column=0, pady=10)

    e1 = Entry(frame, width=30)
    e1.grid(row=1, column=1, padx=20, pady=10, ipady=5)

    password = Label(frame, text="Password", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    password.grid(row=2, column=0, pady=10)

    e2 = Entry(frame, width=30, show="*")
    e2.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    # Putting button to login
    login = Button(frame, text="LOGIN", highlightbackground="#bfd8d5", font=("Times New Roman", 30), padx=20, pady=20)
    login.grid(row=6, column=0, columnspan=2, pady=30)

    frame3 = Frame(signin, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),command = lambda:signin.destroy())
    back.grid()

def signup():

    signup = Toplevel()

    # size of screen
    signup.geometry("1920x1080")
    # title of project
    root.title("Library Management System")

    root.configure(bg="#e1e5ea")

    frame = Frame(signup, bg="#a7bbc7", borderwidth=5, relief="solid", )
    frame.grid(row=0, column=0, padx=200, pady=20)

    # keeping title
    label = Label(frame, text="SIGN UP", bg="#a7bbc7", fg="black", padx=0, pady=0, font=("Times New Roman", 40))
    label.grid(row=0, column=0, columnspan=2, padx=108, pady=10)

    frame1 = Frame(signup, bg="#a7bbc7", padx=130, pady=70, borderwidth=5, relief="solid", )
    frame1.grid(row=1, column=0, padx=200, pady=10)

    # Keeping Lables that and entries that makes form for adding book

    text = Label(frame1, text="Please fill up the following details :", bg="#a7bbc7", fg="black",
                   font=("Times New Roman", 35))
    text.grid(row=1, column=0, padx=150, pady=10, sticky="nw", columnspan=2)

    firstname = Label(frame1, text="First Name :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    firstname.grid(row=2, column=0, sticky="nw", padx=1)

    e2 = Entry(frame1, width=56, font=("Times New Roman", 15))
    e2.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    lastname = Label(frame1, text="Last Name :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    lastname.grid(row=3, column=0, sticky="nw", padx=1)

    e3 = Entry(frame1, width=56, font=("Times New Roman", 15))
    e3.grid(row=3, column=1, padx=20, pady=10, ipady=5)

    email = Label(frame1, text="Email Id :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    email.grid(row=4, column=0, sticky="nw", padx=1)

    e3 = Entry(frame1, width=50)
    e3.grid(row=4, column=1, padx=20, pady=10, ipady=5)

    username = Label(frame1, text="Username :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    username.grid(row=5, column=0, sticky="nw", padx=1)

    e4 = Entry(frame1, width=50)
    e4.grid(row=5, column=1, padx=20, pady=10, ipady=5)

    password = Label(frame1, text="Password :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    password.grid(row=6, column=0, sticky="nw", padx=1)

    e5 = Entry(frame1, width=50)
    e5.grid(row=6, column=1, padx=20, pady=10, ipady=5)

    frame2 = Frame(signup, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=20)

    submit = Button(frame2, text="Sign up", highlightbackground="#bfd8d5", font=("Times New Roman", 30))
    submit.grid(sticky="s", ipadx=20, ipady=20)

    # Creating a back button which takes us to the welcome page
    frame3 = Frame(signup, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),command = lambda:signup.destroy())
    back.grid()




root=Tk()

#size of screen
root.geometry("1920x1080")
#title of project
root.title("Library Management System")

#opening the image
bg=Image.open("lib23.png")

#resizing the image
resized = bg.resize((1435,765),Image.ANTIALIAS)

#assigning the resized image
bgnew=ImageTk.PhotoImage(resized)

#putting it on screen
my_label= Label(root,image=bgnew)
my_label.grid(row=0,column=0)

#creating frame for text
frame=Frame(root,bg="#bfd8d5",borderwidth=5, relief="solid",)
frame.grid(row=0,column=0)

#Including text which says Library Management System
label2=Label(frame,text="LIBRARY MANAGEMENT SYSTEM",bg="#b67162",fg="white",font=("Times New Roman",50))
label2.grid()

#Creating another frame for button
frame1=Frame(root,borderwidth=5, relief="solid",)
frame1.grid(row=0,column=0,sticky="ne",padx=20,pady=20)

#Inserting button inside the frame
signin=Button(frame1,text="SIGN IN",highlightbackground="#bfd8d5",font=("Times New Roman",30),padx=30,pady=30,command=login)
signin.grid()

#Creating frame for the sign up button

frame2=Frame(root,borderwidth=5, relief="solid",)
frame2.grid(row=0,column=0,sticky="ne",padx=220,pady=20)

signup=Button(frame2,text="SIGN UP",highlightbackground="#bfd8d5",font=("Times New Roman",30),padx=30,pady=30,command=signup)
signup.grid()
root.mainloop()




from tkinter import*
from PIL import ImageTk,Image
def add():
    from PIL import ImageTk, Image
    add = Toplevel()

    # size of screen
    add.geometry("1920x1080")
    # title of project
    add.title("Library Management System")

    add.configure(bg="#e1e5ea")

    frame = Frame(add, bg="#a7bbc7", borderwidth=5, relief="solid", )
    frame.grid(row=0, column=0, padx=325, pady=20)

    # keeping title
    label = Label(frame, text="ADD A BOOK", bg="#a7bbc7", fg="black", padx=0, pady=0, font=("Times New Roman", 50))
    label.grid(row=0, column=0, columnspan=2, padx=108, pady=30)

    frame1 = Frame(add, bg="#a7bbc7", padx=130, pady=70, borderwidth=5, relief="solid", )
    frame1.grid(row=1, column=0, padx=325, pady=20)

    # Keeping Lables that and entries that makes form for adding book

    name = Label(frame1, text="Name :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    name.grid(row=1, column=0, pady=10, sticky="nw", padx=1)

    e1 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e1.grid(row=1, column=1, padx=20, pady=10, ipady=5)

    id = Label(frame1, text="Book Id :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    id.grid(row=2, column=0, sticky="nw", padx=1)

    e2 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e2.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    author = Label(frame1, text="Author :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    author.grid(row=3, column=0, sticky="nw", padx=1)

    e3 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e3.grid(row=3, column=1, padx=20, pady=10, ipady=5)

    status = Label(frame1, text="Status :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    status.grid(row=4, column=0, sticky="nw", padx=1)

    # Creating dropdown for status
    def show():
        Label.config(text=clicked.get())

    # making Dropdown menu option into list
    option = [
        "Available",
        "Issued"

    ]
    # data type of menu text
    clicked = StringVar()
    # initial menu text
    clicked.set("Select")
    # creating drop down menu
    drop = OptionMenu(frame1, clicked, *option)
    drop.config(width=34, borderwidth=4, bg="white", font=("Times New Roman", 15))
    drop.grid(row=4, column=1, padx=20, pady=10, ipadx=54, ipady=8)

    # e3= Entry(frame, width=50)
    # e3.grid(row=3,column=1,padx=20,pady=10,ipady=5)

    frame2 = Frame(add, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=20)

    submit = Button(frame2, text="Submit", highlightbackground="#bfd8d5", font=("Times New Roman", 30))
    submit.grid(sticky="s", ipadx=20, ipady=20)

    frame3 = Frame(add, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", pady=20, padx=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),command = lambda:add.destroy())
    back.grid()

def issue():

    issuebook = Toplevel()

    # size of screen
    issuebook.geometry("1920x1080")
    # title of project
    issuebook.title("Library Management System")

    issuebook.configure(bg="#e1e5ea")

    frame = Frame(issuebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame.grid(row=0, column=0, padx=325, pady=20)

    # keeping title
    label = Label(frame, text="ISSUE A BOOK", bg="#a7bbc7", fg="black", font=("Times New Roman", 50))
    label.grid(row=0, column=0, columnspan=2, padx=108, pady=30)

    frame1 = Frame(issuebook, bg="#a7bbc7", padx=130, pady=70, borderwidth=5, relief="solid")
    frame1.grid(row=1, column=0, padx=300, pady=20)

    # Keeping Lables and entries that makes form for issuing book

    bookname = Label(frame1, text="Book Name :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    bookname.grid(row=1, column=0, pady=10, sticky="nw", padx=1)

    e1 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e1.grid(row=1, column=1, padx=20, pady=10, ipady=5)

    bookid = Label(frame1, text="Book ID :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    bookid.grid(row=2, column=0, sticky="nw", padx=1)

    e2 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e2.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    author = Label(frame1, text="Author :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    author.grid(row=3, column=0, sticky="nw", padx=1)

    e3 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e3.grid(row=3, column=1, padx=20, pady=10, ipady=5)

    issuedate = Label(frame1, text="Issue Date :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    issuedate.grid(row=4, column=0, sticky="nw", padx=1)

    e3 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e3.grid(row=4, column=1, padx=20, pady=10, ipady=5)

    # Creating button which records book which are issued after it is clicked
    frame2 = Frame(issuebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=20)

    submit = Button(frame2, text="Issue", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 40))
    submit.grid(sticky="s")

    # Creating a back button which takes us to the what do you want to do page
    frame3 = Frame(issuebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),command =lambda:issuebook.destroy())
    back.grid()

def returned():
    returnedbook = Toplevel()

    # size of screen
    returnedbook.geometry("1920x1080")
    # title of project
    returnedbook.title("Library Management System")

    #putting background color
    returnedbook.configure(bg="#e1e5ea")

    frame = Frame(returnedbook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame.grid(row=0, column=0, padx=325, pady=20)

    # keeping title
    label = Label(frame, text="RETURNED BOOK", bg="#a7bbc7", fg="black", font=("Times New Roman", 50))
    label.grid(row=0, column=0, columnspan=2, padx=108, pady=30)

    frame1 = Frame(returnedbook, bg="#a7bbc7", padx=130, pady=70, borderwidth=5, relief="solid")
    frame1.grid(row=1, column=0, padx=300, pady=20)

    # Keeping Lables that makes form

    bookname = Label(frame1, text="Book Name: ", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    bookname.grid(row=1, column=0, pady=10, sticky="nw", padx=1)

    e1 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e1.grid(row=1, column=1, padx=20, pady=10, ipady=5)

    bookid = Label(frame1, text="Book ID :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    bookid.grid(row=2, column=0, sticky="nw", padx=1)

    e2 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e2.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    name = Label(frame1, text="Name :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    name.grid(row=3, column=0, sticky="nw", padx=1)

    e3 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e3.grid(row=3, column=1, padx=20, pady=10, ipady=5)

    returneddate = Label(frame1, text="Returned Date :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    returneddate.grid(row=4, column=0, sticky="nw", padx=1)

    e3 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e3.grid(row=4, column=1, padx=20, pady=10, ipady=5)

    frame2 = Frame(returnedbook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=20)

    submit = Button(frame2, text="Submit", highlightbackground="#bfd8d5", borderwidth=5, relief="solid", padx=20,
                    pady=20, font=("Times New Roman", 30))
    submit.grid()

    frame3 = Frame(returnedbook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", highlightthickness=2, bd=2, padx=20, pady=20,
                  font=("Times New Roman", 30),command = lambda: returnedbook.destroy())
    back.grid()

def delete():


    deletebook = Toplevel()

    # size of screen
    deletebook.geometry("1920x1080")
    # title of project
    deletebook.title("Library Management System")

    deletebook.configure(bg="#e1e5ea")

    frame = Frame(deletebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame.grid(row=0, column=0, padx=325, pady=50)

    # keeping title
    label = Label(frame, text="DELETE BOOK", bg="#a7bbc7", fg="black", font=("Times New Roman", 50))
    label.grid(row=0, column=0, columnspan=2, padx=108, pady=30)

    frame1 = Frame(deletebook, bg="#a7bbc7", padx=130, pady=70, borderwidth=5, relief="solid")
    frame1.grid(row=1, column=0, padx=300, pady=20)

    # Keeping Lables that makes form

    bookid = Label(frame1, text="Book ID :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    bookid.grid(row=2, column=0, sticky="nw", padx=1)

    e2 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e2.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    frame2 = Frame(deletebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=50)

    submit = Button(frame2, text="Delete", highlightbackground="#bfd8d5", borderwidth=5, relief="solid", padx=20,
                    pady=20, font=("Times New Roman", 30))
    submit.grid()

    frame3 = Frame(deletebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", highlightthickness=2, bd=2, padx=20, pady=20,
                  font=("Times New Roman", 30),command = lambda: deletebook.destroy())
    back.grid()

def update():
    updatebook = Toplevel()

    # size of screen
    updatebook.geometry("1920x1080")
    # title of project
    updatebook.title("Library Management System")

    updatebook.configure(bg="#e1e5ea")

    frame = Frame(updatebook, bg="#a7bbc7", borderwidth=5, relief="solid", )
    frame.grid(row=0, column=0, padx=325, pady=20)

    # keeping title
    label = Label(frame, text="UPDATE A BOOK", bg="#a7bbc7", fg="black", padx=0, pady=0, font=("Times New Roman", 50))
    label.grid(row=0, column=0, columnspan=2, padx=108, pady=30)

    frame1 = Frame(updatebook, bg="#a7bbc7", padx=130, pady=70, borderwidth=5, relief="solid", )
    frame1.grid(row=1, column=0, padx=325, pady=20)

    # Keeping Lables that and entries that makes form for adding book

    name = Label(frame1, text="Name :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    name.grid(row=1, column=0, pady=10, sticky="nw", padx=1)

    e1 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e1.grid(row=1, column=1, padx=20, pady=10, ipady=5)

    id = Label(frame1, text="Book Id :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    id.grid(row=2, column=0, sticky="nw", padx=1)

    e2 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e2.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    author = Label(frame1, text="Author :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    author.grid(row=3, column=0, sticky="nw", padx=1)

    e3 = Entry(frame1, width=50, font=("Times New Roman", 15))
    e3.grid(row=3, column=1, padx=20, pady=10, ipady=5)

    status = Label(frame1, text="Status :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    status.grid(row=4, column=0, sticky="nw", padx=1)

    # Creating dropdown for department
    def show():
        Label.config(text=clicked.get())

    # making Dropdown menu option into list
    option = [
        "Available",
        "Issued"

    ]
    # data type of menu text
    clicked = StringVar()
    # initial menu text
    clicked.set("Select")
    # creating drop down menu
    drop = OptionMenu(frame1, clicked, *option)
    drop.config(width=34, borderwidth=4, bg="white", font=("Times New Roman", 15))
    drop.grid(row=4, column=1, padx=20, pady=10, ipadx=54, ipady=8)

    # e3= Entry(frame, width=50)
    # e3.grid(row=3,column=1,padx=20,pady=10,ipady=5)

    frame2 = Frame(updatebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=20)

    submit = Button(frame2, text="Submit", highlightbackground="#bfd8d5", font=("Times New Roman", 30))
    submit.grid(sticky="s", ipadx=20, ipady=20)

    frame3 = Frame(updatebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", pady=20, padx=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),command = lambda:updatebook.destroy())
    back.grid()




dashboard=Tk()
#size of screen
dashboard.geometry("1920x1080")
#title of project
dashboard.title("Library Management System")

dashboard.configure(bg="#e1e5ea")
#
#making outer frame
frame=Frame(dashboard,bg="#a7bbc7",borderwidth=5, relief="solid")
frame.grid(row=0,column=0,padx=300,pady=40)


#keeping title
label=Label(frame,text="WHAT DO YOU WANT TO DO?",bg="#a7bbc7",fg="black",font=("Times New Roman",50))
label.grid(row=0,column=0,columnspan=2,padx=108)

frame1=Frame(dashboard,bg="#a7bbc7",padx=130,pady=70,borderwidth=5, relief="solid")
frame1.grid(row=1,column=0,padx=300,pady=20)

#adding BUttons
addbook=Button(frame1,padx=62,pady=20,text="Add a book",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=add)
addbook.grid(row=1,column=0,padx=20,pady=20)

updateinfo=Button(frame1,padx=40,pady=20,text="Update Books",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=update)
updateinfo.grid(row=1,column=1,padx=20,pady=20)

delete=Button(frame1,padx=50,pady=20,text="Delete Books",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=delete)
delete.grid(row=2,column=0,padx=20,pady=20)

view=Button(frame1,padx=50,pady=20,text="View Books",highlightbackground="#bfd8d5",font=("Times New Roman",30))
view.grid(row=2,column=1,padx=20,pady=20)

issuebook=Button(frame1,padx=68,pady=20,text="Issue Book",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=issue)
issuebook.grid(row=3,column=0,padx=20,pady=20)

returnbook=Button(frame1,padx=38,pady=20,text="Returned Book",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=returned)
returnbook.grid(row=3,column=1,padx=20,pady=20)

#Creating another frame for button
frame4=Frame(dashboard,borderwidth=5, relief="solid")
frame4.grid(row=0,column=0,sticky="nw",padx=20,pady=20)

#Inserting button inside the frame
logout=Button(frame4,text="LOG-OUT",highlightbackground="#bfd8d5",font=("Times New Roman",30),padx=20,pady=20)
logout.grid()


dashboard.mainloop()
