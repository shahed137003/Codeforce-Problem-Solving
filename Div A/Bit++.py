x=0 
n=int(input())
statements=[]

for i in range(n):
    statements.append(input())
    
for statement in statements:
    if "+" in statement:
        x+=1
    elif "-" in statement:
        x-=1
        
print(x)