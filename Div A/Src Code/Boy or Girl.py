string=input("Enter the username: ")

distinct=0
similars=[]
for i in range(len(string)):
    if i not in similars:
        distinct+=1
        for j in range(i+1,len(string)):
           
           if string[i]==string[j]:
               
              similars.append(j)

              

    
   
if   distinct%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
        
               



               
            
    