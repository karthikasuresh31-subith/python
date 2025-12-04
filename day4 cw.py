#Create separate lists for each section with at least 3 items.
fruits = ["apple", "orange", "mango"]
vegetables = ["carrot", "tomato", "onion"]
beverages = ["Juice", "Soda", "Water"]

#Add a new item to the fruits list.
fruits.append("kiwi")
print(fruits)

#Insert a new item at the second position of the vegetables list.
vegetables.insert(2, "cucumber")
print(vegetables)

#Remove the last item from the beverages list.
del beverages[2]
print(beverages)

#Combine all three lists into a nested list called inventory.
inventory = [fruits, vegetables, beverages]

#Use slicing to print only the first two fruits.
first_two_fruits = fruits[:2]

#Use negative indexing to access the last item from the vegetables list.
last_vegetable = vegetables[-1]

#Create a list of lengths of all items in the fruits list using list comprehension.
fruit_length = [len(item) for item in fruits]

#Check if "Water" is in the beverages list.
if"water" in beverages:
    print("yes, 'water' is in the beverages list")
else:
    print("no, 'water' is not in the beverages list")

#Finally, create a tuple of the first item from each section.
my_tuple = (fruits[0] ,vegetables[0] ,beverages[0])
print(my_tuple)