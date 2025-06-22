n=int(input())
problems=[]
for i in range(n):
    inp=input()
    sureness=inp.split(" ")
    problems.append(sureness)
    
count=0 
for problem in problems:
    sureenough=0
    for sure in problem:
        if sure == '1':
            sureenough+=1
            
    if sureenough >=2:
        count+=1
        
print(count)