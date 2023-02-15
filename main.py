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

def solve(s):
   res = ""
   cnt = 1
   for i in range(1, len(s)):
      if s[i - 1] == s[i]:
         cnt += 1
      else:
         res = res + s[i - 1]
         if cnt > 1:
            res += str(cnt)
         cnt = 1
   res = res + s[-1]
   if cnt > 1:
      res += str(cnt)
   return res

s = "aaabbbbbccccaacccbbbaaabbbaaa"
print(solve(s))

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


# Task 2: Prime Numbers


# Task 3: Fibonacci


