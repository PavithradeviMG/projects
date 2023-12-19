grid = [["-", "-", "-", "#", "#"],["-", "#", "-", "-", "-"], ["-", "-", "#", "-", "-"],["-", "#", "#", "-", "-"],["-", "-", "-", "-", "-"]]
counter=0
for row in len(grid):
	for col in len(grid):
		# North
	    if row > 0:
		    if grid[row - 1][col] == "#":
			    counter += 1
			    print(counter)
			else:
			    counter+=0

   #North west
        if row 

	# North East
         if row > 0 and col < len(grid) - 1:
		   if grid[row - 1][col + 1] == "#":
			  counter += 1
	# South
	if row < len(grid) - 1:
		if grid[row + 1][col] == "#":
			counter += 1


	grid[row][col] = counter
	counter = 0

		

		for count,value in enumerate(grid,start = 0):
		print(value)
			
		print(grid[row][col],end=' ')
	print()
