#Button F number remote

from  tkinter import *

root = Tk()
root.geometry('180x400+1000+20')
root.title('Remote control')

show = StringVar()
show.set('ส่วนแสดงผลเริ่มต้น \nส่วนแสดงผลเริ่มต้น \nส่วนแสดงผลเริ่มต้น ')



#---*** function source ***--
def YT():
	show.set('open YouTube\nHS4QWC')
	print('open YouTube HS4QWC')

def SOURCE():
	show.set("open SOURCE")
	print('open source')

def NF():
	show.set('open NETFLIX')
	print('open NETFLIX')

def FB():
	show.set('open Facebook')
	print('open Facebook')




#---*** function ***---
def LISTS():
	show.set('Button List')
	print("Button List")
def ADD():
	show.set("Button ADD")
	print('Button ADD')




#---*** function button 0-9 ***---
def Number1():
	print('BUTTON-1')
	show.set('BUTTON-1')

def Number2():
	print('BUTTON-2')	
	show.set('BUTTON-2')

def Number3():
	print('BUTTON-3')
	show.set('BUTTON-3')

def Number4():
	print('BUTTON-4')
	show.set('BUTTON-4')

def Number5():
	print('BUTTON-5')
	show.set('BUTTON-5')

def Number6():
	print('BUTTON-6')
	show.set('BUTTON-6')	

def Number7():
	print('BUTTON-7')
	show.set('BUTTON-7')

def Number8():
	print('BUTTON-8')
	show.set('BUTTON-8')

def Number9():
	print('BUTTON-9')
	show.set('BUTTON-9')

def Number0():
	print('BUTTON-0')
	show.set('BUTTON-0')	




# ---***  ส่วนแสดงผล *** ---
L1 = Label(root, textvariable=show,
				font=('YouTube Sans', 10),
				bg='#e5dece',
				fg='black',
			 	borderwidth=2,
		  		relief='groove',
			  	width=26, # width
			   	height=5) # height
L1.place(x=10, y=35)
#--------------------------------#

# FRAME ***
F2 =Frame(root)
F2.place(x=5, y=120)

F1 = Frame(root)
F1.place(x=5, y=200)



#*********************
POWER = Button(root, text='ON', bg='red')
POWER.place(x=10,y=2)

MUTE = Button(root,text='MUTE')
MUTE.place(x=130,y=2)


#*********  ปุ่มตัวเลข FRAME-1 **********
b1 = Button(F1, text='1', bg='gray', fg='white', command=Number1).grid(ipadx=10, ipady=5, padx=5,pady=5,row=0, column=0)
b2 = Button(F1, text='2', bg='gray', fg='white', command=Number2).grid(ipadx=10, ipady=5, padx=5,pady=5,row=0, column=1)
b3 = Button(F1, text='3', bg='gray', fg='white', command=Number3).grid(ipadx=10, ipady=5, padx=5,pady=5,row=0, column=2)

b4 = Button(F1, text='4', bg='gray', fg='white', command=Number4).grid(ipadx=10, ipady=5, padx=5,pady=5,row=1, column=0)
b5 = Button(F1, text='5', bg='gray', fg='white', command=Number5).grid(ipadx=10, ipady=5, padx=5,pady=5,row=1, column=1)
b6 = Button(F1, text='6', bg='gray', fg='white', command=Number6).grid(ipadx=10, ipady=5, padx=5,pady=5,row=1, column=2)

b7 = Button(F1, text='7', bg='gray',fg='white', command=Number7).grid(ipadx=10, ipady=5, padx=5,pady=5,row=2, column=0)
b8 = Button(F1, text='8', bg='gray',fg='white', command=Number8).grid(ipadx=10, ipady=5, padx=5,pady=5,row=2, column=1)
b9 = Button(F1, text='9', bg='gray', fg='white', command=Number9).grid(ipadx=10, ipady=5, padx=5,pady=5,row=2, column=2)
b0 = Button(F1, text='0', bg='gray', fg='white', command=Number0).grid(ipadx=10, ipady=5, padx=5,pady=5,row=3, column=0)

b_list = Button(F1, text='LIST',bg='orange',fg='gray', command=LISTS)
b_list.grid(ipadx=10, ipady=5, padx=5,pady=5,row=3, column=1)
b_AD = Button(F1, text='AD', bg='gray', fg='white', command=ADD)
b_AD.grid(ipadx=10, ipady=5, padx=5,pady=5,row=3, column=2)

#---***  BUTTON FRAME 2 *****---
b_youtube = Button(F2, text='YouTube',font=('YouTube Sans', 12), fg='white', bg='red', command=YT)#font=YouTube Sans
b_youtube.grid(row=0, column=0)

b_SOURCE = Button(F2, text='SOURCE', font=('YouTube Sans', 12), bg='green', fg='white', command=SOURCE)
b_SOURCE.grid(row=0, column=1,ipadx=15)

b_NETFLIX = Button(F2, text='NETFLIX', font=('Bebas Neue', 12) ,fg='red', bg='white', padx=10, command=NF)
b_NETFLIX.grid(row=1,column=0)

b_FB = Button(F2, text='Facebook', font=('Facebook Letter Faces', 11) ,fg='blue', bg='white', padx=10, command=FB)
b_FB.grid(row=1,column=1, padx=3, )

root.mainloop()