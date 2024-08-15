n=int(input("Enter the number of oranges: "))
b=int(input("Enter the maximum size of the orange that fits in the juicer: "))
d=int(input("Enter the value that determines the condition when the waste section should be: "))
a=[]
print("Enter the size of each orange: ")
for i in range(n):
    a.append(int(input()))

emptyWaste=0
totalSize=0

for i in range(n):
    if a[i]<=b:
        totalSize+=a[i]
        if totalSize>d:
            emptyWaste+=1
            totalSize=0

print(emptyWaste)