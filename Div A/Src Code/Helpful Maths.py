string=input("Enter the string containing the sum of the numbers: ")
charList=string.split('+')
numbers=0
for i in string:
    if i!='+':
        numbers+=1
        
for i in range(numbers):
    for j in range(i+1,numbers):
        num1=int(charList[i])
        num2=int(charList[j])
        if num1>num2:
            temp=charList[i]
            charList[i]=charList[j]
            charList[j]=temp
            
newString='+'.join(charList)       

print(newString)