list1 = [1,2,3]
list2 = [4,5,6]

nested_list = [list1,list2] #list inside of a list of lists

print(nested_list)
print(nested_list[1][2]) #first index references the list (list2) and then the second index references the number that you want in the list2

# video example

fruits = ['apples', 'orange', 'banana', 'coconut']
vegetables = ['celery', 'carrots', 'potatoes']
meats = ['chicken', 'fish', 'turkey']
#               0         1        2
groceries = [fruits, vegetables, meats]

print(groceries[1][2]) #potatoes
print(groceries[0][2]) #banana
print(groceries[2][2]) #turkey

for collection in groceries: #collection references each item (its a variable), groceries represents the list were going to loop through
    for food in collection: #nested loop
        print(food, end= " ")
    print() #space_


num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()


# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6
print(matrix[0][2])    # 3
print(matrix[0][0])    # 1
# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]

for row in matrix: #different lines but same thing
    print(row[0])


# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

matrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

# Print the first list.

print(matrix[0])

# Print the second item from the third list.

print(matrix[2][1])

# Use a list comprehension to extract the last item from each sub-list.

last_col = [row[2] for row in matrix]
print(last_col)

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension

squared_numbers = [x**2 for x in range (1,11)]
#or
# for x in range (1,11):
#     squared = x**2
#     print(squared)

print(squared_numbers)



