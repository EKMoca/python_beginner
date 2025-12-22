# What does the following code do and why?
print('5' + '10')
# Deceptively, it may look like an arithmetic operation returning an int value
# of 15. However, Since both data types are strings they are performing
# string concatenation which combines the two strings together to make:
print('510')