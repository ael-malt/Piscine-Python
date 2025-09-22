ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Start of my code
# print("Before: \n")
# print(ft_list)
# print(ft_tuple)
# print(ft_set)
# print(ft_dict)
# print("\n")


# List items are ordered, changeable, and allow duplicate values
ft_list[1] = "World!" 

# Tuples are immutable, convert to list first, modify, then convert back to tuple
ft_tuple_list = list(ft_tuple)
ft_tuple_list[1] = "France!"
ft_tuple = tuple(ft_tuple_list)

# Sets are unordered, unindexed, cannot be modified but we can remove and add elements and they do not allow duplicates (Sets WILL appear in a random order every time)
ft_set.remove("tutu!")
ft_set.add("Paris!")

# Dictionaries are ordered, changeable, and do not allow duplicates. Duplicate values will overwite existing values!
ft_dict["Hello"] = "42 Paris!"

# End of my code

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)