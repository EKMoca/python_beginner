# Will an error occur if you try to access a list element equal to or 
# exceeding the length of the list?
foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error?

# This results in an error because sequential indexing starts at 0.
# Even though there are 3 elements, the third element is actually represented
# as element 2. or foo[2]