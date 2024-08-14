n=int(input("Enter the number of problems in the contest : "))
TeamSure=[]
for i in range(n):
    TeamInternal=[]
    for j in range(3):
        TeamInternal.append(int(input(" ")))
    print("")
    TeamSure.append(TeamInternal)
problemsToBeSolved=0       
for i in range(n):
    Sure=0
    for j in range(3):
      if  TeamSure[i][j]==1:
          Sure+=1
    if Sure>=2:
        problemsToBeSolved+=1
        
        
        
print("the number of problems the friends will implement on the contest "+str(problemsToBeSolved))
        
                   
