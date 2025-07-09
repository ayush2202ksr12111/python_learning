# how to play with strings in python

# we will add a name variable in python such that it should be name defined

name = 'youtube'

# now we will print one string which is inside the variable and one string that is inside  the name

print(name+' rocks')
#==================================================
# name = youtube

#  0   1  2  3  4  5   6
#  Y   O  U  T  U  B   E
# -7  -6 -5 -4 -3 -2  -1
#

# In python we use a variable index for accessing the index of variable and not only this a string can be treated as list by this function


# we access a index 0 element in python


print(name[0])

# now we access a index 6 element in python


print(name[6])

# if we access out of scope element we will get index out of scope error

#Uncomment it to test it
#print(name[8])

# if we try to access the element in negative iteration we will still we can acess it but it will start from the end of the list

print(name[-1])













