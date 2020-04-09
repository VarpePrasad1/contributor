from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

root=Tk()
root.title("-CONTRIBUTOR-")
root.geometry("500x500")
root['bg']='#6AC5FE'
dic={}  #empty dictionary
list1=[]
global i
no=StringVar()
who=StringVar()


def check():
	if len(who.get())==0:
		messagebox.showerror("Pop_up Message","Enter Valid Name")
		root.quit()   

def show_error():
	messagebox.showerror("ERROR","Invalid Input")
	root.quit()

def get_value(val):
   	for key, value in dic.items():
   		if val == value:
   			return key

def show_pop_up():
	global s2
	s2=messagebox.askyesno("Pop_up"," "+ name.upper()+" Paid for all?")
	#print(s2)      #s2->Paid For all or not
	calc()

def calc():
	if s2 == True :
		key=dic[name]
		print(key)
		amount=int(value)/content
		for i in range(0,content):
			arr[key][i]=arr[key][i]+amount
		#who_paid()
		print(arr)
		solve()
	else:
		list1=[]
		print("Enter number of friends:")
		s4=simpledialog.askinteger("Pop_up Message","For how many people "+name.upper()+" paid?")
		#btn=Button(root,text="Done!").place(x=280,y=160)
		if(s4<=content):
			for i in range(s4):
				print("Enter The Name Of Friends:")
				s3=simpledialog.askstring("input string","Enter Name Of Peoples For "+name.upper()+" paid money")
				#name1=input()
				list1.append(s3)
		else:
			show_error()
		amount=value
		amount=int(amount)/s4
		key=dic[name]
		for j in range(s4):
			arr[key][dic[list1[j]]]+=amount
		solve()

def print_content(i):
	global s
	s=simpledialog.askstring("input string","Enter Your Name")
	if len(s)==0:
		show_error()
	store(i)          

def store(i):
	x=s
	print(x)
	list1.append(x)
	dic[x]=i

def printdic():
	print(dic)
	print(list1)
	x=no.get()
	who_paid()

def who_paid():
	global who
	label2=Label(root,text="Who paid the money?",bg='#6AC5FE')
	label2.place(x=10,y=170)
	label2.config(font=labelfont)
	entry2=Entry(root,width=30,textvariable=who).place(x=200,y=170)
	who.set("-")
	button=Button(root,text="Done!",command=print_who,bd=4).place(x=425,y=170)
	button4=Button(root,text="Show contro",command=statement,bd=4,width=10).place(x=250,y=205)

def print_who():
	global name
	check()
	name=who.get()           #name->Who paid money
	print(name.upper()+ " paid the money")
	print_how()

def print_how():
	global value
	s1=simpledialog.askinteger("input string","Enter The Amount")
	value=s1               #value->Amount
	if value==0:
		messagebox.showerror("Warning","Invalid Input")
		print_how()
	print(value)
	show_pop_up()

def call_function():
	global arr,content
	content=value.get()      #content-> number of friends
	arr=[[0 for i in range(content)]for j in range(content)]
	print(arr)
	print(content)   #print number of friends
	if content==0:
		show_error()
	for i in range(content):    
	    print_content(i)    #print names
	button1=Button(root,text="Proceed To Contro!",command=printdic,bd=4)
	button1.grid(column=1,padx=30)
	button1.place(x=235,y=120) 

def solve():
	for i in range(content):
   		for j in range(content):
   			if(i!=j):
   				if(arr[i][j]!=0 and arr[j][i]!=0):
   					if(arr[i][j]>arr[j][i]):
   						arr[i][j]=arr[i][j]-arr[j][i]
   						arr[j][i]=0
   					else:
   						arr[j][i]=arr[j][i]-arr[i][j]
   						arr[i][j]=0
	for i in range(content):
		for j in range(content):
			print(arr[i][j], end='\t')
		print()

def statement():
	global size
	size=IntVar
	size=270
	for i in range(content):
		for j in range(content):
			if(i>j):
				if(arr[i][j]>0):                       
					label=Label(root,text=get_value(j).upper()+" Should give money to "+get_value(i).upper()+" ->")
					label.place(x=70,y=size)
					label.config(font=labelfont)
					label=Label(root,text=round(arr[i][j],2))
					label.place(x=340,y=size)
					label.config(font=labelfont)
					size+=20
					print(get_value(j).upper()+" Should give money to "+get_value(i).upper(),end='->')
					print(arr[i][j])
				else:
					label=Label(root,text=get_value(i).upper()+" Should give money to "+get_value(j).upper()+" ->")
					label.place(x=70,y=size)
					label.config(font=labelfont)
					label=Label(root,text=round(arr[j][i],2))
					label.place(x=340,y=size)
					label.config(font=labelfont)
					size+=20
					print(get_value(i).upper()+" Should give money to "+get_value(j).upper(),end='->')
					print(arr[j][i])

global name,amount,value
name1=StringVar
name= StringVar
amount1=IntVar
amount=IntVar
value = IntVar()
heading=Label(root,text="Welcome to Contributor!!!",fg='#152238',bg='#6AC5FE')
heading.grid(row=0,column=0)
heading.place(x=20,y=10)
heading.config(font=('times', 30, 'bold'))
labelfont=('times',12,'bold')
label=Label(root,text="Enter number of friends:",bg='#6AC5FE')
label.grid(row=1,column=0,padx=10,pady=80)
label.config(font=labelfont)
entry=Entry(root,width=30,textvariable=value).grid(row=1,column=1,padx=10)
button=Button(root,text="Done!",command=call_function,bd=4).grid(row=1,column=2,padx=30)
value.set(2)
exit_button=Button(root,text="EXIT",command=root.quit,width=10).place(x=400,y=450)

root.mainloop()