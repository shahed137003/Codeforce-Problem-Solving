n=int(input("Enter the number of chars in this string: "))
string=input("Enter the required string: ")
string=string.lower()
if n<26:
    print("No")
else:
    similar=0
    checked=[]
    for i in range(n):
        checked.append(0)
    for i in range(n):
        if checked[i]==0:
              for j in range(i+1,n):
                  if string[i]==string[j] :
                      similar+=1
                      checked[j]=1
    dist=n-similar
    if dist==26:
        print("Yes")
    else:
        print("No")
               
                
            
      
                
                
