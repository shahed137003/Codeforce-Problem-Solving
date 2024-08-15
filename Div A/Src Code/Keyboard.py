letter=input("Enetr the letter discriping the shifting: ")
string=input("Enter the  sequence of characters written by Mole: ")
keyboard=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']
outPutList=[]
shift=0
if letter=='R':
    shift=-1
else:
    shift=1
for i in string:
    for  j in range(30):
        if i==keyboard[j]:
            if j==0 and letter=='R':
                outPutList.append(keyboard[j])
            elif j==29 and letter=='L':
                outPutList.append(keyboard[j])
            else:
                outPutList.append(keyboard[j+shift])
                break
            
            
theActual=''.join(outPutList)            
print(theActual)        