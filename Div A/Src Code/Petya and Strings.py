string1=input("Enter the first string : ")
string2=input("Enter the second string :")
diff=0
string1=string1.lower()
string2=string2.lower()
for i in range(len(string1)):
    diff+=(ord(string1[i])-ord(string2[i]))
    
if diff==0:
    print(0)
elif diff<0:
    print(-1)
else:
    print(1)
