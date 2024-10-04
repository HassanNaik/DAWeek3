#Week 3 Day 2 Loops

#Code solves problems for us – and sometimes that problem is about efficiency.

# Iteration in Coding -For Loops

# Iteration means repeating or going over. 
# In coding, it could mean repeating the running of a certain block of code.

# For loops

# • Iterate though a sequence
# • Execute a block of code for as many things as there are in the sequence
# • Run a finite amountof times – they will always eventually stop

#Iteration in Coding -Range

#Range generates a sequence for us to iterate through.
#Range needs 1 argument – but is actually using 3. 
#start, stop, step

#Iteration in Coding -While

# Run infinitely until a condition is met
# Allow us to loop code for an unknown amount of times

# While loops don’t just need to work with input. 
# While loops are written with conditions. 
# If statements are also written with conditions.
# If you’re struggling to think of the while loop, try an if statement first!

#A while loop will run infinitely and do its job until a condition is met.

#Using range, find the total of adding the numbers 1 - 100.

sum1 = 0
for i in range(1,101):
    sum1 = sum1+i
print(sum1)

#peresh

total = sum(range(1, 101))
 
print(total)
#elliot


# Activity 1

# Create a for loop that prints “hello world” 13 times.
# Now, convert this into a while loop that does the same job.

print("for loop")

for i in range(13):
    print(f"hello world , {i+1}")

print("while loop")

i = 1
while i < 13:
  print(f"hello world , {i+1}")
  i += 1

# Activity 2

# Use a nested for loop to write a program which prints out the multiplication tables from 1 to 12. 
# Include a line-break between each multiplication table to make it easier to read.

Block1 = range(1,13)
Block2 = range(1,13)

for x in Block1:
     print()
     for y in Block2:
          print(f"{x} x {y} = { x * y}")



# Activity 3

# Write a small log-in program that asks a user to enter a password to continue.
# The user cannot continue until they get the password correct.

# Activity 3: Stretch

# Add a limit to this program – maybe the user can only try three times before they are locked out?
# Remember your logical operators!

answer = input("Enter Passowrd ")
attempt = 0


while answer != "Password" and attempt < 2:
    print("incorrect")
    attempt += 1
    answer  = input("Enter Passowrd ")
if attempt == 2:
        print("Too many failed attmepts, you are locked out! Have a nice day :)")

else:
    print("correct")


   
 