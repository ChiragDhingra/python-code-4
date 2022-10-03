# Creating an empty set 

b = set()
print(type(b))

# Adding the value to an empty set

b.add(2)
b.add(15)
b.add(15) # We can not add any repetative values because it will not change a set
b.add(1) 
b.add(33) 
b.add((15 , 2 , 9 , 15)) # We can add tuple to the set
# b.add({1:4}) # We can't add list and dictionary to the set
print(b)

# Length of the set
print(len(b)) # Print the length of the set 

# Removal of an Item
b.remove(1) # Remove the 1 from the set
# b.remove(12) # Throws an error as 12 is not present in the set
print(b)

print(b.pop()) # Pop any value from the set
print(b)       
b.clear()
print(b)