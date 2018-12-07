#2-1. Simple Message: Store a message in a variable, and then print that message .
message = "Hello Python world!"
print(message)

message_1 = "Hello Python Crash Course World"
print(message_1)

#2-2. Simple Messages: Store a message in a variable, and print that message . Then change the value of your
#  variable to a new message, and print the new message .

message_1 = "The Cleveland Browns are awesome"
print(message_1)

#2-3. Personal Message: Store a person’s name in a variable, and print a message to that person . Your
#message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

message = "Hello Cody, would you like to watch football today?"
print(message)

#2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase,
#and titlecase .

name = "Cody Cardillo"
print(name.upper())
print(name.lower())
print(name.title())

#2-5. Famous Quote: Find a quote from a famous person you admire . Print the quote and the name of its author .
#Your output should look something like the following, including the quotation marks:

message = 'A man named Wayne Gretzky once said, "You miss 100% of the shots you dont take" '
print(message)

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called
#famous_person . Then compose your message and store it in a new variable called message . Print your message .

famous_person = "Wayne Gretzky"
message = "A man named " + famous_person.title() + ' once said, "You miss 100% of the shots you dont take"'
print(message)

#2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the
#name . Make sure you use each character combination, "\t" and "\n", at least once .

print("Name:\n\tCody\n\tCody\n\tCody")

#2-7. Print the name once, so the whitespace around the name is displayed . Then print the name using each of the three
#stripping functions, lstrip(), rstrip(), and strip() .

favorite_language = ' python '
favorite_language.rstrip()
' python'
favorite_language.lstrip()
'python '
favorite_language.strip()
'python'

#Write addition, subtraction, multiplication, and division operations that each result in the number 8 . Be sure to
#enclose your operations in print statements to see the results . You should create four lines that look like this:
# Cody October 13th 2018
print("This program adds, subtracts, multiplies, and divides numbers")

print(4+4)
print(10-2)
print(2*4)
print(16/2)

#2-9. Favorite Number: Store your favorite number in a variable . Then, using that variable, create a message that
#reveals your favorite number . Print that message .

age = 44
message = "Happy " + str(44) + "rd Birthday!"
print(message)

#2-10. Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each . If you don’t
#have anything specific to write because your programs are too simple at this point, just add your name and the current
#date at the top of each program file . Then write one sentence describing what the program does .
# Cody October 13th 2018
print("This program adds additional comments")







