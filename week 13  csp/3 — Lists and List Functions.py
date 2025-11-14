# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

#collections are used to store multipe items in a single variable
#lists are order collections of items
# lists are mutable, meaning you can change their content
# lists are created using square brackets []

#instead of creating a whole bunch of seperate variables, you can instead put all those variables in a list so that you can access them later.
# efficient for objects that are similar
# you can change all those objects all at once
# makes our job easier


# my_list = [1,2,3,4,5]
# print(my_list) # [1,2,3,4,5]
# print(type(my_list)) # <class 'list'

# print(my_list[0])
# print(my_list[1:4])
# print(my_list[0:])

# #to add items to a list use .append() and or .extend()

# my_list.append(6) #singular values
# print(my_list)

# my_list.extend([7, 8]) #multiple values
# print(my_list)

# my_list.extend(list(range(5,515))) #mutliple values with a scope of numbers
# print(my_list)

# my_list.extend(list(range(600, 1000))) #example
# print(my_list)

#-----

new_list = ['a','b','c']
print(new_list)
new_list.append('d')
print(new_list)

#removing an item from the list at the end by default
removed_item = new_list.pop()

print(removed_item)
print(new_list)
#removes the first item from the list 
removed_second_item = new_list.pop(1)
print(removed_second_item)
print(new_list)
#sorts items

numbers = [4,2,5,1,3]
numbers.sort()
print(numbers)

#reverses list

numbers.reverse()
print(numbers)

#inserts items into specific position

numbers.insert(2,10)
print(numbers)

# replaces values inside the list with other values
third_list = [7,8,9]
third_list[0] = 6
print(third_list)
third_list[-1] = 10
print(third_list)

#prints a list of 10 random values ranging from 1 to 100 
import random

random_list = random.sample(range(1,1000), 100)
print(random_list)
print(sorted(random_list))

sorted_list = sorted(random_list)
print(sorted_list)

#removes every third value in the list

list = sorted_list.reverse
list.pop(3)
print(list)

#summary of list functions
# .append(item) - adds an item to the end of the list
# .pop(index) - removes and returns the item at the specificed index
# .sort() - sorts the list in asecending order
# .reverse() - reverses the order of the list



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

