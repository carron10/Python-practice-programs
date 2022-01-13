#Hy this program is to accept Scores from the user in%.. meaning the must be >=0 but <=100
#So The output of the program is not only the CPGA but The full statement of the students passes
#Then it will also Give the value(CPGA) on its own
#Let me explain all the steps ..Please note that not all the variables have meaningful names..Because i was to be fast.


#below are the firs statements given to the user
print("CPGA CALCULATION")
print("Please Enter your scores")

#listing all courses
courses=("GNS 101","GNS 102","COM 213","COM 214","COM 315","STAT 355","MTH 213",
"STAT 415")

#delaring all values as list
#i gave names variables below as the main variables of the program

#scores are pass of student in %
scores=[]
a=0

#these are credits as they are in the qtn
credits=[2,2,3,4,4,3,3,3]

#these are points, I declared them as zeros so that they will be upgraded later

pValue=[0,0,0,0,0,0,0,0]

#grades are the student grade in poi t form

grades=[0,0,0,0,0,0,0,0]

#symbols are symbols they depends on the student scores
symbols=[0,0,0,0,0,0,0,0]

#cgpa is zero coz it will be updated later
cgpa=0

#total points and credits
totalpoints=0
totalcredits=0
t=0

#the below loop is asking a for scores is in %form in all from all 8 courses

for n in range(7):
		a=int(input(courses[n]+": "))
		scores.append(a)#adding the values to the scores list
		

#this functiom will check if the scores are valid or not
#if they are not valid the course with invalid score need to be updated
#it returns scores  only after every invalid value have been solved
def check(scores):
				c=0
				for n in scores:
					if n>100 or n<0:
						c=scores.index(n)
						print("course",courses[c]," with score ",n," is invalid please enter the score again")
						scores[c]=int(input(courses[c]+": "))
						check(scores)
				
				return scores				

#function cal() accept point values as parameter and return the list with updated values this also update symbols because symbols go hand in hand with points
def cal(pValues):
	score=check(scores)

	for i in range(7):
			if scores[i]>=90:
					pValue[i]=4
					symbols[i]='A'
			if scores[i]>=80 and scores[i]<90:
				    pValue[i]=3.5
				    symbols[i]='B'
			if scores[i]>=70 and scores[i]<80:
					pValue[i]=3
					symbols[i]='C'
			if scores[i]<70:
					pValue[i]=2.5
					symbols[i]='U'
	return  pValues	  
			
	#the go() function I just gave it this name! kkk,    It accept cpga which is zero and return it after calculation..
	#this is the function also which provide the argument to the cal function
	
def go(c):
	#this one it calculate the CGPA
	
	global totalpoints
	global totalcredits
	
	values=cal(pValue)
	global cgpa
	
	for i in pValue:
		totalpoints+=i	
	
	for t in credits:
		totalcredits+=t
	
	cgpa=totalpoints/totalcredits
	return cgpa,values

#This is the main function to me Because everythin starts here...See then.This functions call the go() function and the go() function calls the cal() function ..the cal() function will lastly call the check function..
#At the end all the Information are being posted to the results function, which is The one to display everything.
#Doneee..


def results():
	p=go(cgpa)
	h=p[1]
	heading=("course   ","score  ","symbol ","points ")
	print(heading)
	v=[]
	results={}
	for i in range(7):
		v=[scores[i],symbols[i],h[i]]
		results={courses[i]:v}
		print(results)

	
	print("Your finally CGPA is",p[0])
	return
#Whenever we develop a python u know right where do we start..It starts in by calling one or more functions and the code to do this is always at the bottom like the one below here..It calls the results function which the main method to me

results()