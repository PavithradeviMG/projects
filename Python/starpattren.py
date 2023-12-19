##Define the funtion triangle and get the input n
#input("number of star in a traingle n = ")
def triangle(n):
    ##number of spaces
    k = n-1
    ##Number of rows(outer loop)
    for i in range(0,n):
    #number of spaces (inner loop)
      for j in range(0,k):
        print(end=" ")
        #decreasing k after each loop
        k -=1
        # inner loop to handle number of rows
        for j in range(0,i+1):
           #Printing stars
           print("* ",end = "")
           # ending line after each row
      print("\r")
    return

          
           