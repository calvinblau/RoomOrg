from room import Room
from user import User
import sys
import math

userlist = {}
roomlist = {}

####
# statt die räume und nutzer in variablen zu speichern, speichere ich sie hier
# in dicts ab, um direkt alle bisher erstellten/importierten räume u. nutzer
# aufrufen zu können - deswegen kann es chaotisch aussehen, aber das ist auch
# nur ein entwurf
####

def import_user(filename):
    if type(filename) is str:
        with open(filename, encoding="utf-8") as csv:
            user = csv.readlines()

        for i in range(0, len(user)):
            data = user[i].split(";")
            userlist["user" + str(i)] = User(data[0], data[1], data[2], 
                    data[3], data[4], data[5])

        return userlist
    else:
        pass

def export_user(filename):
    if type(filename) is str:
        csv = open(filename, 'w')
        for i in range(0, len(userlist)):
            csv.write(userlist['user' + str(i)].name+';'+
                    userlist['user' + str(i)].surname+';'+
                    userlist['user' + str(i)].age+';'+
                    userlist['user' + str(i)].mail+';'+
                    userlist['user' + str(i)].phone+';'+
                    userlist['user' + str(i)].address+';')
            csv.write('\n')
    else:
        pass

def new_user(name, surname, age, mail, phone, address):
    userlist["user" + str(len(userlist))] = User(name, surname, 
            age, mail, phone, address)

def new_room(number = None, name = None, available = None, size = None):
    if number is None and name is None and available is None and size is None:
        roomlist["room" + str(len(roomlist))] = Room()
    else:
        roomlist["room" + str(len(roomlist))] = Room(len(roomlist), name, 
                available, size)

    return roomlist

def alloc_room(room, user):
    if type(room) is Room and type(user) is User:
        room.user = user
        room.available = False
        user.room = room
    else:
        pass

def dealloc_room(room):
    if type(room) is Room and room.available is False:
        room.user.room = None
        room.user = None
        room.available = True 
    else:
        pass

def deassign_room(room):
    pass

def main():
    '''
    print("Hello world")
    users = import_user("personen.csv")
    new_room()
    new_room(21,'raum21',False,2)
    new_room()
    new_room()
    print(roomlist)
    print(roomlist['room1'].available)
    #print(userlist['user0'].name)
    #print(userlist['user1'].address)
    export_user("personen1.csv")    
    '''
    users = import_user("personen.csv")
    new_room(21,'raum21',True,2)
    alloc_room(roomlist['room0'], userlist['user1'])
    print(roomlist['room0'].user.name)
    new_user('hany', 'bal', '30', 'mail', 'phone', 'address')
    export_user("personen1.csv")    

if __name__ == "__main__":
    main()
