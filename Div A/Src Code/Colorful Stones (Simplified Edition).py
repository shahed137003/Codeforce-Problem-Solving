stones=input("Enter the color of the i-th stone ")
instructions=input("Enter the instruction to be performed : ")

currentPosition=0


for i in instructions:
    if stones[currentPosition]==i:
        currentPosition+=1


currentPosition+=1

print(currentPosition)
