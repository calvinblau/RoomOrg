
#		   Date: 06.10.2016
#Author of file: Maximus

class User():
	
	def __init__(self, user_surname, user_name, user_age, 
					user_mail, user_phone, user_address):
		self.surname = user_surname
		self.name = user_name
		self.age = user_age
		self.phone = user_phone
		self.address = user_address
		self.mail = user_mail
		pass

	def __del__(self):
		pass		


def main():
	pass

if __name__ == '__main__':
	main()