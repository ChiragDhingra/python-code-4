mydict = {
     "chirag":"Is a good boy",
     "marks":[99 , 94 , 98 , 92 ],
     "fast":"Quick",
 }
print(mydict.keys()) # Print the keys of the Dictionary

#or

# print(list(mydict.keys()))

print(mydict.values()) # Print the values of the Dictionary

print(mydict)

updateDict = {

    "chirag":"Is a coder",

    "marks":[99 , 98 , 100 ,99.5],
}
mydict.update(updateDict) # Update the Dictiionary by adding the keys-values pair from updateDict

print(mydict)

print(mydict.items())

print(mydict.get("marks")) 

print(mydict["chirag"])

print(mydict.get("marks")) # Print value associated with key chirag

# print(mydict["chirag"])  # Print value associated with key chirag

# The Difference between .get and [] syntax in Dictionaries

# print(mydict.get("marks2")) # It will not throw an error it will show none instant of error

# print(mydict["chirag2"]) # Throw an error as chirag2 is not in the dictionary





