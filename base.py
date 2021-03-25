from tkinter import *
from tkinter import ttk

COLOR="#FFE7E4"
BUTTON="#FF7777"
class gui():
	def __init__(self):
		self.Win=Tk()
		self.Win.title("My Order")
		self.Win.geometry("390x620+270+60")
		self.Win.wm_overrideredirect(True)
		self.Win.resizable(False,False)
		self.starting()
		self.Win.mainloop()

	def starting(self):
		self.IconVIIT = PhotoImage(file = "asset/Food.png")
		self.iconFrame = Frame(self.Win,bg=COLOR)
		self.Icon = Label(self.iconFrame,image = self.IconVIIT,bg=COLOR)
		self.Icon.place(relheight=1,relwidth=1)
		self.iconFrame.place(relheight=1,relwidth=1)
		self.iconFrame.after(3000,self.deleteFrame)

	def deleteFrame(self):
		self.Win.wm_overrideredirect(False)
		self.iconFrame.destroy()
		self.mainWin()


	def mainWin(self):
		try:
			self.startframe.destroy()
		except :
			pass
		self.startframe=Frame(self.Win,bg=COLOR)
		showText=Label(self.startframe, text ="Are You Hungry !",font="arial 17 bold",bg=COLOR,)
		showText.place(relheight=0.12,relwidth=0.7,relx=0.15,rely=0.1)

		dinner=Button(self.startframe,text="dinner",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command=self.dinner)
		dinner.place(relheight=0.1,relwidth=0.44,relx=0.03,rely=0.3)

		Lunch=Button(self.startframe,text="Lunch",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command=self.lunch)
		Lunch.place(relheight=0.1,relwidth=0.44,relx=0.53,rely=0.3)

		Breakfast=Button(self.startframe,text="Breakfast",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command=self.Breakfast)
		Breakfast.place(relheight=0.1,relwidth=0.44,relx=0.03,rely=0.43)

		FastFood=Button(self.startframe,text="Fast Food",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command=self.FastFood)
		FastFood.place(relheight=0.1,relwidth=0.44,relx=0.53,rely=0.43)

		foodbasket=Button(self.startframe,text="Basket",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command=self.FastFood)
		foodbasket.place(relheight=0.1,relwidth=0.3,relx=0.35,rely=0.85)
		self.startframe.place(relheight=1,relwidth=1)

	def lunch(self):
		self.orderfood("Lunch")

	def FastFood(self):
		self.orderfood("FastFood")

	def Breakfast(self):
		self.orderfood("Breakfast")

	def dinner(self):
		self.orderfood("dinner")

	def orderfood(self,name):
		self.startframe.destroy()
		self.startframe=Frame(self.Win,bg=COLOR)
		self.startframe.place(relheight=1,relwidth=1)

		label=Label(text=f"Looking for {name}",bg=COLOR,anchor="center",font="arial 20").place(relwidth=1,relheight=0.3)
		
		foodbasket=Button(self.startframe,text="Basket",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command=self.FastFood)
		foodbasket.place(relheight=0.1,relwidth=0.3,relx=0.35,rely=0.85)
		
		self.orderframe=Frame(self.startframe,bg=COLOR)
		self.orderframe.place(relwidth=1,relheight=0.5,rely=0.3)
		my_canvas =  Canvas(self.orderframe,bg=COLOR)
		my_canvas.pack(fill=BOTH,expand=1,side=LEFT)
		my_Scroll = ttk.Scrollbar(self.orderframe,orient=VERTICAL,command = my_canvas.yview,)
		my_Scroll.pack(side= RIGHT,fill=Y)
		my_canvas.configure(yscrollcommand=my_Scroll.set)
		my_canvas.bind('<Configure>', lambda e : my_canvas.configure(scrollregion = my_canvas.bbox("all")))
		secondFrame = Frame(my_canvas)
		my_canvas.create_window((0,0),window = secondFrame ,anchor="nw")	

		for i in range(1,20):
			rup=Button(secondFrame,text=i,height=2,width=7,bg=COLOR,activebackground=COLOR,borderwidth=0,font="arial 15 bold",).grid(row=i,column=0)
			name=Button(secondFrame,text="pizza",height=2,width=25,command = self.mainWin,bg=COLOR,activebackground=COLOR,borderwidth=0,font="arial 15 bold",).grid(row=i,column=1)


if __name__=="__main__":
	gui()