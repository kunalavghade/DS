from tkinter import *

COLOR="#FFE7E4"
class gui():
	def __init__(self):
		self.window=Tk()
		self.window.title("My Order")
		self.window.geometry("360x620+270+60")
		self.window.wm_overrideredirect(True)
		self.window.resizable(False,False)
		self.starting()
		self.window.mainloop()

	def starting(self):
		self.IconVIIT = PhotoImage(file = "asset/Food.png")
		self.iconFrame = Frame(self.window,bg=COLOR)
		self.Icon = Label(self.iconFrame,image = self.IconVIIT,bg=COLOR)
		self.Icon.place(relheight=1,relwidth=1)
		self.iconFrame.place(relheight=1,relwidth=1)
		self.iconFrame.after(3000,self.deleteFrame)

	def deleteFrame(self):
		self.window.wm_overrideredirect(False)
		self.iconFrame.destroy()


if __name__=="__main__":
	gui()