n=int(input("Enter the number of digits in the password: "))
k=int(input("Enter the number of distinct char in the string: "))
chars=[]
for i in range(97,123):
    chars.append(chr(i))
    
password=[] 

for i in range(k):
    password.append(chars[i])
i=0    
remaining=n-k
while i!=remaining:
    if i==k:
        i=0
        remaining-=k
        continue
    password.append(chars[i])
    i+=1
    

        
StringPassword=''.join(password)
print(StringPassword)
