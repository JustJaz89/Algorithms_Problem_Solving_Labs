# Task 1
# INPUT: "Hello World"
# OUTPUT: "dlroW olleH"

# 0. Our Initial Function (from lecture)
def reverse_string(string):
    final_index = len(string) - 1
    string_reverse = ""
    # range(start, stop, increment)
    for index in range(final_index, -1, -1):
        string_reverse += string[index]
        # print(string[index])
        # string[4]
    print(string_reverse)

reverse_string("HaHaHa Hello World")

# H E L L O

# 1. Using Concatenation (-index)
    # Final letter in string has index -1
    # First letter in string has index - len(string)
def reverse_string_one(string):
    stopping_index = -len(string)
    index = -1
    while index >= stopping_index:
        string_reversed += string[index]
        index -= 1
    print(string_reversed)

reverse_string_one("HelloWorld")

# 2. Appending order
def reverse_string_two(string):
    reversed_string = ""
    for letter in string:
        reversed_string = letter + reversed_string
    print(reversed_string)

reverse_string_two("Banana")

# Task 2
# RACECAR --> Palindrome
# TACOCAT --> Palindrome

# User input
# Check for palidrome-ness
# IF it is a palindrome, let them know
# IF it is NOT a palindrome, let them know
# "12321"

# 1. Using reversed string method
def palindrome_checker():
    user_word = input("Please enter a word to check it it's a palindrome: ").lower
    reverse_user_word = reverse_string_two(user_word)
    # user_word.lower()
    # or user_word.upper()
    print(f"Your word is: {user_word}")
    print(f"And the reverse version is: {reverse_user_word}")
    if user_word == reverse_user_word:
        print("Congratulations, that's a palindrome! :)")
    else:
        print("Oh rats, that's not quite a palindrome...")

palindrome_checker()

# 2. Using the string itself (front & back)
# tacocat
# Walking through 1 letter at a time, forwards AND backwards
# Forwards will start with index 0, and go UP TO len(word) - 1
# Backwards will start with index -1, and go DOWN TO -len(word)
def palindrome_checker_two():
    user_word = input("Please enter a word to check if it's a palindrome: ").lower()
    halfway = int(len(user_word)/2)
    for i in range(halfway):
        # First and last letters are not equal
        # print(user_word[-1 - i])
        if user_word[i] != user_word[-1 - i]:
            print("Oh darn, that's not a palindrome!")
            return
    print("Congratulations! That's a palindrome! :) ")
# 0, 1, 2, 3
# -1, -2, -3, -4

palindrome_checker_two()