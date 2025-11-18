# sets and tuples and lists examples:

#sets use {}
#sets are not able to be duplicated or ordered

set1 ={1,2,3,4,5}
print(set1)
print(type(set1))
set1.add(6)
print(set1)
set1.remove(2)
print(set1)

# sets remove duplicate items in the array
set2 = {"apple", "banana", "cherry", "cherry"}
print(set2)

#tuples
tuple1 = (1,2,3,4,5)
print(tuple1)
print(type(tuple1))

# tuples are immutable, meaning they cannot be changed after creation
# this makes tuples useful for storing data that should not modified.

social_security_number = (123444,4444445,5676789)
print(social_security_number)