# 1
# String Basics and Slicing
# Create a program that extracts the first 5 characters from a given string.
# Extract the last 3 characters of a string using slicing.
# Write a program to print every second character from a string.
# Reverse a given string using slicing and print the result.
# Replace all occurrences of a specific character with another character in a string.


# input_string = input("Enter a string: ")

# first_5_chars = input_string[:5]
# print(f"The first 5 characters are: {first_5_chars}")

# last_3_chars = input_string[-3:]
# print(f"The last 3 characters are: {last_3_chars}")

# every_second_char = input_string[::2]
# print(f"Every second character is: {every_second_char}")

# reversed_string = input_string[::-1]
# print(f"The reversed string is: {reversed_string}")

# old_char = input("Enter the character to replace: ")
# new_char = input("Enter the new character: ")
# replaced_string = input_string.replace(old_char, new_char)
# print(f"The string after replacement is: {replaced_string}")



# 2
# Write a program to print a formatted message like: "Hello, my name is James and I am 20 years old." using f-strings

# name = "Neuer"
# age = 25

# print(f"Hello, my name is {name} and I am {age} years old.")




# 3
# Create a program to format and print a float with 2 decimal places.

# float_num = float(input("Enter a float number: "))

# print(f"The number with 2 decimal places is: {float_num:.2f}")



# 4
# Write a program to convert all characters in a string to uppercase and then to lowercase.

# input_string = input("Enter a string: ")

# uppercase_string = input_string.upper()

# lowercase_string = input_string.lower()

# print(f"Uppercase: {uppercase_string}")
# print(f"Lowercase: {lowercase_string}")



# 5
# Create a program to count the number of occurrences of a specific character in a string.

# string = input("Enter a string: ")

# char_to_count = input("Enter the character to count: ")

# occurrences = string.count(char_to_count)

# print(f"The character '{char_to_count}' appears {occurrences} times in the string.")




# 6
# Write a program to concatenate two strings with a space in between.

# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")


# result = string1 + " " + string2

# print(f"The concatenated string is: {result}")



# 7
# Create a program to find the sum of the first and last digit of a given number.

# num = input("Enter a number: ")

# first_digit = int(num[0])
# last_digit = int(num[-1])

# sum_digits = first_digit + last_digit

# print(f"The sum of the first and last digits is: {sum_digits}")



# 8
# Write a program to calculate the average of 3 float numbers and format the result to 3 decimal places.


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# average = (num1 + num2 + num3) / 3

# print(f"The average of the numbers is: {average:.3f}")




# 9
# Create a program that takes a string input and an integer input and repeats the string that many times.


# input_string = input("Enter a string: ")
# repeat_count = int(input("Enter the number of times to repeat the string: "))

# repeated_string = input_string * repeat_count

# print(f"The repeated string is: {repeated_string}")



# 10
# Ask the user to enter a string, and then print the string in reverse order.

# input_string = input("Enter a string: ")

# reversed_string = input_string[::-1]

# print(f"The reversed string is: {reversed_string}")



# 11
# Count how many vowels are in the string and print the count.

# input_string = input("Enter a string: ")

# vowels = "aeiouAEIOU"

# vowel_count = 0

# for char in input_string:
#     if char in vowels:
#         vowel_count += 1


# print(f"The number of vowels in the string is: {vowel_count}")



# 12
# Write a program that takes a string as input and outputs the longest substring without repeating characters. For example, the string "abcabcbb" should return "abc".


# def longest_substring(s):
#     left, max_substr = 0, ""
#     char_set = set()

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_substr = max(max_substr, s[left:right+1], key=len)

#     return max_substr


# print(longest_substring(input("Enter a string: ")))




# 13
# Write a program using a while loop that repeatedly asks the user to input a number until they input 0, then print the sum of all entered numbers.


# total_sum = 0

# while True:
#     number = int(input("Enter a number (or 0 to stop): "))
    
#     if number == 0:
#         break  
    
#     total_sum += number 

# print(f"The sum of all entered numbers is: {total_sum}")



# 14
# Create a list of 10 numbers (hardcoded) and calculate the sum of all numbers in the list.

# ls=[1,2,3,4,5,6,7,8,9,10]
# total=0
# for numbers in ls:
#     total +=numbers
# print("The sum of the numbers is:", total) 


# 15
# Հայտարարել list, և տպել list-ի էլեմենտներից առավելագույնի արժեքը: List-ը պետք է պարունակի միայն int տիպի արժեքներ: Չօգտագործել max ֆունկցիան:

# ls=[1,2,6,9,22]
# max_ls=ls[0]
# for i in ls:
#     if i>max_ls:
#         max_ls=i
# print("the max value is:", max_ls)



# 16
# Հայտարարել list և տպել նվազագույն արժեքով էլեմենտի ինդեքսը։


# ls=[]
# n=int(input("Enter a number for size:"))
# index_min=0

# for i in range(n):
#     list.append(int(input(f'Enter a{i+1} number for list:')))
#     if list[i]<list[index_min]:
#         index_min=i
# print(f"list->{list}, min index={index_min}")

#  second variat 2

# ls=[3,6,8,7,2]
# min_value=ls[0]
# min_index=0

# for i in range(1,len(ls)):
#     if ls[i]<min_value:
#         min_value =ls[i]
#         min_index=i

# print(f"The min value is {min_value} at index {min_index}") 



# 17
# Հայտարարել  երկու ամբողջ թվային արժեքներով list- եր  և տպել համապատասխանող ինդեքսներով էլեմնետների արտադրյալը էկրանին

# ls1=[2,5,8,9,6]
# ls2=[2,6,8,9,3]
# for i in range(len(ls1)):
#     print(ls1[i]*ls2[i],"")



# 18
# Գրել ծրագիր, որը ստանում է ամբողջ թիվ։ Հայտարարել list: Եթե list-ում առկա է տրված թիվը տպել YES, հակառակ դեպքում տպել NO։ 

# ls=[1,2,3,4,5]
# num=int(input("Please enter the searching number"))

# for i in ls:
#     if (i==num):
#         print("yes")
#         break
#     else:
#         print("no")



# 19
# Հայտարարել list,  որը բաղկացած է string-ներից: Տպել թե քանի անգամ է յուրաքանչյուրը հանդիպում list-ում:

# ls=['hello','world', 'hello', 'barev', 'world']
# for i in range(len(ls)):
#     if ls[:i].count(ls[i]):
#        continue
#     k=ls.count(ls[i])
#     print(f'{ls[i]}:{k}')