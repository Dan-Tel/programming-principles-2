import re

# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
print(re.match(r"ab*", input()))

# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
print(re.match(r"ab{2,3}", input()))

# Write a Python program to find sequences of lowercase letters joined with a underscore.
print(re.match(r"([a-z]\_)+[a-z]", input()))

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
print(re.match(r"([A-Z][a-z]+)+", input()))

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
print(re.match(r"a[a-z]*b", input()))

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
print(re.sub(r"[ ,.]", ":", input()))

# Write a python program to convert snake case string to camel case string.
print("".join(x.capitalize() or "_" for x in input().split("_")))

# Write a Python program to split a string at uppercase letters.
print(re.split(r"[A-Z]", input()))

# Write a Python program to insert spaces between words starting with capital letters.
print(re.sub(r"([a-z])([A-Z])", r"\1 \2", input()))

# Write a Python program to convert a given camel case string to snake case.
print(re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", input()).lower())
