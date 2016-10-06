
#		   Date: 06.10.2016
#Author of file: Maximus

class Room():
	def __init__(self, room_number = None, room_name = None, room_available = None, room_size = None):

		if room_number is None and room_name is None and room_available is None and room_size is None:
			self.room_number = 0;
			self.room_name = "Empty Room"
			self.room_available = True
			self.room_size = -1

		else:
			self.room_number = room_number
			self.room_name = room_name
			self.room_available = room_available
			self.room_size = room_size		
		pass


	def __del__(self):
		pass

	def addUser(self, user = None):
		#branch if user is object or number
		
		if user is None:
			pass
		elif type(user) is str:
			pass

		pass

	
	def delUser(self, user = None):
		#branch if user is object or number

		if user is None:
			pass
		elif type(user) is str:
			pass

		pass





def main():
	pass

if __name__ == '__main__':
	main()