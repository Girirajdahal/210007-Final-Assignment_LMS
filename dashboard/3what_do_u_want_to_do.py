from tkinter import*
from PIL import ImageTk,Image


root=Tk()
#size of screen
root.geometry("1920x1080")
#title of project
root.title("Library Management System")
#
#opening the image
bg=Image.open("finalassignmentpic.png")

#resizing the image
resized = bg.resize((1435,765),Image.ANTIALIAS)

#assigning the resized image
bgnew=ImageTk.PhotoImage(resized)

#putting it on screen
my_label= Label(root,image=bgnew)
my_label.grid(row=0,column=0)

#making outer frame
frame=Frame(root,bg="#383956")
frame.grid(row=0,column=0,padx=325,pady=20)

#keeping title
label=Label(frame,text="WHAT DO YOU WANT TO DO?",bg="#383956",fg="white",font=("Times New Roman",40))
label.grid(row=0,column=0,columnspan=2,padx=108)

#adding BUttons
addbook=Button(frame,padx=62,pady=20,text="Add a book",highlightbackground="#bfd8d5",font=("Times New Roman",30))
addbook.grid(row=1,column=0,padx=20,pady=20)

updateinfo=Button(frame,padx=20,pady=20,text="Update Information",highlightbackground="#bfd8d5",font=("Times New Roman",30))
updateinfo.grid(row=1,column=1,padx=20,pady=20)

delete=Button(frame,padx=20,pady=20,text="Delete information",highlightbackground="#bfd8d5",font=("Times New Roman",30))
delete.grid(row=2,column=0,padx=20,pady=20)

search=Button(frame,padx=20,pady=20,text="Search Information",highlightbackground="#bfd8d5",font=("Times New Roman",30))
search.grid(row=2,column=1,padx=20,pady=20)

issuebook=Button(frame,padx=68,pady=20,text="Issue Book",highlightbackground="#bfd8d5",font=("Times New Roman",30))
issuebook.grid(row=3,column=0,padx=20,pady=20)

returnbook=Button(frame,padx=48,pady=20,text="Returned Book",highlightbackground="#bfd8d5",font=("Times New Roman",30))
returnbook.grid(row=3,column=1,padx=20,pady=20)



root.mainloop()