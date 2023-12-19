# Calculate the average by user input 
sum = 0
count = 0
 #intialize the variable
number = int(input("Enter a positive number,negative number to exit: " ))
while number >= 0:
    sum += number
    count += 1 
    number = int(input("Enter a positive number,negative number to exit: "))
if count > 0:
    print(f"Average is {sum /count} ")
    