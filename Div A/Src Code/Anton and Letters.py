string=input("Enter the string that to be used : ")

similar=0
totalLetters=0
for i in range(1,len(string),3):
    if string[i]!='}':
        totalLetters+=1
        
        
# to get the number of similar letters: 
for i in range(1,len(string),3):
    for j in range(i+3,len(string),3):
        if string[i]==string[j]:
            similar+=1
            
distinct=totalLetters-similar   
print(distinct)