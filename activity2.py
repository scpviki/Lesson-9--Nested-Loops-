units=int(input("Enter the units you have consumed--"))
if(units<50):
    amount=units*2.6
    tax=25
elif(units<=100):
    amount=130+((units-50)*3.25)
    tax=35
elif(units<=200):
    amount=192.50+((units-100)*5.26)
    tax=45
else:
    amount=130+162.50+526+((units-200)*8.45)
    tax=75
total_amount=amount+tax
print(f"Your total electricity bill is{total_amount}")