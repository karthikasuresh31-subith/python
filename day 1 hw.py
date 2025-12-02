#Use variables to store the prices and quantities.
import random
rice = 45
sugar = 40
oil = 130

riceqty = 3
sugarqty = 2.5
oilqty = 1.8

ricetotal = rice * riceqty
sugartotal = sugar * sugarqty
oiltotal = oil * oilqty

print(ricetotal)
print(sugartotal)
print(oiltotal)

#Use appropriate data types
print(type(ricetotal))
print(type(sugartotal))
print(type(oiltotal))

#Calculate and print the total price for each item and the final total bill.
finalbill = ricetotal + sugartotal + oiltotal
print(finalbill)

#Show the total bill as an integer and also as a string.

billasstr= str(finalbill)
print(billasstr)

billasint = int(finalbill)
print(billasint)


#Use random number generation to add a random ?5–?10 delivery charge
deliverycharge = random.randrange(5,10)
print(deliverycharge)

#Show the final bill amount including delivery charge.
finalamount = finalbill + deliverycharge
print(finalamount)


