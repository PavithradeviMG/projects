# Design a program that determines the award  a person competing in a traithalon
# Declare the activities in traithalon.
#Calculate the time taken for swimming.
swimming = int( input("Enter the time taken for swimming in minutes:"))
print("Time taken for swimming task:" ,swimming)
#Calculate the time taken for cycling.
cycling = int(input("Enter the time taken for cycling in minutes: "))
print("Time taken for cycling: ",cycling)
#Calculate the time taken for running
running = int(input("Enter the time taken for running in minutes:"))
print("Time taken for running: ",running)
#Calculate the total time taken for Traithlon.
total_time_traithlon = (swimming + cycling + running)
print("Time to complete Traithalon : ",total_time_traithlon)
# Award the participant by  time taken for completing the triathlon.
if total_time_traithlon <= 100:
    print(" Provincial Colours!")
elif total_time_traithlon > 100 and total_time_traithlon <= 105:
    print("Provincial Half Colours!")
elif total_time_traithlon >= 106 and total_time_traithlon <= 110:
    print("Provincial Scroll!")
else:
    print("No Awards!")

