# Bab 1 - Pengenalan: program pertama
print("Halo Python")





# Chapter 2 - Variables and Data Types

# Floating point number
a = 7.5
print(a)

# Integer
x = 5
y = 3
z = x + y
print(z)

# String with single quotes
myFirstName = 'Rizqi'

# String with double quotes
myLastName = "Maulana"

# Number written as a string
myAge = "25"

# Multiline string
myHobby = """I like cycling
and playing games.
"""

# Print string variables
print(myFirstName + " " + myLastName)
print("My age is " + myAge)
print(myHobby)

# Correct boolean values
isStudent = True
isMarried = False
print(isStudent, isMarried)

# Incorrect boolean value (raises NameError if uncommented)
# c = true
# print(c)








# Chapter 3 - Operators

# Arithmetic operators
a = 4
b = 2
print(a + b)   # Addition: 6
print(a - b)   # Subtraction: 2
print(a * b)   # Multiplication: 8
print(a / b)   # Division: 2.0
print(a % b)   # Modulus: 0
print(a ** b)  # Exponentiation: 16

# Comparison operators
a = 3
b = 5
print(a == b)  # False
print(a != b)  # True
print(a < b)   # True
print(a <= b)  # True
print(a > b)   # False
print(a >= b)  # False

# Logical operators
a = 3
b = 9

# and
print(a < 5 and b > 6)  # True
print(a < 5 and b < 6)  # False
print(a > 5 and b < 6)  # False

# or
print(a < 5 or b > 6)   # True
print(a < 5 or b < 6)   # True
print(a > 5 or b < 6)   # False

# not
print(not (a < 5 or b > 6))  # False
print(not (a > 5 or b < 6))  # True





# Chapter 4 - Conditionals (if, elif, else)
# Python uses indentation to define code blocks.

# Correct indentation
if True:
    print("Correct.")

x = 5
y = 10

# Runs because x < y is True
if x < y:
    print("x is less than y.")

# Does not run because x > y is False
if x > y:
    print("x is greater than y.")

# if - elif
a = 80
if a > 90:
    print("Grade A.")
elif a > 70:
    print("Grade B.")  # runs

# if - elif - else
a = 60
if a > 90:
    print("Grade A.")
elif a > 70:
    print("Grade B.")
else:
    print("Grade C.")  # runs







# Chapter 5 - Loops

# for loop with range
for x in range(5):
    print("Hello Python.")

# for loop over a list
fruits = ['Apple', 'Banana', 'Mango', 'Durian']
for fruit in fruits:
    print(fruit)

# for loop over a string
myCountry = "indonesia"
for letter in myCountry:
    print(letter)

# while loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# break: stop the loop when x is 3
for x in range(5):
    print(x)
    if x == 3:
        break

# continue: skip even numbers, print odd numbers only
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)







# Chapter 6 - Lists

animals = ["Chicken", "Duck", "Lizard"]

# Access items by index (starts from 0)
print(animals[1])   # Duck
print(animals[-1])  # Lizard
print(animals[-2])  # Duck

# Add items
animals.append("Sheep")
print(animals)
animals.insert(2, "Crocodile")
print(animals)

# Remove items
animals = ["Chicken", "Duck", "Lizard"]
animals.remove("Duck")
print(animals)

animals = ["Chicken", "Duck", "Lizard"]
animals.pop()
print(animals)

animals = ["Chicken", "Duck", "Lizard"]
animals.pop(0)
print(animals)

animals = ["Chicken", "Duck", "Lizard"]
animals.clear()
print(animals)

# Combine lists
animals = ["Chicken", "Duck", "Lizard"]
otherAnimals = ["Sheep", "Eagle", "Elephant"]
animals.extend(otherAnimals)
print(animals)

fruits = ["Apple", "Mango", "Banana"]
otherFruits = ["Durian", "Watermelon", "Orange"]
allFruits = fruits + otherFruits
print(allFruits)









# Chapter 7 - Dictionaries

firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Access items
print(firstPerson['first_name'])  # Hana
print(firstPerson.get('age'))     # 10
print(firstPerson.keys())
print(firstPerson.values())

# Add an item
firstPerson['weight'] = 12
print(firstPerson)

# Update items
firstPerson['age'] = 15
firstPerson.update({"age": 15})
firstPerson.update({"hair_color": "black"})
print(firstPerson)

# Remove items
firstPerson.pop("age")
print(firstPerson)

firstPerson.clear()
print(firstPerson)







# Chapter 8 - Functions

# Function without arguments
def say_hello():
    print("Hello")

say_hello()

# Function with one argument
def greet(name):
    print("Hello, I am %s" % name)

greet("Rizqi")

# Function with two arguments
def introduce(name, age):
    print("Hello, I am %s. I am %d years old" % (name, age))

introduce("Rizqi", 30)

# Arbitrary arguments (*args)
def greet_many(*names):
    for name in names:
        print("Hello, I am %s" % name)

greet_many("Rizqi", "Fika", "Yudi")

# Keyword arguments: order does not matter
introduce(age=25, name="Fika")

# Arbitrary keyword arguments (**kwargs)
def introduce_student(**student):
    print("Hello, I am %s. I am %d years old" % (student['name'], student['age']))

introduce_student(age=20, name="Rizqi")

# Default argument value
def greet_default(name="Alien"):
    print("Hello, I am %s" % name)

greet_default()








# Chapter 9 - Classes and Objects

# Class with a property
class Cat:
    color = "black"

cat1 = Cat()
print(cat1.color)  # black


# Class with a constructor
class CatWithColor:
    color = "black"

    def __init__(self, color):
        self.color = color

cat2 = CatWithColor("orange")
print(cat2.color)  # orange


# Class with a method
class TalkingCat:
    def say(self):
        print("Meow..meow")

cat3 = TalkingCat()
cat3.say()


# The first method parameter can have any name (convention: self)
class CustomCat:
    color = "black"

    def say(myParam):
        print("My color is %s" % myParam.color)

cat4 = CustomCat()
cat4.say()







# Chapter 9 - PIP and Virtual Environments
from colorama import Fore, Style, init

init(autoreset=True)
print(Fore.GREEN + "Colorama is installed inside the virtual environment.")
print(Fore.RED + "This line is printed in red.")
print(Style.BRIGHT + Fore.CYAN + "PIP and venv work correctly.")