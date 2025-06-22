n=int(input())
words=[]
for i in range(n):
    inp =input()
    words.append(inp)
    
for wordm in words:
    if len(wordm)<=10:
        print(wordm)
    else:
        print(wordm[0]+str(len(wordm)-2)+wordm[-1])
