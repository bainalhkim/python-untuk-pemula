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