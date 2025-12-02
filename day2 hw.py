#Write a Python program
paragraph = """Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.
Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception."""

#Display the length of the paragraph (number of characters).
print(len(paragraph))

#Display the first and last characters in the paragraph.
print(paragraph[0])
print(paragraph[-1])

#Slice and print a short preview: the first 50 characters
print(paragraph[:50])

#Replace all occurrences of the word "Python" with "PYTHON" (in all caps).
paragraphreplaced = paragraph.replace("Python", "PYTHON")

#Convert the entire paragraph to lowercase.
paragraphlower = paragraphreplaced.lower()

#Remove any extra whitespaces from the start or end.
paragraphtrimmed = paragraphlower.strip()

#Split the paragraph into individual words and print the list.
wordslist = paragraphtrimmed.split()
print("Words list:", wordslist)

#Check if the word "course" exists in the paragraph. Print a message if found.
if "course" in paragraphtrimmed:
    print("The word 'course' is found in the paragraph.")
else:
    print("The word 'course' is NOT found.")

#Display the final message:
finalmessage = "The course description is {} characters long and has {} words.".format(
    len(paragraphtrimmed), len(wordslist)
)
print(finalmessage)





