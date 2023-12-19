# Function to add two numbers
def add(x,y):
    return x + y
# Function to subtract two numbers
def subtract(x,y):
    return x - y
# Function to multiply two numbers
def multiply(x,y):
    return x * y
# Function to divide two numbers
# This prints message if the number is divide by zero
def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
       return "Division by zero\n"
# Create a file in write mod
answer = 0
file = open("output.txt", "a")
while True:
    # Read numbers and operator
    try:
        number1 = float(input("Enter first number: "))
        number2 = float (input("Enter second number: "))
    except ValueError:
        print("please enter the integer")
        continue
    operator = input(" Enter operator: ")
   # file.write(str(number1)+" "+operator+" "+str(number2)+"\n")
    # if else statment to print the answer for the given operator
    if operator in ("+", "-", "*", "/"):
        if operator == "+":
            answer = add(number1,number2)
        elif operator == "-":
           answer =  subtract(number1,number2)
        elif operator == "*":
            answer = multiply(number1,number2)
        elif operator == "/":
            answer = divide(number1,number2)
    else:
        print("please enter the operator" )
        continue
    file.write(str(answer)+"=" + str(number1)+" "+operator+" "+str(number2)+"\n")
    #Chose whether to continue or not
    choice = input("read from file Continue - Y / exit No - N: ")
    file.close()
    if choice == "N":
       break
    else:
        #open the file in read mode
        #read content of the file 
        try:
           file2 = open(input(" Enter the file name:"),"r")
           print(file2.read())
           file2.close()
        except IOError:
          print("file not exists")

else:
    print("Invalid Input\n")
# Close the file
file.close()   

