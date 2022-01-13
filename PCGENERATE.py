import random
import collections
def menu():
	print ("Would u prefer to print the number your self or the computer will generatie for u\n1.me\n2.computer")
	a=int(input("Response: "))	
	if a==1:
		print("Please sorry this feature is not available")
		menu()
	elif a==2:
		PcGenerate()	
	else:
	   print("invalid answer, try again\n")
	   menu ()    
def PcGenerate():
	randomlist=random.sample(range(0,9),5)	

	envelopelist=[3,4,5,8,9]
	randomlist.sort()
	envelopelist.sort()
	print(randomlist)
	print(envelopelist)
	
	if randomlist==envelopelist:
		print("You won a gold price")
	else:
		print("You lost, please try again\n ")
		menu()
menu()
