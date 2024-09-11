units=int(input("Enter total units consumed:"))
bill_amount=0
if(units>0 and units <=100):
    bill_amount=units*5
elif(units>100 and units<=200):
    bill_amount=100*5+(units-100)*10
elif(units>200):
    bill_amount=(100*5)+(100*10)+(units-200)*15
print(f"bill amount is:{bill_amount}")


