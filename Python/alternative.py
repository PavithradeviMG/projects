#initiate input variables
string = "DataScience"
alternate =""
# using for loop to convert alternative case into uppercase
for i,x in  enumerate(string):
    if (i%2 == 0):
       alternate += (string[i].upper())
    else:
      alternate += (string[i].lower())
print(alternate)

# intialise the input variable
sentence = "I am learning to code"
#convert a sentece to list
list = sentence.split()
print(list)
# using for loop to convert alternative case into uppercase
for i,x in enumerate(list):
    if (i%2 == 0):
       list[i] = (list[i].lower())
       #print(alternate_list[i]) 
    else:
      list[i] = (list[i].upper())
      #print(alternate_list[i] )
#join the list to a sentence
#print(alternate_list)
print((" ".join(list)))  