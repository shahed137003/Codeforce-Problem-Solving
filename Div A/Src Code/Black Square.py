a=[]
wastedCalories=0
s=input("Enetr the string : ")
for i in range(4):
    a.append(int(input()))


for i in s:
    if i=='1':
        wastedCalories+=a[0]    
    elif i=='2':
        wastedCalories+=a[1]
    elif i=='3':
        wastedCalories+=a[2]
    elif i=='4':
        wastedCalories+=a[3]
        
print(wastedCalories)        