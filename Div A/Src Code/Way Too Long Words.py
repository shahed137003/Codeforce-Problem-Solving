n=int(input("Enter the number of the words that is used: "))
a=[]
print("Enter the words: ")
for i in range(n):
    a.append(input())
    

for i in range(n):
    if len(a[i])>10:
        a[i]=a[i][0]+str(len(a[i])-2)+a[i][len(a[i])-1]
        
for i in range(n):
    print(a[i])