n=int(input("enter the number of cards in the table : "))
a=[]
sereja=0
dima=0
for i in range(n):
    a.append(int(input()))
     
      
turn=1
i=0
while n!=0 and i!=n:
    if turn%2==0:
        if a[i]>a[n-1]:
            dima+=a[i]
            i+=1
        else:
            dima+=a[n-1]
            n-=1
    else:
        if a[i]>a[n-1]:
            sereja+=a[i]
            i+=1
        else:
            sereja+=a[n-1]
            n-=1
    turn+=1
 
print(str(sereja)+" "+str(dima))
        
            
            
            
            
        
            
            
    
            
            
        
    
    
   
        

        
        

        
            
        
    
    
    



