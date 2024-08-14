n=int(input("Enter the stones in the table :"))
s=input("Enter the color of each stone in the tabel: ")

stoneToBeremoved=0
i=0
while i<n:
    neibours=i+1
    while neibours<n:
        if s[i]!=s[neibours] :
            break
        neibours+=1
        stoneToBeremoved+=1
    i=neibours

print(stoneToBeremoved)
    