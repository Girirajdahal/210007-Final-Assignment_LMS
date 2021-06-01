from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3

#========================================== CREATING TABLE FOR DATABASE ================================================

# #Create the database or connect to one
# main_database = sqlite3.connect("library_management_system.db")

# #Creating cursor
# m = main_database.cursor()
#
# # #createing table for login and signup
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


#
# #Create the database or connect to one
# main_database = sqlite3.connect("library_management_system.db")
#
# #Creating cursor
# m = main_database.cursor()
#
# #createing table for details of the book
# m.execute("""CREATE TABLE book_detail(
#     book_name text,
#     book_id integer,
#     author text,
#     status text
#     )""")
#
#
# main_database.commit()
# main_database.close()

# #Create the database or connect to one
# main_database = sqlite3.connect("library_management_system.db")

# #Creating cursor
# m = main_database.cursor()

# #createing table for RETURNED book
# m.execute("""CREATE TABLE returnbook(
#     book_name text,
#     book_id integer,
#     author text,
#     returned_date text
#     )""")
#
#
# main_database.commit()
# main_database.close()
#

#Create the database or connect to one
# main_database = sqlite3.connect("library_management_system.db")

# #Creating cursor
# m = main_database.cursor()

# # #createing table for ISSUE BOOKS
# m.execute("""CREATE TABLE issue(
#      book_name text,
#      book_id integer,
#      author text,
#      issued_date text
#     )""")
#
# print("table created successfully")
# main_database.commit()
# main_database.close()

#=============================================ADD A BOOK DATABASE=======================================================

#Inserting data into the database
def add_a_book():
    main_database = sqlite3.connect('library_management_system.db')

    c = main_database.cursor()

    # Adding to database
    c.execute(
        "INSERT INTO book_detail VALUES(:book_name, :book_id, :author, :status )",
        {
            'book_name':e1.get(),
            'book_id': e2.get(),
            'author': e3.get(),
            'status': clicked.get()


        })

    messagebox.showinfo("a", "Data added successfully")


    main_database.commit()
    main_database.close()

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


#====================================DESIGN OF ADD A BOOK PAGE==========================================================

