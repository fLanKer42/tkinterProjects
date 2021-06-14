from tkinter import *
from main_page import *
from read_file import *

class starter:
    start = 0
starter1 = starter()


#creating reader object and reading files
file_data = reader()
file_data.read_userdb()
users = file_data.users

file_data.read_messagedb()

#creating window
root = Tk()
root.title("KGPbook")
root.configure(background='#383636')
root.geometry('1000x500')


#this function opens actual social network widow by creating a page object
def open_page(user_name):        
    for i in range(len(users)):
        if user_name == users[i]:
            starter1.start = 1
            page_creater = page()
            page_creater.current_page = i
            page_creater.create_page(root, file_data)
            break
    

#this function displays the login page
def login_page():
    #handles clicking of login button
    def login_click():
        entry_id = entry.get()
        if entry_id in users:
            entry.destroy()
            heading.destroy()
            button_login.destroy()
            open_page(entry_id)
        else:
            entry.delete(0, END)
            entry.insert(0, "User does not exist!")
    #handles key press events
    def key_pressed(event):
        current = entry.get()
        if current == "Enter your user id" or current == "User does not exist!":
            entry.delete(0, END)
            current = ""
        entry.delete(0, END)
        entry.insert(0,current + event.char)

    #handles left click events
    def left_click(s):
        if starter1.start == 0:
            current = entry.get()
            if current == "Enter your user id" or current == "User does not exist!":
                entry.delete(0, END)

    #handles repeat entries
    def repeat_key(event):
        current = entry.get()
        if current == "Enter your user id" or current == "User does not exist!":
            entry.delete(0, END)

        
    #creating login page
    heading = Label(root, text="KGPbook",font = ("sans-seriff", 50), fg = "#ffffff", bg = "#383636")
    entry = Entry(root, width = 30, borderwidth = 1, font = ("sans-seriff", 15), bg = "#020202", fg = "white")
    entry.insert(0, "Enter your user id")
    root.bind('<Button 1>', left_click)
    root.bind("<Key>", key_pressed)
    root.bind("<Key>", repeat_key)
    button_login = Button(root, text="login", padx= 40, pady=20, command= lambda: login_click(), bg = "#383636", fg = "white")

    heading.place(relx=0.37, rely=0.2)
    entry.place(relx=0.35, rely=0.5)
    button_login.place(relx=0.45, rely=0.7)
    
    return


login_page()
root.mainloop()



