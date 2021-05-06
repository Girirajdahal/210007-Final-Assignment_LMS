from tkinter import*
from PIL import ImageTk,Image
root=Tk()

#size of screen
root.geometry("1920x1080")
#title of project
root.title("Library Management System")

#opening the image
bg=Image.open("../dashboard/finalassignmentpic.png")

#resizing the image
resized = bg.resize((1435,765),Image.ANTIALIAS)

#assigning the resized image
bgnew=ImageTk.PhotoImage(resized)

#putting it on screen
my_label= Label(root,image=bgnew)
my_label.grid(row=0,column=0)

frame=Frame(root,bg="#383956")
frame.grid(row=0,column=0,padx=325,pady=20)

#keeping title
label=Label(frame,text="RETURNED BOOK",bg="#383956",fg="white",font=("Times New Roman",40))
label.grid(row=0,column=0,columnspan=2,padx=108,pady=30)
#Keeping Lables that makes form

bookname=Label(frame,text="Book Name",bg="#383956",fg="white",font=("Times New Roman",30))
bookname.grid(row=1,column=0,pady=10,sticky="nw",padx=1)

e1= Entry(frame, width=50)
e1.grid(row=1,column=1,padx=20,pady=10,ipady=5)

bookid=Label(frame,text="Book ID",bg="#383956",fg="white",font=("Times New Roman",30))
bookid.grid(row=2,column=0,sticky="nw",padx=1)

e2= Entry(frame, width=50)
e2.grid(row=2,column=1,padx=20,pady=10,ipady=5)

name=Label(frame,text="Name",bg="#383956",fg="white",font=("Times New Roman",30))
name.grid(row=3,column=0,sticky="nw",padx=1)

e3= Entry(frame, width=50)
e3.grid(row=3,column=1,padx=20,pady=10,ipady=5)

returneddate=Label(frame,text="Returned Date",bg="#383956",fg="white",font=("Times New Roman",30))
returneddate.grid(row=4,column=0,sticky="nw",padx=1)

e3= Entry(frame, width=50)
e3.grid(row=4,column=1,padx=20,pady=10,ipady=5)

submit=Button(frame,text="Submit",highlightbackground="#bfd8d5",padx=10,pady=10,font=("Times New Roman",30))
submit.grid(row=6,column=0,columnspan=2,pady=30)



root.mainloop()