# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5 #true
7 == 2 * 3 + 1 #true
8 != 8 #false
4 <= 2 + 2 #true

# Write 3 examples that result in True and 3 that result in False.

#true
5 >= 5
5 == 5
4 > 2
#false
2 > 3
2 == 4
2 != 3


# Create a simple grade-checking condition:

A_grade = '90'

# practice problem :
#1
# where a student must check if their score is greater than or equal to 60 to pass a test.

score = int(input("Enter your score: "))

if score >= 60:
    print("You passed the test!")
else:
    print("You did not pass the test bum")

#2
# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

password = input("Enter your password: ")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is valid")
else:
    print("password is invalid")