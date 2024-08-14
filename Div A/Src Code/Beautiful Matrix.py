Matrix=[]

for i in range(5):
    interalMatrix=[]
    for j in range(5):
        interalMatrix.append(int(input()))
    print()  
    Matrix.append(interalMatrix)
    
onePositionRaw=0
onePositionCol=0
for i in range(5):
    for j in range(5):
        if Matrix[i][j]==1:
            onePositionRaw=i
            onePositionCol=j
            break
minMoves=abs(onePositionRaw-2)+abs(onePositionCol-2)
print("the minimum number of moves needed to make the matrix beautiful."+str(minMoves))           
            