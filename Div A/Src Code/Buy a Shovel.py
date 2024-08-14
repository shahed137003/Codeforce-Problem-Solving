k=int(input("Enter the price of one shovel  "))
r=int(input("Enter the denomination of the coin in Polycarp's pocket that is different from 10_burle coins: "))

shovls=0
whatYouPay=0
TotalPriceToBePaid=0
coinCharge=0
charge=1
while charge!=0 :
    shovls+=1
    TotalPriceToBePaid+=k
    while  (whatYouPay+r)<TotalPriceToBePaid:
        whatYouPay+=10
        if whatYouPay+r== TotalPriceToBePaid:
            coinCharge=1
            
    if coinCharge==1:
        break        
    charge=whatYouPay-TotalPriceToBePaid
   

 

print(shovls)
