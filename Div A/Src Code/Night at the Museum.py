string=input(" the name of some exhibit : ")
rotations=0

currentPosition=ord("a")

for i in string:
    clockWise=26-abs(ord(i)-currentPosition)
    antiColockWise=abs(ord(i)-currentPosition)
    if clockWise<antiColockWise:
        rotations+=clockWise
    else:
        rotations+=antiColockWise   
    currentPosition=ord(i)
        
print(rotations)        
