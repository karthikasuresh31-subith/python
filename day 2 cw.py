header = """BOOKSTORE RECEIPT"""

#each line showing the book and price, use a single string with basic {} placeholders and call format() once to fill in the values.
book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

a = "\t{}  - {}".format(book1,price1)
b = "\t{}  - {}".format(book2,price2)

#Calculate the total price and add it similarly.
totalprice = price1 + price2
total = "\tTotal: {}".format(totalprice)

#Concatenate a thank-you message at the end.
thankyou = "\nTHANK YOU FOR YOUR PURCHASE!!!"

#Make sure the output uses newline (\n) and tab (\t) for readability.
receipt = header + "\n" + a + "\n" + b + "\n" + total + thankyou

#Display the entire receipt in uppercase.
print(receipt.upper())

