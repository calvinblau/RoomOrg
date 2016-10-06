from room import *
from user import *
import math

def import_user(filename):
    with open(filename) as csv:
        user = csv.readlines()

    users = {}
    for i in range(0, len(user)):
        data = user[i].split(";")
        users["user" + str(i)] = User(data[1], data[0], data[2], data[3], data[4], data[5])

    return users

    
            
def main():
    print("Hello world")
    users = import_user("personen.csv")
    print(users['user0'].name)
    print(users['user1'].name)

#if "__main__" == __main__:
main()
