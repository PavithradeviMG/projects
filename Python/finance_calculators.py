#program  for  a finanace_calculator
#Define the variable for calculation
#get the input
import math #use mathematical calculation
print("investment:To calaculate the amount of interest you will earn on your investment")
print("bond:To calculate the amount you will have to pay on your Home loan")
variable = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))
if variable.lower() == 'investment':
    interest_rate = int(input("Enter the interest rate: "))#integer input
    r = float(interest_rate/100)
    p = float(input("Deposit amount: "))
    t = int(input("Number of years: "))
    interest = str(input("Enter the interst is 'simple_interest' or 'compound_interest': "))
    if interest == 'simple_interest':
        A = p* (1 + r*t)#calculate the simple interest
        print(A)
    else:
        A = p* math.pow(1 + r,t) #calculate the compound interest
        print(A)
if variable.lower() == 'bond':
    p = float(input("Present value of the house: "))
    n = int (input( "Number of months the bond repaid: "))
    interest = int(input("Enter the interest: "))
    interest_rate = float(interest/100)
    i =float(interest_rate/12)#monthly_interest_rate
    repayment = (i * p)/ (1 - (1 + i)** (-n))
    print(repayment)
                        
