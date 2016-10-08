from user import *

#Date: 06.10.2016
#Author of file: Maximus

class Room():
    def __init__(self, room_number = None, room_name = None, room_available = None, room_size = None):
        if room_number is None and room_name is None and room_available is None and room_size is None:
            self.number = 0;
            self.name = "Empty Room"
            self.available = True
            self.size = -1
            self.user = None

        else:
            self.number = room_number
            self.name = room_name
            self.available = room_available
            self.size = room_size
            self.user = None
        pass


    def __del__(self):
        pass

'''
    def addUser(self, user = None):
        #branch if user is object or number
        if user is None:
            pass
        elif type(user) is User:
            self.user = user
            self.available = False
            user.room = self

    
    def delUser(self):
        self.user.room = None
        self.user = None
        self.available = True
'''

def main():
    pass

if __name__ == '__main__':
    main()
