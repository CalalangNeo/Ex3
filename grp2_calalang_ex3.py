# A program for you calculate the length of a string.

input_string = "Calalang, Nea B."
print("The length of the string is:", len(input_string))

#  A program count the number of characters in a string.

input_string = input("Enter a string: ")
character_count = len(input_string)
print("The number of characters in the string is:", character_count)

#  A program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

input_string = input("Enter a string: ")
modified_string = input_string[0] + input_string[1:].replace(input_string[0], '$')
print("The modified string is:", modified_string)

#  A program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) > 1 and len(str2) > 1:
    str1 = str1[1] + str1[0] + str1[2:]
    str2 = str2[1] + str2[0] + str2[2:]

print("The result is:", str1 + " " + str2)

# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces

str1 = "Calalang"
str2 = "Nea"
str3 = "B."
str4 = "BSCS 3G"

result = str1 + " " + str2 + " " + str3 + " " + str4
print("The result is:", result)

# Using + Concatenate Strings in Python get two strings from user input and concatenate them

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + " " + str2
print("The result is:", result)

# Using + Concatenate in Python using your name and your age in a paragraph

name = "Calalang, Neo B."
age = "21 years old."

paragraph = "My name is " + name + " and I am " + age + "."
print(paragraph)
