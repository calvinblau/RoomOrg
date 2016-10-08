#Date: 06.10.2016
#Author of file: Maximus

class User():

    def __init__(self, user_name, user_surname, user_age, user_mail, user_phone, user_address):
        self.name = user_name
        self.surname = user_surname
        self.age = user_age
        self.mail = user_mail
        self.phone = user_phone
        self.address = user_address
        self.room = None
        pass

    def __del__(self):
        pass		



def main():
    pass

if __name__ == '__main__':
    main()
