from tkinter import*
from PIL import ImageTk,Image
root=Tk()

#size of screen
root.geometry("1920x1080")
#title of project
root.title("Library Management System")

#opening the image
bg=Image.open("finalassignmentpic.png")

#resizing the image
resized = bg.resize((1435,765),Image.ANTIALIAS)

#assigning the resized image
bgnew=ImageTk.PhotoImage(resized)

#putting it on screen
my_label= Label(root,image=bgnew)
my_label.grid(row=0,column=0)

frame=Frame(root,bg="#bfd8d5")
frame.grid(row=0,column=0)


label2=Label(frame,text="LIBRARY MANAGEMENT SYSTEM",bg="#bfd8d5",fg="black",font=("Times New Roman",50))
label2.grid()

frame1=Frame(root)
frame1.grid(row=0,column=0,pady=170,sticky="s")

welcome=Button(frame1,text="SIGN IN",highlightbackground="#bfd8d5",font=("Times New Roman",30),padx=30,pady=30)
welcome.grid()

root.mainloop()
