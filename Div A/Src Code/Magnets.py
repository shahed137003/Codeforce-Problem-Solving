n=int(input("Enter the number of magnets : "))
magnets=[]
groups=1
for i in range(n):
    magnets.append(input())
        
i=0
nextIndex=1
while  nextIndex!=n:
    if magnets[i][1]==magnets[nextIndex][0]:
            groups+=1        
    nextIndex+=1
    i+=1
    
    

print(groups)
                
            
            
        
    
    
           

        
    
    
        