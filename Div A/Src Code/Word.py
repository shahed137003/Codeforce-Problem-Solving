word=input("Eneter the string : ")


lower=0
upper=0
for i in word:
    if i.islower()==1:
        lower+=1
    else:
        upper+=1
        
if upper>lower:
    print(word.upper())
else:
    print(word.lower())
    