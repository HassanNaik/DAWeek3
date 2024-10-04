# Week 3 Day 2 Lists
# Coding is all about data – storing it, retrieving it, manipulating it.
# So far, we’ve been storing one bit of data to variable –
# but what about if we wanted a collection of data? 

#List syntax
#Lists are stored within [] square brackets, with each item separated by a comma.
# To access the data inside the list, we use the variable name.

# Each item in this case is a string – they’ll all need their own set of quotation marks.

#The items don’t need to be on a new line – but it does make it more readable.

#Data, Properties and Methods with Lists

#Properties
# We can find out properties of our lists – like how many items are in the list.
# We can use len()!

#Methods
#Like strings, lists have associated methods we can use to manipulate them! 
#Remember dot notation:
#object.method()
#Add
#The .append() method allows us to add an item to the end of our list.
#Remove
#The .pop() method will remove the last item in our list.
#Or we can give it an index position to work with, if we know where things are in the list

# .remove() - The remove() method removes the first occurrence of the element with the specified value.
# .reverse() - The reverse() method reverses the sorting order of the elements.
# .sort() - The sort() method sorts the list ascending by default.
# .count() - The count() method returns the number of elements with the specified value.
# .extend() - The extend() method adds the specified list elements (or any iterable) to the end of the current list.

#Dictionaries

# Lists are useful in a single dimension. 
# A tabular structure allows us to look things up based on a key. 
# This could be a cell reference (like A3) or simply a useful word. 
# You might look something up in a dictionary.

#In real life, dictionarieshold words and their definitions in pairs.
# Coding: the process or activity of writing computer programs.

# In Python, dictionaries are collections of data.
# The data is stored inkey:value pairs.

# Dictionaries are wrapped in {}curly brackets.
# Keys and values are split by : a colon.
# Items are split by , a comma.

# Keys and values are linked together.
# The key is a unique identifier for the value.
# A key:value pair is called an item.

# The dictionary key must be an immutable datatype.
# This means a data type that can’t be changed once it’s been made.
# It would be hard to look something up by its name if the name kept changing!

# Immutable data types include:
# • strings
# • integers
# • floats
# • Booleans
# • None.

# Mutable data types include:
# • lists
# • sets
# • dictionaries

#Values can be any data type; strings, integers, lists, other dictionaries,and even functions!

#A key cannot be changed, but a value can.
# Much like how we updated list elements using their index position, 
# we can update the values of our dictionary items using a key.

# Like lists, dictionaries have associated methods.
# These methods can allow us to access data within our dictionary.

#coffee_order = [
#        "Alex - Cortado",
#        "Ben - Latte",
#        "Charlie - Mocha"
#]
#creates a list for variable coffee_order

#print(coffee_order)
#prints ['Alex - Cortado', 'Ben - Latte', 'Charlie - Mocha'] on one line

my_list = [
        "Laptop",
        "Iphone",
        "Book"
]
#creates a list for variable

print(my_list)
#prints my_list

my_list[2] = "Clock"

print(my_list)


#Activity 1
#Copy out the list. 
#Use a method to find out how many of the following items I’ve ordered:
# • egg
# • kale
# • stamps
# • carrot
# • orange juice

s_l = [
    "apple",
    "carrot",
    "pizza",
    "carrot",
    "dog food",
    "orange juice",
    "egg",
    "kale",
    "carrot",
    "kale",
    "orange juice",
    "kale",
    "toilet roll",
    "stamps",
    "noodles",
    "pasta sauce",
    "egg",
    "pasta sauce"
]

s_l.sort()
print(s_l)

e = s_l.count("egg")
k = s_l.count("kale")
s = s_l.count("stamps")
c = s_l.count("carrot")
o = s_l.count("orange juice")

print(f"{e} egg {k} kale {s} stamps {c} carrot {o} orange juice")

#Acitvity 1

#Create a dictionary of four animals and what their babies are called
# (e.g. “Lion” : “Cub”)
#Using square brackets, print the value of your third item.

a_b = {
    "Elephant":"Calf",
    "Racoon":"Kit",
    "Otter":"Pup",
    "Pig":"Piglet",
    "Alpaca":"Cria"
 
}

print(a_b)
print(a_b.keys())
print(a_b.values())
print(a_b.items())
print(a_b["Otter"])
print(a_b.get(input("Enter animal for baby name: "),"This does not exist in my dictionary"))

# Activity 1

# Create a list of your three favourite websites and then 
# add another two using a method.
# Then, remove the last website using a method.

website = [
    "Google",
    "Youtube",
    "Bing"
]

website.append("apple")
website.append("Hotmail")

print(website)

website.pop()

print(website)



# Activity 2

# Research into the following list methods:
# .remove()
# .reverse()
# .sort()
# .count()
# .extend()
# Write a program demonstrating each method.

website2 = [
    "Google",
    "Youtube",
    "Bing"
]

website2.remove("Bing")
print(website2)
website2.reverse()
print(website2)
website2.sort()
print(website2)
print(website2.count("Google"))

site2 = [
    "MS",
    "Fifa",
    "MW"
]

website2.extend(site2)
website2.sort()

print(website2)




# Activity 3

# Using the two lists, create a dictionary where country is the key, and language is the value.

countries = ["England", "Spain", "Ethiopia", "Iran"]

languages = ["English", "Spanish", "Amharic", "Farsi" ]


# Creating a dictionary from two lists
my_dict = dict(zip(countries, languages))

print(my_dict)

# Activity 4

# Using your dictionary of animals, create a program 
# which allows a user to search for an animal to see the corresponding young name.
# If the animal does not exist in the dictionary, return a suitable message.

