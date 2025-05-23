#three ways to write a string 
#name = "gokul"
#name = 'gokul'
#name = '''gokul'''

#name = '''gokul'''
#nameshort = name[0:3]
#print(nameshort)
#character1 = name[1]
#name = "santonment"
#print(name[0:3])
#print(name[-4: -1])
#print(name[:4])
#print(name[1:])
#print(name[1:5])
##word ="amazious"
##print(word[1:4:2])

# string functions 
##name ="Harvinder"
#print(len(name))
#print(name.endswith("inder"))
#print(name.startswith("H"))
#print(name.capitalize())
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
#A = "bhavya is sexy"
#c = A.replace ("sexy","awesome")
#print(c)
