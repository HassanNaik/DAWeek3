#Comparison operators
#== Equal to
#!= Not equal to
#<  Less than
#<= Less than or equal to
#>  More than
#>= More than or equal to

#Logical Operators
#AND = The expressions either side of the logical operator are evaluated 
# – because we’re using and, either side needs to evaluate to True.
#True and True -> True
#True and False -> False
#False and False -> False

#OR = The expressions either side of the logical operator are evaluated 
# – but because we’re using or only one has to be true.
#True and True -> True
#True and False -> True
#False and False -> False

# if statements

# music = "classical"

# if music == "classical":
#     print("Oh no, it's classical again" )
# elif music == "no music":
#     print("Ah, peace and quiet" )
# elif music == "":
#     print("Ah, peace and quiet" )
# else:
#     print("Turn it up!" )

#Create a variable called age. 
#Write an if statement that prints “Yes I can serve you” if 
#age is greater than or equal to 18 and else prints 
#“You aren’t old enough”.
#Take your age checker code from earlier, and make 
#sure your guest is also in the U.K


# age = int(input("enter age: "))
# country = "uk"
             
# if age >= 18 and country == "uk":
#     print("Yes I can serve you" )
# elif age >= 18 and country == "uk":
#     print("Where are you from?")
# else:
#     print("You aren’t old enough")

#AND Logical Operator

# place = "MCR"
# weather = "Cloudy"

# if place == "MCR" and weather == "Sunny":
#     print("Check again")
# elif place == "MCR" and weather == "Rain":
#     print("Obvs")
# elif place == "MCR" and weather == "Cloudy":
#     print("Its cloudy today in manchester")
# else:
#     print("What? It isn't raining?")

#OR Logical Operators

# day = "Saturday"

# if day == "Saturday" or day == "Sunday" :
#     print("It's the weekend" )
# else:
#     print("When is the weekend?" )

#Activity 1
# Create a variable called password.
# Check how many letters are in the password, if there 
# are fewer than 8 print that the password is too short.
# Otherwise print the password.

password = input("Enter password: ")

if len(password)!=8 :
    print("password is too short" )
else:
    print(f"Your Password is {password}")

# Activity 2 % functions
# Create a variable called num.
# Check if the variable is divisible by 3 or 5. 
# If it is print “This number is divisible by 3 or 5” to the 
# terminal.
# Otherwise print “This number is not divisible by 3 or 5”.

num = float(input("Enter a number: "))
a = num % 3 
b = num % 5
c = num % 7

#print(a)
#print(b)

if a == 0 or b == 0:
   print("This number is divisible by 3 or 5" )
else:
   print("This number is not divisible by 3 or 5")
        
          

# Activity 3
# Create a variable called num.
# If num is divisible by 3 print “fizz”, if it’s divisible by 7 
# print “buzz”, if it’s divisible by both 3 and 7 print 
# “fizzbuzz”. 
# Otherwise print num.

if a == 0 and c == 0:
    print("fizzbuzz" )
elif c == 0:
    print("buzz" )
elif a == 0:
    print("fizz" )
else:
    print(num)

# Activity 4
# Correct the code on the following slide so it functions 
# as expected.
# Can you use anything to make sure “London” and 
# “london” are accepted as correct answers?
print("What is the capital of England?" )

answer = input("Type your answer here >>")

if answer.casefold() == "london":
    print(f"Correct! The answer is {answer.capitalize()}")
else:
    print(f"Incorrect, the answer is 'London', not {answer.capitalize()}")


# Activity 5
# Create a variable called word that takes a string.
# Create an if statement that checks if the last letter is 
# the same as the first. 
# If it is return true, otherwise return false.
# Activity 5: Stretch
# Create a variable called word that takes a string.
# Create an if statement that checks if the whole string is 
# a palindrome (reads the same forwards as it does 
# backwards e.g. abba)

word = input("Enter word: ")

if word[0] == word[-1]:
    print("True")
else:
    print("False")

test_txt = input('Enter text: ')
 
palindrome = False
for i in range(0, len(test_txt) // 2):
  palindrome = test_txt[i] == test_txt[0 - (i + 1)]
  if not palindrome:
      break
 
if palindrome:
    print(test_txt + ' is a palindrome')
else:
    print(test_txt + ' is not a palindrome')