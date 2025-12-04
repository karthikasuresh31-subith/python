#Create a list for each workshop containing the names of 3 participants.
web_development = ["Ramesh","Kiran","Vikram"]
data_science = ["Aditi","Vijay","sanjay"]
ui_ux_design =["Ravi","viji","sam"]

#Combine all three workshop lists into a single nested list called all_participants.
all_paticipants = [web_development , data_science , ui_ux_design]

#A new participant joins the Web Development workshop — add their name to that list
web_development.append("Neha")
print(web_development)

#Insert one more participant at the 2nd position in the Data Science list.
data_science.insert(2, "Sruthi")
print(data_science)

#Remove the last participant from the UI/UX Design list.
del ui_ux_design[2]
print(ui_ux_design)

#Copy the list of Data Science participants to a new list and clear the original.
new_data_science = data_science.copy()
data_science.clear()
print(new_data_science)

#From the Web Development list, display only the first two participants.
two_participants = web_development[:2]
print(two_participants)

#Use list comprehension to create a list of the length of each name in the copied Data Science list.
name_length = [len(name) for name in new_data_science]
print(name_length)

#Check whether “Asha” is in any of the workshop lists.
asha_name = ("Asha" in web_development or
"Asha" in new_data_science or
"Asha" in ui_ux_design
)
print(asha_name)

#Finally, create a tuple that stores the name of the first participant from each workshop list (use slicing and indexing as needed).
my_tuple = (web_development[0],new_data_science[0],ui_ux_design[0])
print(my_tuple)

