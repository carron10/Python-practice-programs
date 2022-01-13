def myGuess():
     print("Enter five numbers: ")
     a=int(input ("1st: "))
     b=int(input ("2nd: "))
     c=int(input ("3rd: "))
     d=int(input ("4th: "))
     e=int(input ("5th: "))
     numbers=[a,b,c,d,e]
     envelopelist=[3,4,5,8,9]
 	numbers.sort()
     correct.sort()
     
 	if numbers==correct:
    		print("You won the price")
 	else:
    	 print("You are wrong\nPlease try again")
    	 menu()