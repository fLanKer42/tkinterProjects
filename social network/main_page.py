from tkinter import *
from read_file import *

#this class creates the main window
class page:
    #reader.users[current_page] = user_id
    current_page = 0
    user_id = None

    #this function takes TK() object and reader object as parameters to show the window in accordance to the data
    def create_page(self, root, file_data):
        
        #this function deals with clicking of dropdown menu on top right corner
        def drop_downmenu(event):
            drop_val = variable.get()
            if drop_val == self.user_id:
                pass
            else:
                for i in range(len(file_data.users)):
                    if drop_val == file_data.users[i]:
                        self.current_page = i
                        break
                self.create_page(root, file_data)

        #this function deals with clickig of refresh button on top left corner
        def refresh_data():
            file_data.read_messagedb()
            self.create_page(root, file_data)
            pass

        
        root.update()
        rootHeight = root.winfo_height()
        rootWidth = root.winfo_width()
        self.user_id = file_data.users[self.current_page]


        #title bar module
        ######################################################################################################################################
        variable = StringVar(root)
        variable.set(file_data.users[self.current_page])
        titlebar = Frame(root, width= rootWidth, height = rootHeight/10, bg= '#383630')
        refresh_button = Button(titlebar, text="Refresh", fg = "white", bg = "#020202", command= lambda: refresh_data())
        title_label = Label(titlebar, text="KGPbook", fg="white",font = ("sans-seriff", 15), bg = '#383636')
        menu_button = OptionMenu(titlebar, variable, *file_data.users, command = drop_downmenu)
        menu_button.configure(bg = "#020202", fg="white")
        titlebar.place(relx=0,rely=0)
        refresh_button.place(relx=0.02, rely=0.15)
        title_label.place(relx=0.45, rely=0.15)
        menu_button.place(relx=0.90, rely=0.15)
        ######################################################################################################################################


        #message display module
        ######################################################################################################################################
        message_frame = Frame(root, width= rootWidth/2, height= 6*(rootHeight/10), bg= 'blue')
        display_list = list()
        for i in file_data.message_data:
            if self.user_id in i.reciever:
                display_list.append(i)
        k = 0.3
        message_bit = Label(message_frame, text = "Incoming Messages", fg = "white", bg = "#665757", font = ("sans-seriff", 15))
        message_bit.place(relx=0.05, rely=0.1)
        for i in display_list:
            message_bit = Label(message_frame, text = i.sender + '\n' + i.content, fg = "white", bg = "#665757", font = ("sans-seriff", 10))
            message_bit.place(relx=0.05, rely=k)
            k = k + 0.2
        message_frame.place(relx=0.25, rely=0.1)
        ######################################################################################################################################

        #group list diplay module
        ######################################################################################################################################
        groups_frame = Frame(root, width= rootWidth/4, height=9*(rootHeight/10), bg= 'yellow')
        group_list = list()
        k = 0
        for i in file_data.groups_list:
            if self.user_id in i:
                group_list.append(file_data.groups[k])
                k += 1
            else:
                k += 1
        group_bit = Label(groups_frame, text = "Groups", fg = "white", bg = "#665757", font = ("sans-seriff", 15))
        group_bit.place(relx = 0.05, rely = 0.1)
        k = 0.2
        for i in group_list:
            group_bit = Label(groups_frame, text = i, fg = "white", bg = "#665757", font = ("sans-seriff", 10))
            group_bit.place(relx = 0.05, rely = k)
            k += 0.1
        groups_frame.place(relx=0.75, rely=0.1)
        ######################################################################################################################################


        #contacts list display module
        ######################################################################################################################################
        contacts_frame = Frame(root, width= rootWidth/4, height = 9*(rootHeight/10), bg = 'orange')
        contact_list = file_data.users_friends[self.current_page]
        contact_bit = Label(contacts_frame, text = "Contacts", fg = "white", bg = "#665757", font = ("sans-seriff", 15))
        contact_bit.place(relx=0.05, rely=0.1)
        k = 0.2
        for i in contact_list:
            contact_bit = Label(contacts_frame, text = i, fg = "white", bg = "#665757", font = ("sans-seriff", 10))
            contact_bit.place(relx=0.05, rely=k)
            k += 0.1
        contacts_frame.place(relx = 0, rely=0.1)
        ######################################################################################################################################

        #this function deals with posting of messages
        def post_message(event):
            share_val = var.get()
            data_share = input_box.get()
            input_box.delete(0, END)
            if share_val == 'Share on my wall':
                file_data.addMessage(data_share, self.user_id, '0')
            else:
                file_data.addMessage(data_share, self.user_id, share_val)

        #post message module
        ######################################################################################################################################
        post_frame = Frame(root, width = rootWidth/2, height = 3*(rootHeight/10), bg = 'red')
        input_box = Entry(post_frame, width = 35, borderwidth = 1, font = ("sans-seriff", 15), bg = "#020202", fg = "white")
        input_box.place(relx = 0.1, rely = 0.1)
        var = StringVar(root)
        var.set("Share With")
        share_list = list()
        share_list.append('Share on my wall')
        share_list += group_list
        share_button = OptionMenu(post_frame, var , *share_list, command = post_message)
        share_button.configure(bg = "#020202", fg="white")
        share_button.place(relx=0.45, rely=0.5)
        post_frame.place(relx = 0.25, rely = 0.7)
        ######################################################################################################################################






#This part is required when run without index.py
if __name__ == "__main__":
    root = Tk()
    root.title("KGPbook")
    root.configure(background='#383636')
    root.geometry('1000x500')
    file_data = reader()
    file_data.read_userdb()
    file_data.read_messagedb()

    pager = page()
    pager.create_page(root, file_data)
    
    root.mainloop()
