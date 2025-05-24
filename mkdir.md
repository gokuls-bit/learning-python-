'''1. Basic String Functions
Function	Description
len(s)	Returns the length of the string s.
str(x)	Converts a value x to a string.

2. Case Conversion
Function	Description
s.lower()	Converts all characters to lowercase.
s.upper()	Converts all characters to uppercase.
s.capitalize()	Capitalizes the first character.
s.title()	Capitalizes the first letter of each word.
s.swapcase()	Swaps the case of each character.

3. Searching and Replacing
Function	Description
s.find(sub)	Returns the lowest index of substring sub. Returns -1 if not found.
s.index(sub)	Same as find() but raises an error if not found.
s.rfind(sub)	Returns the highest index of substring sub.
s.replace(old, new)	Replaces all occurrences of old with new.
s.count(sub)	Counts the number of occurrences of sub.

4. Validation Methods
Function	Description
s.isalpha()	Returns True if all characters are alphabetic.
s.isdigit()	Returns True if all characters are digits.
s.isalnum()	Returns True if all characters are alphanumeric.
s.isspace()	Returns True if all characters are whitespace.
s.islower()	Returns True if all characters are lowercase.
s.isupper()	Returns True if all characters are uppercase.
s.istitle()	Returns True if string is titlecased.

5. Splitting and Joining
Function	Description
s.split(delimiter)	Splits string into a list using the delimiter (default is whitespace).
s.rsplit(delimiter)	Splits from the right side.
s.splitlines()	Splits at line breaks.
'delimiter'.join(list)	Joins a list into a string with delimiter.

6. Trimming and Formatting
Function	Description
s.strip()	Removes leading/trailing whitespace.
s.lstrip()	Removes leading whitespace.
s.rstrip()	Removes trailing whitespace.
s.zfill(width)	Pads string with zeros on the left.
s.center(width)	Centers the string in a field of given width.
s.ljust(width)	Left-justifies the string.
s.rjust(width)	Right-justifies the string.
s.format(...)	Formats string with placeholders.
f"{var}"	f-string formatting (Python 3.6+).'''
'''🐍 Python Handy Notes
📌 1. Basic Syntax
python
Copy
Edit
# Single-line comment
'''
Multi-line string (not an actual comment)
'''

print("Hello, World!")  # Output
📌 2. Variables and Data Types
python
Copy
Edit
x = 10              # int
y = 3.14            # float
name = "Alice"      # str
is_active = True    # bool
📌 3. Data Structures
🔹 Lists
python
Copy
Edit
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits[0]  # 'apple'
🔹 Tuples
python
Copy
Edit
point = (10, 20)
🔹 Dictionaries
python
Copy
Edit
person = {"name": "Alice", "age": 25}
person["name"]  # 'Alice'
🔹 Sets
python
Copy
Edit
unique = {1, 2, 3, 3}
📌 4. Control Statements
python
Copy
Edit
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Loops
for i in range(5):
    print(i)

while x > 0:
    x -= 1
📌 5. Functions
python
Copy
Edit
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))
📌 6. String Methods
python
Copy
Edit
s = " Hello World "
s.strip()      # Remove spaces
s.lower()      # ' hello world '
s.upper()      # ' HELLO WORLD '
s.split()      # ['Hello', 'World']
" ".join(["A", "B"])  # 'A B'
📌 7. List Comprehension
python
Copy
Edit
squares = [x*x for x in range(5)]
📌 8. Exception Handling
python
Copy
Edit
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("Done")
📌 9. File I/O
python
Copy
Edit
# Writing
with open("file.txt", "w") as f:
    f.write("Hello")

# Reading
with open("file.txt", "r") as f:
    content = f.read()
📌 10. Modules & Libraries
python
Copy
Edit
import math
print(math.sqrt(16))

import random
print(random.randint(1, 10))
📌 11. Classes & Objects
python
Copy
Edit
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I am {self.name}")

p = Person("Alice")
p.greet()
📌 12. Useful Built-in Functions
Function	Description
len()	Length of string/list
type()	Data type
int(), str()	Type conversion
range(start, stop)	Generate numbers
enumerate()	Index + value in loop
zip()	Pair elements of iterables'''
