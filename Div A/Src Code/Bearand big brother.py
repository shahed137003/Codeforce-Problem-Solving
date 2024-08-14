
a=int(input("Enter the weight of Limak : "))
b=int(input("Enter the weigtht of Bob : "))
years =0
Done=0

while Done==0:
    a*=3
    b*=2
    years+=1
    if a>b:
        Done=1
        
print("the number of years after which Limak will become strictly larger than Bob "+str(years))