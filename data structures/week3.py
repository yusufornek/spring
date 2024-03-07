# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:29:25 2024

@author: test2
"""
"""Basic Concepts of Python Programming
Data Structures & Management
Assoc. Prof. Elif KARTAL"""
# -*- coding: utf-8 -*-
"""
@title: Basic Concepts of Python Programming
@author: Assoc. Prof. Elif Kartal
@date: March 9, 2023
"""
# Say Hello World with Python.
print("Merhaba Dünya!")
print("Hello World!")
# My variables for the first time:)
name = "Elif"
# name = 'Elif'
age = 36
print(name, "is", age, "years old.")
print("""Names of my cats are,
 Çiçero
 Mısık""")
print("My name is " + name)
print("My name is " + name + " and is " + age + " years old.")
print("My name is", name, "and is", age, "years old.")
"""
Python Indentation
be careful how you write in Python!
"""

print("\"Elif\" Kartal")
song = "Nothing Else Matters"
song[1]
song[1:]
song[:1]
song[1::2]
my_text = "My name is {} and is {} years old."
print(my_text.format(name, age))
Surname = 'Kartal'
print(name, Surname)
# String Methods
# https://www.w3schools.com/python/python_strings_methods.asp
dna_sequence = "tgtcgtagggacgggccaacgttcctag"
len(dna_sequence)
"""Basic Concepts of Python Programming
Data Structures & Management
Assoc. Prof. Elif KARTAL"""
dna_sequence.upper()
dna_sequence.find("tag", 0, len(dna_sequence))
dna_sequence.rfind("cc", 0, len(dna_sequence))
dna_sequence = dna_sequence.replace("tag", "gta")
# Variable Definitions
""""076_numb = 1 Değişken tanımlamaları sayı ile başlayamaz."""
"""my-numb = 81"""
"""my numb = 1903 Boşluk olamaz!"""
"""elif = 37 Fonksiyon veya Python'a özgü tanımlar kullanılamaz!"""
myNumb = 1903
mynumb = 1903
my_numb = 1903
myNumb1 = 1903
# Multiple Assignment
a, b, c, d = 30, 35, 40, 45
# Integer
print(0, "is", type(0))
print(-100, "is", type(-100))
print(100, "is", type(100))
print(1234567890, "is", type(1234567890))
print(1234567890123456789012345678901234567890123456789012345678901234567890, "is",
      type(1234567890123456789012345678901234567890123456789012345678901234567890))
ord("E")
ord("e")
chr(69)
chr(101)
# Additionally:
print(0b1010, "in base 2 is 1010 and the type is ", type(0b1010))
print(0o12, "in base 8 is 12 and the type is ", type(0o12))
print(0xA, "in base 16 is A and the type is ", type(0xA))
# Float
print(-0.1, "is", type(-0.1))
print(.325, "is", type(.325))
print(0.1234567890, "is", type(0.1234567890))
print(1E2, "is", type(1E2))  # 1x10^2 = 100
print(1e2, "is", type(1e2))  # 1x10^2
print(1e-2, "is", type(1e2))  # 1 üzeri -2 0.01
print(1.799e308)
print(5e-324)
print(1e-324)
# Complex Numbers
print(2+3j, "is", type(2+3j))  # complex numbers
type(2j)
"""Basic Concepts of Python Programming
Data Structures & Management
Assoc. Prof. Elif KARTAL"""
# None
y1 = None
print(y1)
# hem bir öncekini hem de kendisini yazar. Print içinde print.
print(print("Hello World!"))
# Boolean
True
False
x = 10
y = 20
z = "elif"
a = 0
b = -2
bool(x)
bool(y)
bool(z)
bool(a)
bool(b)
bool("")
10 > 20
10 < 20
10 == 20
10 != 20
10 == 20 and 10 < 20
10 == 20 or 10 < 20
# Basic Control Statements
# Example 1
# Finding maximum
x = 35
y = 100
my_max = y
if x > y:
    my_max = x
print("Maximum is ", my_max)

"""Basic Concepts of Python Programming
Data Structures & Management
Assoc. Prof. Elif KARTAL"""
# Example 2
# Fasting Blood Sugar Levels: <80: low, 80-100 normal, 101-125 impaired
# glucose, > 125 diabetic
bs_level = 150
if bs_level >= 0 and bs_level <= 80:
    print("low")
elif bs_level >= 80 and bs_level <= 100:
    print("normal")
elif bs_level >= 101 and bs_level <= 125:
    print("impaired glucose")
elif bs_level > 125:
    print("diabetic")
else:
    print("Please insert a positive number!")

# Casting
my_num = str(50)
print(my_num)
my_num = int(my_num)
print(my_num)
my_num = float(my_num)
print(my_num)
# Try it with print(type(my_num)) statement.
# Arithmetic Operators
x = 3
y = 5
x + y
x - y
x * y
x / y
y % x
x ** y
y // x
y/x
# Assignment Operators
x = 100
x = x + 5
x += 5
x -= 5
x = x - 5
(18/3+10)*2-70/5


name = "elma"
if "e" in name:
    print("There is a e")
else:
    print("There is no e")


# Data input from user
""""guess = input("What is day of the week two days after the day after the day"""
""""before yesterday?\nAnswer= ")"""
correctAnswer = "tomorrow"
"""if guess.lower() == correctAnswer:
    print("Congratulations!")
else:
    print("Try again!")
# Burada birden fazla değişkeni, aynı anda ve beraber tanımlamış olduk."""
a, b, c, d = 10, 20, 30, 40
"""import random

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print(random.random())"""
