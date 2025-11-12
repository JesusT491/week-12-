# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True


#score calculator
score = int(input("Enter your score (0-100):"))
# if score is between 90 and 100
#assign grade A

if 90 <= score <= 100:
    print("Grade: A")

# if score is between 80 and 89
# assign grade b

elif 80 <= score < 90:
    print("Grade: B")

# if score is between 70 and 79
# assign grade c

elif 70 <= score < 79:
    print("Grade: C")

#if score is between 60 and 69
# assign grade D

elif 60 <= score < 69:
    print("Grade: D")

#if score is below 60
# Assign F lmfao

else:
    print("Grade: F")



# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive)

x = int(input("Enter a number: "))
print(50 <= x <= 100)

# number = 70
# if 50 > number <= 100:
#     print("yes it does")
# else:
#     print("you sold")

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.

y = int(input("Enter another number for challenge 2: "))
print(0 != y > 10)

# if 5 != 0 and 5 > 10:
#     print(True)

# Use chained comparison to check if 3 < 4 < 5.

print (3 < 4 < 5)

if 3 < 4:
    if 4 < 5:
        print('chained ifs expression')

# Challenge: Create a password rule using logical operators:

password_challenge = input("Create your password: ")

if len(password_challenge) <= 5:
    print("incorrect password size")