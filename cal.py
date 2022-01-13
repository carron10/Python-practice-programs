from driagrams import*


def add(a,b):
	print("Addition: ",a+b)
def sub(a,b):
	print("Subtraction: ",a-b)
def mult(a,b):
	print("Multiplication: ",a*b)
def devide(a,b):
	print("Devision",a/b)

def DoThings():
	print("\nWhat do you want me to do for you: ")
	Do()
	
def Do():
	print("\n1.Calculate area of triangle\n2.Calculate area of a circle\n3.Draw a trinagle\n4.Draw a circle\n5.Draw rectangle\n6.Draw square\n7.Conveter numbers\n8.Form a calculator\n8.Launch software on your machine\n9.Solve equation\n10.Do some calculation for u")
	ans=int(input("\n\nEnter response: "))
	if ans==1:
		triangle()
	elif ans==10:
		doit()
	
	elif ans==2:
		circle()
	elif ans==4:
		drawCircle()
	else:
		print("Your answer is out of range: ")
		DoThings()

def triangle():
	print("\n\nCalculating area of a triangle:\n ")
	b=int(input("\nEnter Base: "))
	h=int(input("Enter height: "))
	
	print("\nArea of triangle =",(b*h)*1/2)
	doElse()


def circle():
	print("\n\nCalculating area of a circle:\n ")
	b=int(input("Enter radius: "))
	
	print("\nArea of circle=",3.423*b)
	doElse()
	
def doit():
	a=int(input("\nEnter a number: "))
	b=int(input("Enter a number: \n"))
	add(a,b)
	sub(a,b)
	mult(a,b)
	devide(a,b)
	doElse()

def doElse():
	print("\nDo you want me to do something else for you:\n1.Yes\n2.No")
	a=int(input("Response: "))
	if a==1:
		DoThings()
	elif a==2:
		print("Ooops u am done!!!")
	else:
		print("Your answer is wrong")
		doElse()

