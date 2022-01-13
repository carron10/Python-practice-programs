
# A program to calculate BMI
#To calculate bmi we first ask the user for height and weight, then calculate the bmi and lastly display the output.
#These step have been established at the end of all these code. Pliz read at the bottom
#Step 1. get height and weight from the user
#step 2. calculate bmi
#step 3. display



#A function to Ask user  for height
def get_height():
    height=int(input("Enter height:"))
    while height<=0:
        height=int(input("Height must be more than zero,Enter height again:"))
    return height

#ask user for weight
def get_weight():
    weight=int(input("Enter weight:"))
    while weight<=0:
        weight=int(input("weight must be more than zero,Enter height again:"))
    return weight


#A function to calculate bmi
def calculate_bmi(height,weight):
    return weight/((height)**2)


#function to display the output
def display(bmi):
    print("BMI =",bmi)
    if bmi<18.5:
        print("Underweight")
    elif bmi<=24.9:
        print("Normal")
    elif bmi<=29.9:
        print("Overweight")
    elif bmi>=30:
        print("Obese")
    return



#The step which have been explained above below are they
height=get_height()  #code for step 1
weight=get_weight() #still step 1.
bmi=calculate_bmi(height,weight)    #step 2
display(bmi)                    #step 3.
