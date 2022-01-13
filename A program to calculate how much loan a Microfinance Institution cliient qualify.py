
print("THE FOLLOWING INFORMATION SHOULD BE ENTERED BY THE CLIENT")
name =input("Please eneter your name:")
gross_salary=int(input("How much is your gross salary($):"))
net_salary=int(input("How much is your net salary($):"))
repay_loan=int(input("how many months do you need to repay loan (3,6,or 12):"))
while repay_loan!=3 and repay_loan!=6 and repay_loan!=12:  #Make sure the user enters correct number
    repay_loan=int(input("HOOps! the replay loan should be 3 ,6 or 12\nPlease enter repay loan again:"))

print("THE FOLLOWING INFORMATION SHOULD BE ENTERED BY THE TELLER")
interest_rate=int(input("Enter the current effective Rate(%):"))

if net_salary<(1/2)*gross_salary:
    print("The client do not qualify for automatic loan, please refer the client to the credit officer")
else:
    if repay_loan ==3:
        loan_amount=gross_salary
    elif repay_loan ==6:
        loan_amount=3*net_salary
    elif repay_loan ==12:
        loan_amount=6*net_salary
        

print("        \n\n\nMFI LOAN APPLICATION PRINTOUT")  #print out mfi application
print("Loan report for:",name)
print("Approved loan amount:",loan_amount)

opening=loan_amount # To store the opening balance. Therefore for the first month the opening is loan amount
print("MONTH     INTEREST      REPAYMENT      PAYMENT     BALANCE")
for i in range(repay_loan):
    month=i+1 #To store the current month
    repayment=gross_salary-net_salary#To store the repayment for the current month
    balance=opening-repayment #To store the balance for the current month.
    interest=(interest_rate/100)*(opening/(repay_loan*2))     #To store interest for the current month
    payment=repayment+interest #To store the payment for the current  month.
    print(month,"       $","{:.2f}".format(interest),"        $","{:.2f}".format(repayment),"     $","{:.2f}".format(payment),"       $","{:.2f}".format(balance));
         #balance =opening-repayment***if month =1 then opening=loan_amount else opening=previous month amount-repayment
         #payment=repayment+interest
        
    opening=balance;


