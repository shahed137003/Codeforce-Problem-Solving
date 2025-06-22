w = int(input(""))

n1 = w
n2 = 0
flag=0
while n1 != 0:
    if n1 % 2 == 0 and n2 % 2 == 0 and n1!=0 and n2!=0:
        print("YES")
        flag=1
        break
    n1 -= 1
    n2 += 1

if flag == 0:
    print("NO")
