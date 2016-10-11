#		   Date: 11.10.2016
#Author of file: Maximus
#this file is the model


class RoomOrgModel():
	
	def __init__(self):
		self.Users = []
		self.Rooms = []		
		pass

	#Just adding and removing features for the lists
	def addUserToList(self, user):
		self.Users.append(user)
		pass

	def removeUserFromList(self, user_id):
		self.Users.remove(user_id)
		pass

	def addRoomToList(self, room):
		self.Rooms.append(room)
		pass

	def removeRoomFromList(self, room_id):
		self.Rooms.remove(room_id)
		pass

	def __del__(self):
		pass

	def __str__(self):		
		pass
		
		



def main():
	backend = RoomOrgModel()	
	pass

if __name__ == '__main__':
	main()
