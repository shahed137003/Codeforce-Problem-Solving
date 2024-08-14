DankiWin=0
AntonWin=0
n=int(input("Enter the number of games: "))
s=input("Enter the  outcome of each of the games (A for Anton and D for Danki) : ")


for i in s:
    if i=='A':
        AntonWin+=1
    else:
        DankiWin+=1


if DankiWin==AntonWin:
    print('Friendship ')
elif (DankiWin>AntonWin):
    print('Danik')
else:
    print('Anton')
    