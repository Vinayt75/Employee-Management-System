from customtkinter import *
from PIL import Image
from tkinter import messagebox


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All field requried')
    elif usernameEntry.get()=='vinay' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems

    else:
        messagebox.showerror('Error','Invalid login credentials')


root=CTk()
root.geometry('930x622')
root.resizable(0,0)
root.title('login page')
image=CTkImage(Image.open('pack.jpg'),size=(930,622))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text='Employee Management System',bg_color='#E1F3FD',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headingLabel.place(x=20,y=100)

usernameEntry= CTkEntry(root,placeholder_text='Enter the Username',width=180)
usernameEntry.place(x=50,y=150)

passwordEntry= CTkEntry(root,placeholder_text='Enter the Password',width=180,show='*')
passwordEntry.place(x=50,y=200)

loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=70,y=250)
root.mainloop()