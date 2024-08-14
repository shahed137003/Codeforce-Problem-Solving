n=int(input("Enter the number of events : "))
a=[]

print("Enter If the integer is -1 then it means a crime has occurred. Otherwise, the integer will be positive, the number of officers recruited together at that time. No more than 10 officers will be recruited at a time : ")
for i in range(n):
    a.append(int(input()))

unTreatedCrimes=0
police=0
for i in a:
    if i==-1:
        if police==0:
            unTreatedCrimes+=1
        else:
            police-=1      
    else:
        police+=i
        
print(unTreatedCrimes) 
            
        
