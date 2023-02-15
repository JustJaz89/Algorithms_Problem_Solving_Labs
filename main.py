# Algorithms & Problem Solving II
# Task 1: Reverse a String ("Welcome")
# Use a slice that steps backwards, -1
word = "Welcome"

reversed_word = ""

for index in range(len(word) -1, -1, -1):
    reversed_word += word[index]

print(reversed_word)

# OR
# Slice string, then print
word = "Welcome"[:: -1]
print(word)

# Task 2: Capitalize a Letter ("hello world" to "Hello World")
# string.title() is used for generating titles for strings
# Capitalize the first letter of every word and change the other letters to lowercase
s = "hello world"
print("Original string:")
print(s)
print("After capitalizing first letter:")
result = " ".join(elem.capitalize() for elem in s.split())
print(result)

#Or
# "capwords()" = a function that converts the first letter of every word into uppercase and every other letter into lowercase
# function needs to take the string as the parameter value and then return the string with the first letter capital

import string
s = "hello world"
print("Original string:")
print(s)
print("After capitalizing first letter:")
result = string.capwords(s)
print(result)

# Task 3: Palindrome ("level" or "racecar" or "taco cat" or "rotator")
# User input needs to check to see if your selected word is a Palindrome and has a positive result
# Palindrome needs to read the same backwards and forward

def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

s = "radar"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

# Task 4: Compress a string of characters ("aaabbbbbccccaacccbbbaaabbbaaa" to "3a5b4c2a3c3b3a3b3a")

# def solve(s):
#    res = ""
#    cnt = 1
#    for i in range(1, len(s)):
#       if s[i - 1] == s[i]:
#          cnt += 1
#       else:
#          res = res + s[i - 1]
#          if cnt > 1:
#             res += str(cnt)
#          cnt = 1
#    res = res + s[-1]
#    if cnt > 1:
#       res += str(cnt)
#    return res

# s = "aaabbbbbccccaacccbbbaaabbbaaa"
# print(solve(s))

# OR

def compress(my_string):
    index = 0
    compressed_string = " "
    string_len = len(my_string)
    while index != string_len:
        count = 1
        while (index < string_len-1) and (my_string[index] == my_string[index+1]):
            count = count + 1
            index = index + 1
        if count == 1:
            compressed_string += str(my_string[index])
        else:
            compressed_string += str(my_string[index]) + str(count)
        index = index + 1
    return compressed_string

my_string = "aaabbbbbccccaacccbbbaaabbbaaa"
print(compress(my_string))

# OR

string_one = ""
string_two = "aaabbbbbccccaacccbbbaaabbbaaa"
count = 1
for i in range(len(string_two)-1):
    if string_two[i] == string_two[i+1]:
        count = count + 1
    else:
        string_one = string_one + string_two[i] + str(count)
        count = 1
string_one = string_one + string_two[i+1] +str(count)
print(string_one)

# Algorithms & Problem Solving III
# Task 1: Happy Numbers
# Start with a positive integer, replace the number by the sum of the squares of its digits, and
# repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a
# cycle which does not include 1.

def is_happy_num(num):
    past = set()
    while num != 1:
        num = sum(int(i)**2 for i in str(num))
        if num in past:
            return False
        past.add(num)
    return(True)
print(is_happy_num(7))
print(is_happy_num(999))
print(is_happy_num(19))


# Task 2: Prime Numbers
# Check if a number is prime or not
# Take input from the user
# A prime number is a number that is only divisible by one and itself.
# Write a method that prints out all prime numbers between 1 and 100 


num = 19 #(19 is a prime number, 22 isn't a prime number)
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "*", num/i, "=", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than or equal to 1, it is not prime

# prime numbers between 1 and 100

# for num in range(1, 101):
#     status = True
#     if num < 2:
#         status = False
#     else:

def is_prime(num):
    status = True
    if num < 2:
        status = False
    else:
        for i in range(2, num):
            if num % i == 0:
                status = False
    return status

for num in range(1, 101):
    if is_prime(num):
        if num == 97:
            print(num)
        else:
            print(num, "", "")

# OR
# number_one = input("Input a number: ")
# number_two = input("Input another number: ")
number_one = 1
number_two = 101

for x in range(1, 101):
    prime = True
    for i in range(2, x):
        if (x % i == 0):
            prime = False
    if prime == True:
        print(x)

print("Completed")
    

# Task 3: Fibonacci
# a series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers

