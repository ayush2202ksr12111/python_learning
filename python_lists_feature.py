# In python we have a feature of lists which will help insert number of lists in it

# we will define a variable that will define list of numbers to be added

# index    0    1   2   3
nums =   [25, 12, 36, 95]
# index   -4  -3  -2  -1 
 # suppose we want to display the whole numbers list array
 
print(nums)

#now suppose if we just want to print the single number at particular index this will print at index position 0 

print(nums[0])

# now suppose we want to print the number at index position 3

print(nums[3])

# now suppose we want to print the number list starting from index postion 1 till end

print(nums[1:])


#now suppose we want to print the number at index position -1 this will print the number from last position

print(nums[-1])

#+++++++++++++++++++++++++++++++++++++++++++++++++
# now we will use string feature here 

# we use names list that will contain multiple string variables


# index      0        1          2       3

names = [ 'naveen', 'Kiran' , 'John', 'Kailash' ]

# index     -4        -3        -2       -1 
 
# suppose we want to display the whole names list array
 
print(names)

#now suppose if we just want to print the single name at particular index this will print at index position 0 

print(names[0])



# now we want to print the number from first position by using the negative number for that we are going to use -4

print(nums[-4])

# now suppose we want to print the name from names list array at index position 3

print(names[3])

# now suppose we want to print the names list starting from index postion 1 till end

print(names[1:])


#now suppose we want to print the names at index position -1 this will print the names from last position

print(names[-1])

# now we want to print the names from first position by using the negative number for that we are going to use -4

print(names[-4])
# now we will follow same procedure as above

#+=======================================
# now we will use feature of  list where a number can be added we will use variable that will contain both numbers and string list 

num_name = [nums, names]
# this will contain list in nested loop
print(num_name)


# now we are going to use feature of append in list where we are going to append the list
nums.append(45)

# now we are again going to reprint the number array

print(nums)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
# now suppose we want to insert the number at index position 2 for that we are going to add it in list for that we are going to use insert feature in it

nums.insert(2,77)

print(nums)

# suppose now we want to remove the number form lists for that we are going to use remove feature of list in it just by deifning the number 

nums.remove(95)

print(nums)


#+++++++++++++++++++++++++++++++++++++
# now suppose we want to add feature of list which will remove the number from list for that we will use pop method pop method will automatically remove the element from index

nums.pop(1)

print(nums)

#+++++++++++++++++++++++++++++++++++++++++

# there is by default feature of pop that will be used in last in first out feature

# we will use lifo feature here which will by default pop the last element

# it will by default remove the last feature from the last stack
nums.pop()
print(nums)

# suppose you want to add the feature of list in which where you can add the feature that will display the new list will be deleted where we want it to be deleted

del nums[2:]

print(nums)



























































