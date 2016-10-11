import tkinter as tk

#		   Date: 06.10.2016
#Author of file: Maximus
#this file is for gui purposes, for testing

class RoomOrgView(tk.Frame):
	
	def __init__(self, master=None):
		super().__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Hello World"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side = "top")

		self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
		self.QUIT.pack(side = "bottom")

	def say_hi(self):
		print("hi there")


def main():
	#root = tk.Tk()
	#view = RoomOrgView(master=root)
	#view.mainloop()

	window = tk.Tk()	
	window.mainloop()
	#window.geometry("100x100")
	pass
	

if __name__ == '__main__':
	main()