def add_book():
    global clicked
    global e1
    global e2
    global e3

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
    e1.focus()
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

    submit = Button(frame2, text="Submit", highlightbackground="#bfd8d5", font=("Times New Roman", 30),command=add_a_book)
    submit.grid(sticky="s", ipadx=20, ipady=20)

    frame3 = Frame(add, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", pady=20, padx=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),command = lambda:add.destroy())
    back.grid()


#=====================================DESIGN PAGE FOR UPDATE PAGE========================================================
def update_records():

    global bookname_update
    global author_update
    global updatebook
    global clicked

    updatebook = Toplevel()

    main_database = sqlite3.connect('library_management_system.db')

    c = main_database.cursor()

    record_id = bookid_entry.get()

    c.execute("SELECT * FROM book_detail WHERE book_id= " + record_id)

    datas = c.fetchall()

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

    bookname_update = Entry(frame1, width=50, font=("Times New Roman", 15))
    bookname_update.focus()
    bookname_update.grid(row=1, column=1, padx=20, pady=10, ipady=5)

    author = Label(frame1, text="Author :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    author.grid(row=3, column=0, sticky="nw", padx=1)

    author_update = Entry(frame1, width=50, font=("Times New Roman", 15))
    author_update.grid(row=3, column=1, padx=20, pady=10, ipady=5)

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

    for data in datas:
        bookname_update.insert(0, data[0])
        author_update.insert(0, data[2])
        clicked.set(data[3])




    frame2 = Frame(updatebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=20)

    submit = Button(frame2, text="Save", highlightbackground="#bfd8d5", font=("Times New Roman", 30),command=updated_data)
    submit.grid(sticky="s", ipadx=20, ipady=20)

    frame3 = Frame(updatebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", pady=20, padx=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),
                  command=lambda: updatebook.destroy())
    back.grid()

#=====================================DATABASE FOR UPDATE PAGE==========================================================

def updated_data():


    main_database = sqlite3.connect('library_management_system.db')

    c = main_database.cursor()

    record_id = bookid_entry.get()

    # Must be same name as in database
    c.execute("""UPDATE book_detail SET        
                    book_name = :bookname,
                    author = :author,
                    status = :status
                    WHERE book_id = :book_id""",

              {
                  'bookname': bookname_update.get(),
                  'author': author_update.get(),
                  'status': clicked.get(),
                  'book_id':record_id

              }
              )

    messagebox.showinfo("a", "Data updated successfully")


    main_database.commit()
    main_database.close()

    updatebook.destroy()

#================================PAGE FOR UPDATE WHICH HELPS IN OPENING RECORDS ACCORDING TO BOOK ID===================

def update():

    global bookid_entry
    update_book = Toplevel()

    # size of screen
    update_book.geometry("1920x1080")
    # title of project
    update_book.title("Library Management System")

    update_book.configure(bg="#e1e5ea")

    frame = Frame(update_book, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame.grid(row=0, column=0, padx=325, pady=50)

    # keeping title
    label = Label(frame, text="UPDATE A BOOK", bg="#a7bbc7", fg="black", font=("Times New Roman", 50))
    label.grid(row=0, column=0, columnspan=2, padx=108, pady=30)

    frame1 = Frame(update_book, bg="#a7bbc7", padx=130, pady=70, borderwidth=5, relief="solid")
    frame1.grid(row=1, column=0, padx=300, pady=20)

    # Keeping Lables that makes form

    bookid = Label(frame1, text="Book ID :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    bookid.grid(row=2, column=0, sticky="nw", padx=1)

    bookid_entry = Entry(frame1, width=50, font=("Times New Roman", 15))
    bookid_entry.focus()
    bookid_entry.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    frame2 = Frame(update_book, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=50)

    submit = Button(frame2, text="Update", highlightbackground="#bfd8d5", borderwidth=5, relief="solid", padx=20,
                    pady=20, font=("Times New Roman", 30),command=update_records)
    submit.grid()

    frame3 = Frame(update_book, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", highlightthickness=2, bd=2, padx=20, pady=20,
                  font=("Times New Roman", 30),command = lambda: update_book.destroy())
    back.grid()


#=============================================DATABASE FOR THE ISSUE BOOKS===================================================================



def issue_books():
    main_database = sqlite3.connect('library_management_system.db')

    c = main_database.cursor()

    c.execute("INSERT INTO issue  VALUES(:book_name, :book_id, :author, :issued_date)",
              {"book_name": bookname_issued.get(),
               "book_id": bookid_issued.get(),
               "author": author_issued.get(),
               # "status": clicked.get(),
               "issued_date": issuedate1.get(),
               # "returned_date":returneddate1.get()
               })


    messagebox.showinfo("a", "Book issued")

    main_database.commit()
    main_database.close()

    bookname_issued.delete(0, END)
    bookid_issued.delete(0, END)
    author_issued.delete(0, END)
    issuedate1.delete(0, END)
    # returneddate1.delete(0,END)

#===========================================DESIGN PAGE FOR ISSUE BOOKS================================================

def issue():
    global bookid_issued
    global bookname_issued
    global author_issued
    global issuedate1

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

    bookname_issued= Entry(frame1, width=50, font=("Times New Roman", 15))
    bookname_issued.focus()
    bookname_issued.grid(row=1, column=1, padx=20, pady=10, ipady=5)

    bookid = Label(frame1, text="Book ID :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    bookid.grid(row=2, column=0, sticky="nw", padx=1)

    bookid_issued= Entry(frame1, width=50, font=("Times New Roman", 15))
    bookid_issued.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    author = Label(frame1, text="Author :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    author.grid(row=3, column=0, sticky="nw", padx=1)

    author_issued = Entry(frame1, width=50, font=("Times New Roman", 15))
    author_issued.grid(row=3, column=1, padx=20, pady=10, ipady=5)

    issuedate = Label(frame1, text="Issue Date :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    issuedate.grid(row=4, column=0, sticky="nw", padx=1)

    issuedate1 = Entry(frame1, width=50, font=("Times New Roman", 15))
    issuedate1.grid(row=4, column=1, padx=20, pady=10, ipady=5)

    # Creating button which records book which are issued after it is clicked
    frame2 = Frame(issuebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=20)

    submit = Button(frame2, text="Issue", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 40),command=issue_books)
    submit.grid(sticky="s")

    # Creating a back button which takes us to the what do you want to do page
    frame3 = Frame(issuebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),command =lambda:issuebook.destroy())
    back.grid()

#==================================DATABASE FOR RETURNED BOOKS===========================================================

def returned_books():
    main_database = sqlite3.connect('library_management_system.db')

    c = main_database.cursor()

    # Adding to database
    c.execute("INSERT INTO returnbook VALUES(:book_name, :book_id, :author, :returned_date )",
        {
            'book_name': bookname_returned.get(),
            'book_id': bookid_returned.get(),
            'author': author_returned.get(),
            'returned_date': returneddate1.get()

        })

    #Popup message for the page return book
    messagebox.showinfo("a", "Book returned")

    main_database.commit()
    main_database.close()

    bookname_returned.delete(0, END)
    bookid_returned.delete(0, END)
    author_returned.delete(0, END)
    returneddate1.delete(0,END)

#================================================DESIGN PAGE FOR RETURNED BOOKS=========================================================

def returned():
    global bookname_returned
    global bookid_returned
    global author_returned
    global returneddate1


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

    bookname_returned = Entry(frame1, width=50, font=("Times New Roman", 15))
    bookname_returned.focus()
    bookname_returned.grid(row=1, column=1, padx=20, pady=10, ipady=5)

    bookid = Label(frame1, text="Book ID :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    bookid.grid(row=2, column=0, sticky="nw", padx=1)

    bookid_returned = Entry(frame1, width=50, font=("Times New Roman", 15))
    bookid_returned.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    author = Label(frame1, text="Author :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    author.grid(row=3, column=0, sticky="nw", padx=1)

    author_returned = Entry(frame1, width=50, font=("Times New Roman", 15))
    author_returned.grid(row=3, column=1, padx=20, pady=10, ipady=5)

    returneddate = Label(frame1, text="Returned Date :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    returneddate.grid(row=4, column=0, sticky="nw", padx=1)

    returneddate1 = Entry(frame1, width=50, font=("Times New Roman", 15))
    returneddate1.grid(row=4, column=1, padx=20, pady=10, ipady=5)

    frame2 = Frame(returnedbook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=20)

    submit = Button(frame2, text="Submit", highlightbackground="#bfd8d5", borderwidth=5, relief="solid", padx=20,
                    pady=20, font=("Times New Roman", 30),command=returned_books)
    submit.grid()

    frame3 = Frame(returnedbook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", highlightthickness=2, bd=2, padx=20, pady=20,
                  font=("Times New Roman", 30),command = lambda: returnedbook.destroy())
    back.grid()

#=======================================FUNCTION TO DELETE RECORDS===============================================================

def delete_the_records():
    main_database = sqlite3.connect('library_management_system.db')

    c = main_database.cursor()

    c.execute("DELETE from book_detail WHERE book_id = " + bookid_entry.get())

    bookid_entry.delete(0, END)

    #popup message when we click on delete.
    messagebox.showinfo("a", "Data deleted successfully")

    main_database.commit()
    main_database.close()

#===========================================DESIGN PAGE FOR DELETE RECORDS======================================================

def delete():
    global bookid_entry


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

    bookid_entry = Entry(frame1, width=50, font=("Times New Roman", 15))
    bookid_entry.focus()
    bookid_entry.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    frame2 = Frame(deletebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=50)

    submit = Button(frame2, text="Delete", highlightbackground="#bfd8d5", borderwidth=5, relief="solid", padx=20,
                    pady=20, font=("Times New Roman", 30),command=delete_the_records)
    submit.grid()

    frame3 = Frame(deletebook, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", highlightthickness=2, bd=2, padx=20, pady=20,
                  font=("Times New Roman", 30),command = lambda: deletebook.destroy())
    back.grid()

#============================================DESIGN PAGE FOR DASHBOARD================================================================

def dashboard():

    global dashboard_page


    dashboard_page = Toplevel()
    #size of screen
    dashboard_page.geometry("1920x1080")
    #title of project
    dashboard_page.title("Library Management System")

    dashboard_page.configure(bg="#e1e5ea")

    #making outer frame
    frame=Frame(dashboard_page,bg="#a7bbc7",borderwidth=5, relief="solid")
    frame.grid(row=0,column=0,padx=300,pady=40)


    #keeping title
    label=Label(frame,text="WHAT DO YOU WANT TO DO?",bg="#a7bbc7",fg="black",font=("Times New Roman",50))
    label.grid(row=0,column=0,columnspan=2,padx=108)

    frame1=Frame(dashboard_page,bg="#a7bbc7",padx=130,pady=70,borderwidth=5, relief="solid")
    frame1.grid(row=1,column=0,padx=300,pady=20)

    #adding BUttons
    addbook=Button(frame1,padx=62,pady=20,text="Add a book",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=add_book)
    addbook.grid(row=1,column=0,padx=20,pady=20)

    updateinfo=Button(frame1,padx=40,pady=20,text="Update Books",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=update)
    updateinfo.grid(row=1,column=1,padx=20,pady=20)

    delete1=Button(frame1,padx=50,pady=20,text="Delete Books",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=delete)
    delete1.grid(row=2,column=0,padx=20,pady=20)

    view=Button(frame1,padx=50,pady=20,text="View Books",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=show_all)
    view.grid(row=2,column=1,padx=20,pady=20)

    issuebook=Button(frame1,padx=68,pady=20,text="Issue Book",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=issue)
    issuebook.grid(row=3,column=0,padx=20,pady=20)

    returnbook=Button(frame1,padx=38,pady=20,text="Returned Book",highlightbackground="#bfd8d5",font=("Times New Roman",30),command=returned)
    returnbook.grid(row=3,column=1,padx=20,pady=20)

    #Creating another frame for button
    frame4=Frame(dashboard_page,borderwidth=5, relief="solid")
    frame4.grid(row=0,column=0,sticky="nw",padx=20,pady=20)

    #Inserting button inside the frame
    logout=Button(frame4,text="LOG-OUT",highlightbackground="#bfd8d5",font=("Times New Roman",30),padx=20,pady=20,command=logout_fun)
    logout.grid()

#=======================================FUNCTION TO LOGOUT THE FUNCTION WITH MESSAGEBOX==================================================

def logout_fun():

    v=messagebox.askquestion("a","Are you sure you want to logout?",parent=dashboard_page)
    if v == "yes":
        dashboard_page.destroy()
    else:
        dashboard_page.mainloop()

#===========================DATABASE INCLUDING POPUP FOR LOGIN===========================================================

def login_fun():

    #Create the database or connect to one
    main_database = sqlite3.connect("library_management_system.db")

    #Creating cursor
    m = main_database.cursor()

    #createing table for login and signup
    m.execute("SELECT * FROM login_and_signup")
    data=m.fetchall()


    user_name=e1.get()
    password=e2.get()

    username_all=""
    password_all=""
    for data1 in data:
        username_all += str(data1[3])
        password_all += str(data1[4])

    if e1.get() == "" or e2.get() == "":
        messagebox.showerror("Error", "Please fill up username and password")
    else:
        if user_name in username_all and password in password_all:
            e1.delete(0, END)
            e2.delete(0, END)
            messagebox.showinfo("Success", "Successfully Login")
            dashboard()

        else:
            messagebox.showerror("Error", "Invalid Username and Password")

    main_database.commit()
    main_database.close()

#==========================================DESIGN PAGE FOR THE LOGIN PAGE================================================

def login():
    global e1
    global e2
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

    e1.focus()

    e1.grid(row=1, column=1, padx=20, pady=10, ipady=5)

    password = Label(frame, text="Password", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    password.grid(row=2, column=0, pady=10)

    e2 = Entry(frame, width=30, show="*")
    e2.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    # Putting button to login
    login = Button(frame, text="LOGIN", highlightbackground="#bfd8d5", font=("Times New Roman", 30), padx=20, pady=20,command=login_fun)
    login.grid(row=6, column=0, columnspan=2, pady=30)

    frame3 = Frame(signin, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),command = lambda:signin.destroy())
    back.grid()

#===========================================DATABASE AND POPUP FOR THE SIGNUP PAGE=========================================================================

def signup_data():


    #Create the database or connect to one
    main_database = sqlite3.connect("library_management_system.db")

    #Creating cursor
    m = main_database.cursor()

    #collect/save/record/insert the data
    m.execute(" INSERT INTO login_and_signup VALUES(:f_name, :l_name, :email_id, :username, :password)",{
                "f_name":e1.get(),
                "l_name":e2.get(),
                "email_id":e3.get(),
                "username":e4.get(),
                "password":e5.get()
    })


    main_database.commit()

    main_database.close()

    if e1.get()=="" or e2.get()=="" or e3.get()==""  or e4.get()=="" or e5.get()=="":
        messagebox.showerror("Error","Please Fill up all the details")
    else:
        messagebox.showinfo("Success","Signed Up Successfully")

#clearing the previous data that was entered to signup
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

#=============================================DESIGN PAGE FOR THE SIGNUP PAGE=========================================================================

def signup():
    #assigning it as a global variable so that it can be functioned out of the loop too
    global e1
    global e2
    global e3
    global e4
    global e5
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

    e1 = Entry(frame1, width=56, font=("Times New Roman", 15))
    e1.focus()
    e1.grid(row=2, column=1, padx=20, pady=10, ipady=5)

    lastname = Label(frame1, text="Last Name :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    lastname.grid(row=3, column=0, sticky="nw", padx=1)

    e2 = Entry(frame1, width=56, font=("Times New Roman", 15))
    e2.grid(row=3, column=1, padx=20, pady=10, ipady=5)

    email = Label(frame1, text="Email Id :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    email.grid(row=4, column=0, sticky="nw", padx=1)

    e3 = Entry(frame1, width=50)
    e3.grid(row=4, column=1, padx=20, pady=10, ipady=5)

    username = Label(frame1, text="Username :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    username.grid(row=5, column=0, sticky="nw", padx=1)

    e4= Entry(frame1, width=50)
    e4.grid(row=5, column=1, padx=20, pady=10, ipady=5)

    password = Label(frame1, text="Password :", bg="#a7bbc7", fg="black", font=("Times New Roman", 30))
    password.grid(row=6, column=0, sticky="nw", padx=1)

    e5= Entry(frame1, width=50,show="*")
    e5.grid(row=6, column=1, padx=20, pady=10, ipady=5)

    frame2 = Frame(signup, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame2.grid(sticky="s", pady=20)

    submit = Button(frame2, text="Sign up", highlightbackground="#bfd8d5", font=("Times New Roman", 30),command=signup_data)
    submit.grid(sticky="s", ipadx=20, ipady=20)

    # Creating a back button which takes us to the welcome page
    frame3 = Frame(signup, bg="#a7bbc7", borderwidth=5, relief="solid")
    frame3.grid(row=0, column=0, sticky="nw", padx=20, pady=20)

    back = Button(frame3, text="Back", highlightbackground="#bfd8d5", padx=20, pady=20, font=("Times New Roman", 30),command = lambda:signup.destroy())
    back.grid(row=0,column=0)

#=====================================FUNCTION TO VIEW THE RECORDS IN TREE VIEW======================================================================

def show_all():
    all = Toplevel()
    all.title("Library Management System - Show All Datas")
    all["background"] = "#e1e5ea"
    all.geometry("1920x1080")

    style = ttk.Style()

    style.configure("Treeview",
                    foreground='black',
                    rowheight=30)

    def connect_all():
        con1 = sqlite3.connect("library_management_system.db")

        cur1 = con1.cursor()

        cur1.execute("CREATE TABLE IF NOT EXISTS viewrecords ( book_name TEXT, book_id INTEGER PRIMARY KEY, author TEXT, status TEXT)")

        con1.commit()

        con1.close()

    def View1():
        con1 = sqlite3.connect("library_management_system.db")

        cur1 = con1.cursor()

        cur1.execute("SELECT * FROM book_detail")

        rows = cur1.fetchall()

        for row1 in rows:
            print(row1)

            tree_head.insert("", END, values=row1)

        con1.close()

    # connect to the database

    connect_all()

#====================================DATA DISPLAYED IN THE DATABASE IN TREE VIEW========================================

    tree_head = ttk.Treeview(all, column=("c1", "c2", "c3","c4"), show='headings')

    tree_head.column("#1",anchor=tk.W,width=190, )

    tree_head.heading("#1", text="BOOK NAME")

    tree_head.column("#2",anchor=tk.CENTER ,width=75,)

    tree_head.heading("#2", text="BOOK ID")

    tree_head.column("#3",anchor=tk.CENTER,width=190, )

    tree_head.heading("#3", text="AUTHOR")

    tree_head.column("#4",anchor=tk.CENTER ,width=100,)

    tree_head.heading("#4", text="STATUS")


    tree_head.grid(row=0,column=0,padx=30,pady=20)

#CONNECTING TO THE DATABASE

    def connect():
        con2 = sqlite3.connect("library_management_system.db")

        cur2 = con2.cursor()

        cur2.execute("CREATE TABLE IF NOT EXISTS viewissue ( book_name TEXT, book_id INTEGER PRIMARY KEY, author TEXT, issue TEXT)")

        con2.commit()

        con2.close()

    def issue_():
        con2 = sqlite3.connect("library_management_system.db")

        cur2 = con2.cursor()

        cur2.execute("SELECT * FROM issue")

        rows = cur2.fetchall()

        for data in rows:
            print(data)

            tree.insert("", END, values=data)

        con2.close()

    # connect to the database


    connect()

    # issue1 = Toplevel()
    # issue1.title("Library Management System - issue")
    # issue1["background"] = "#e1e5ea"
    # issue1.geometry("500x500")
#====================================DATA DISPLAYED IN THE DATABASE IN TREE VIEW========================================
    tree = ttk.Treeview(all, column=("c_1", "c_2", "c_3","c_4"), show='headings')

    tree.column("#1",anchor=tk.W,width=190, )

    tree.heading("#1", text="BOOK NAME")

    tree.column("#2",anchor=tk.CENTER ,width=75,)

    tree.heading("#2", text="BOOK ID")

    tree.column("#3",anchor=tk.CENTER,width=190, )

    tree.heading("#3", text="AUTHOR")

    tree.column("#4",anchor=tk.CENTER ,width=100,)

    tree.heading("#4", text="ISSUE DATE")


    tree.grid(row=0,column=1,padx=30,pady=20)

#CONNECTING TO A DATABASE

    def connect():


        con3 = sqlite3.connect("library_management_system.db")

        cur3 = con3.cursor()

        cur3.execute("CREATE TABLE IF NOT EXISTS viewreturned ( book_name TEXT, book_id INTEGER PRIMARY KEY, author TEXT, issue TEXT)")

        con3.commit()

        con3.close()

    def View3():
        con3 = sqlite3.connect("library_management_system.db")

        cur3 = con3.cursor()
        cur3.execute("SELECT * FROM returnbook")

        rows = cur3.fetchall()

        print(rows)

        for row3 in rows:
            print(row3)

            tree_return.insert("", END, values=row3)

        con3.close()

    # connect to the database

    connect()

#======================================Data displayed in database on tree view==========================================

    tree_return = ttk.Treeview(all, column=("c1_", "c2_", "c3_","c4_"), show='headings')

    tree_return.column("#1",anchor=tk.W,width=190, )

    tree_return.heading("#1", text="BOOK NAME")

    tree_return.column("#2",anchor=tk.CENTER ,width=75,)

    tree_return.heading("#2", text="BOOK ID")

    tree_return.column("#3",anchor=tk.CENTER,width=190, )

    tree_return.heading("#3", text="AUTHOR")

    tree_return.column("#4",anchor=tk.CENTER ,width=100,)

    tree_return.heading("#4", text="RETURNED DATE")


    tree_return.grid(row=2,column=0,padx=30,pady=20)

    master = Button(all, text="ShowAll", highlightbackground="#bfd8d5", fg="#091b33", padx=20, pady=20,
                     font=("Times New Roman", 30), command=lambda :[View3(),View1(),issue_()])

    master.grid(row=2, column=1)

#============================================ROOT PAGE==========================================================================
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







