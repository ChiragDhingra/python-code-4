myDict = {
    "pankha":"Fan",
    "bandhar":"Monkey",
    "daba":"box",
    "vastu":"item",
    "ghar":"Home",
    "rasta":"Way",
}
print("The options are ",myDict.keys())
a = input("Enter the hindi word\n")
# print("The meaning of the word is", myDict[a] )
print("The meaning of the word is :", myDict.get(a) )