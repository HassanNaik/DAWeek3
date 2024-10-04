print("All Around The World"[7].upper())
#prints U in terminal

# assignment operator
# =
#We can combine our
# += or -= 
# #assignment operator = withour arithmetic operators.
# *= or /=
#These operators do the sum and store the value all in one!
 
 #intergers
# + Addition
# - Subtraction
# * Multiplication
# ** Exponential
# / Division
# % Modulo (Remainder)

my_name = "Hassan"
#string variable is Hassan
my_age_str = "35"

str_is_student = "True"

my_age = 35
#intager varibale is 35

is_a_student = True
#Boolean variable is True

print(my_name)
#Prints variable Hassan in the terminal

print("This is",my_name, "i am",my_age,"years old. It is",is_a_student,"that i am a student at code nation")
#,

print("This is ",my_name, "i am "+my_age_str,"years old. It is "+str_is_student,"that i am a student at code nation")
#+

print( "This is {} i am {} years old. It is {} that i am a student at code nation".format(my_name,my_age_str,str_is_student))
#.format

print(f"This is {my_name} i am {my_age_str} years old. It is {str_is_student} that i am a student at code nation")
# f string

user_name = input("Type in your name: ")
user_age = input("Type your age: ") 
user_drink = input("What is your favourite drink? ")
#Input allows us to write a prompt to the user, and then the terminal will wait for the user’s response before continuing execution.
 

print(f"Hello {user_name}. You are {user_age} years old. {user_drink} is your favourite drink")
#prints string Hello with variable user name 

num1 = int(input ("Type number 1: "))
num2 = int(input ("Type number 2: "))
#Casting


print(f"num1 + num2 = {num1 + num2}")
print(f"num1 - num2 = {num1 - num2}")
print(f"num1 * num2 = {num1 * num2}")
print(f"num1 / num2 = {num1 / num2}")
print(f"num1 % num2 = {num1 % num2}")

balance = 100
amount_withdrawn = 50

balance = balance - amount_withdrawn

print(balance)
#prints 50 which is 100- 50

balance -= amount_withdrawn

print(balance)
#prints 0 which is 50-50

#Activity 1 done in line 47 to 53
#Create a program which asks a user their name, age, and favourite colour. 
#Print these in a sentence using an f string.

#Activity 2 done in lines 56 to 65
#Create a program which accepts two inputs from a user (num1 and num2). 
#Use these inputs with each operator (+, -, /, *, **, %). 
#Print the equation and the output.

#Activity 3
#A shop sells apples for 25p per apple, and bananas for 50p per banana.
#Create a program which asks a user how many apples they want to buy, and how many bananas they want to buy.
#Display the total cost of the apples, the total cost of the 
#bananas, the cost of both combined.

#Activity 3: Stretch
#10 apples would cost £2.50
#Your program will say £2.5
#Research how to have your answer formatted to have 
#two decimal places.

apples = float(0.25)
#price of apples
banana = float(0.50)
#prices of bananas

user_a = int(input("How many apples would you like? "))
user_b = int(input("How many bananas would you like? "))

print(f"You would like {user_a} apples for £{apples:.2f} = £{user_a*apples:.2f}")
print(f"You would like {user_b} apples for £{banana:.2f} = £{user_b*banana:.2f}")
print(f"Your total is £{(user_a*apples)+(user_b*banana):.2f}")

