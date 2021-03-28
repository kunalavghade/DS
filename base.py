from tkinter import *
from tkinter import ttk
import connectToDB as c
import linklist 

COLOR="#FFE7E4"
BUTTON="#FF7777"

class gui():
	def __init__(self):
		self.Win=Tk()
		self.Win.title("My Order")
		self.Win.geometry("390x620+270+60")
		self.Win.wm_overrideredirect(True)
		self.Win.resizable(False,False)
		self.db = c.DataBase()
		self.l = linklist.LinkedList()
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

		foodbasket=Button(self.startframe,text="Basket",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command=self.Basket_func)
		foodbasket.place(relheight=0.1,relwidth=0.3,relx=0.35,rely=0.85)
		self.startframe.place(relheight=1,relwidth=1)

	def lunch(self):
		data_list = self.db.get_data("Lunch")
		self.orderfood("Lunch",data_list)

	def FastFood(self):
		data_list = self.db.get_data("Fast food")
		self.orderfood("FastFood",data_list)

	def Breakfast(self):
		data_list = self.db.get_data("Breakfast")
		self.orderfood("Breakfast",data_list)

	def dinner(self):
		data_list = self.db.get_data("dinner")
		self.orderfood("dinner",data_list)

	def Basket_func(self):
		price=self.total_price()
		self.BasketWin(self.l.get_list(),price)

	def remove(self,key):
		self.l.remove(key)
		price=self.total_price()
		self.BasketWin(self.l.get_list(),price)

	def total_price(self):
		price=0
		for i in self.l.get_list():
			price=price + i[0]
			print(i[0])
		return price

	def BasketWin(self,data,price):
		self.startframe.destroy()
		self.startframe=Frame(self.Win,bg=COLOR)
		self.startframe.place(relheight=1,relwidth=1)

		label1=Label(text="Your Oreders",bg=COLOR,anchor="s",font="arial 20 bold").place(relwidth=1,relheight=0.2)
		label2=Label(text=f"${price}",bg=COLOR,anchor="center",font="arial 20").place(relwidth=1,relheight=0.1,rely=0.2)
		
		Order=Button(self.startframe,text="Order",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command = self.Order_func)
		Order.place(relheight=0.1,relwidth=0.3,relx=0.15,rely=0.85)

		Back=Button(self.startframe,text="Back",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command = self.mainWin)
		Back.place(relheight=0.1,relwidth=0.3,relx=0.55,rely=0.85)
		
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

		i=0
		for j in data:

			rup=Button(secondFrame,text=j[0],height=2,width=7,bg=COLOR,activebackground=COLOR,borderwidth=0,font="arial 15 bold",command= lambda x=j[1] : self.remove(x)).grid(row=i,column=0)
			
			name=Button(secondFrame,text=j[1],height=2,width=25,bg=COLOR,activebackground=COLOR,borderwidth=0,font="arial 15 bold",command= lambda x=j[1] : self.remove(x)).grid(row=i,column=1)
			i+=1

	def orderfood(self,name,data):
		self.startframe.destroy()
		self.startframe=Frame(self.Win,bg=COLOR)
		self.startframe.place(relheight=1,relwidth=1)

		label=Label(text=f"Looking for {name}",bg=COLOR,anchor="center",font="arial 20").place(relwidth=1,relheight=0.3)
		
		foodbasket=Button(self.startframe,text="Basket",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command = self.Basket_func)
		foodbasket.place(relheight=0.1,relwidth=0.3,relx=0.15,rely=0.85)

		Back=Button(self.startframe,text="Back",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command = self.mainWin)
		Back.place(relheight=0.1,relwidth=0.3,relx=0.55,rely=0.85)

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

		i=0
		for j in data:

			rup=Button(secondFrame,text=j[0],height=2,width=7,bg=COLOR,activebackground=COLOR,borderwidth=0,font="arial 15 bold",command= lambda x=int(j[0]),y=j[1] : self.add_to_basket(x,y)).grid(row=i,column=0)
			
			name=Button(secondFrame,text=j[1],height=2,width=25,bg=COLOR,activebackground=COLOR,borderwidth=0,font="arial 15 bold",command= lambda x=int(j[0]),y=j[1] : self.add_to_basket(x,y)).grid(row=i,column=1)
			i+=1
	
	def add_to_basket(self,x,y):
		self.l.createNode(x,y)
		print(self.l.get_list())

	def Order_func(self):
		self.startframe.destroy()
		self.startframe=Frame(self.Win,bg=COLOR)
		self.startframe.place(relheight=1,relwidth=1)
		label=Label(text="Thanks for Ordering !",bg=COLOR,anchor="center",font="arial 20").place(relwidth=1,relheight=0.85)
		Back=Button(self.startframe,text="Back",bg=BUTTON,activebackground=BUTTON,borderwidth=0,font="arial 15 bold",activeforeground="#fff",command = self.mainWin)
		Back.place(relheight=0.1,relwidth=0.3,relx=0.35,rely=0.85)

if __name__=="__main__":
	gui()