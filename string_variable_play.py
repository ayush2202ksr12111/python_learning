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

#=====================================================

# it will print the name in first

print(name[-7])

# we print from 0 to 1, it does not take 2nd index position 
# suppose we want to print the number in list such that 0 to 2

print(name[0:2])

# it will take 1, 2 , 3 index position but not 4 
# now we will try to print something else to test another to see whether it works or not

print(name[1:4])

# now we will try to print the whole letter except first string character

print(name[1:])


# now we will print like it will be into 10th index such that it starts from 3 will it print because we don,t have that much index in a string value

print(name[3:10])

# if we try to assign the value in string using the power of list will it work

# no it will throw the error that the value hasn,t been assigned

#name[0:3] = "my"

# what if we try to print the string variable with dynamically string value

print('my '+name[3:])












