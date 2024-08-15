a=input("Enter the first string : ")
b=input("Enter the second string: ")

if a==b:
    print(-1)
else:
    if len(a)>len(b):
        print(len(a))
    else:
        print(len(b))
        
