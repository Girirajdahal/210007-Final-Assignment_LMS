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
label=Label(frame,text="LOGIN PAGE",bg="#383956",fg="white",font=("Times New Roman",40))
label.grid(row=0,column=0,columnspan=2,padx=108,pady=30)
#Keeping Lables that makes form
username=Label(frame,text="Username",bg="#383956",fg="white",font=("Times New Roman",30))
username.grid(row=1,column=0,pady=10)

e1= Entry(frame, width=30)
e1.grid(row=1,column=1,padx=20,pady=10,ipady=5)

password=Label(frame,text="Password",bg="#383956",fg="white",font=("Times New Roman",30))
password.grid(row=2,column=0,pady=10)

e2= Entry(frame, width=30,show="*")
e2.grid(row=2,column=1,padx=20,pady=10,ipady=5)

login=Button(frame,text="LOGIN",highlightbackground="#bfd8d5",font=("Times New Roman",30))
login.grid(row=6,column=0,columnspan=2,pady=30)

root.mainloop()