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

# OR
num = 13
def is_happy_num(num):
    if num == 1 or num == 7:
        return True

    Sum, x = num, num

    while Sum > 9:
        Sum = 0

if (is_happy_num(num)):
    print(num, "is a Happy number")
else:
    print(num, "is not a Happy number")


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

# OR
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

# OR (I like this one better :) )
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

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1