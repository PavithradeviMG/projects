input = [["-","-","-","#","#"],
         ["-","#","-","-","-" ],
         ["-","-","#","-","-"],
         ["-","#","#","-","-"],
         ["-","-","-","-","-"]]
offsets = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
result = [[["-","#"][c=="#"] for c in row] for row in input] # initialize
for r,s in enumerate(input):# go through input rows
    for c,m in enumerate(s): #go through row's column
        for dr,dc in[] if m =="#" else offsets: #neighbours of "-" of cells
            if r+dr in range(len(input)) and c+dc in range(len(s)):
                result[r][c] += input[r+dr][c+dc] == "#" #count bomb




for row in result:
    for c in row:
        print(c, end =" ")
    print()