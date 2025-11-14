# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

#collections are used to store multipe items in a single variable
#lists are order collections of items
# lists are mutable, meaning you can change their content
# lists are created using square brackets []

my_list = [1,2,3,4,5]
print(my_list) # [1,2,3,4,5]
print(type(my_list)) # <class 'list'

print(my_list[0])
print(my_list[1:4])
print(my_list[0:])

#to add items to a list use .append() and or .extend()

my_list.append(6) #singular values
print(my_list)

my_list.extend([7, 8]) #multiple values
print(my_list)

my_list.extend(list(range(5,515))) #mutliple values with a scope of numbers
print(my_list)

my_list.extend(list(range(600, 1000))) #example
print(my_list)


#instead of creating a whole bunch of seperate variables, you can instead put all those variables in a list so that you can access them later.
# efficient for objects that are similar
# you can change all those objects all at once
# makes our job easier


# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

favorite_food_list = ["Pizza","Tacos","Pasta","Cookies","Bannanas"]

# Print the second and last item.

print(favorite_food_list[1::-1])

# Add a new item using .append().

favorite_food_list.append("67")
print(favorite_food_list)

# Remove the first item using .pop(0).

favorite_food_list.pop(0)
print(favorite_food_list)

# Reverse your list using .reverse().

favorite_food_list.reverse()
print(favorite_food_list)

# Create a list of 3 lists (matrix), and access the middle element.

