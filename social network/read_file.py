import re

#This class deals with file handling for the program
class reader:
    #list of user ids
    users = list() 
    #ith
    #user 1, user2....
    #list of friends, oredered in accordance with users list
    users_friends = list() 
    #ith
    #fiends_user1, friends_user2
    #list of group ids
    groups = list()


    #list of group members, ordered in accordance with groups list
    groups_list = list()
    

    #defines a message with three parts, sender, reciever and content
    class message():
        sender = None    #1 -> 0
        reciever = list()
        content = None

    #list of messages
    message_data = list() #social..................mesaagese

    #this function reads the file social_network.txt and updates the lists of users, friends and groups
    def read_userdb(self):
        fhand = open('social_network.txt')
        count = 0
        for line in fhand:
            if count == 0:
                # # users
                count += 1
                continue
            elif count == 1:
                # #groups
                if line.strip() == '#groups':
                    count += 1
                    continue
                else:
                    # <user_id: friend1, friend2, friend3>
                    new_user = re.findall('^<([^:]+)', line.strip())   # [^a]+   bbihijevieja
                    self.users.append(new_user[0])
                    friends_list = re.findall('\s([^,>]+)', line.strip())
                    self.users_friends.append(friends_list)
            else:
                # <group_id: user1, user2, user3>
                new_group = re.findall('^<([^:]+)', line.strip())
                self.groups.append(new_group[0])
                member_list = re.findall('\s([^,>]+)', line.strip())
                self.groups_list.append(member_list)

    #this function reads the filemessages.txt file and updates the list message_data
    def read_messagedb(self):
        self.message_data = list()
        fhand = open('filemessages.txt')
        # <sender_id: group_id or 0>
        user_num = None
        count = 0
        for line in fhand:
            if count == 0:
                data = self.message()
                new_sender = re.findall('^<([^:]+)', line.strip())
                data.sender = new_sender[0]
                recepients = re.findall('\s([^,>]+)', line.strip())
                for i in range(len(self.users)):
                    if data.sender == self.users[i]:
                        user_num = i
                        break
                for i in recepients:
                    if i == '0':
                        data.reciever = data.reciever + self.users_friends[user_num]
                    else:
                        for j in range(len(self.groups)):
                            if i == self.groups[j]:
                                data.reciever = data.reciever + self.groups_list[j]
                count = 1
            else:
                data.content = line.strip()
                count = 0
                self.message_data.append(data)

    #this function takes message parameters and writes into file filemessages.txt
    def addMessage(self, message, sender, reciever):
        fhand = open('filemessages.txt', "a+")
        fhand.write("<"+ sender + ": " + reciever + ">\n")
        fhand.write(message + "\n")
        fhand.close()

        
                


#for testing, ignore
if __name__ == '__main__':
    dos = reader()
    dos.read_userdb()
    dos.read_messagedb()
    for i in dos.message_data:
        print(i.content)
    
