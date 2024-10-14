# Given the following list of numbers, remove all occurences of item 20

# Given a dictionary, calculate the sum of all items

'''
list1 = [5, 20, 15, 20, 25, 50, 20]
'''

list1 = [5, 20, 15, 20, 25, 50, 20]

# Remove all occurences of 20

list1 = [item for item in list1 if item != 20]

print ("New List: ", list1)


# Calculate the sum of the list 

sum_list = sum(list1)

# Print the sum of the list

print ("Sum of List: ", sum_list)
