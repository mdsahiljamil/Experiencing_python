myDict={
    "fast":"in a quick manner",
    "sahil":"A coder",
    "marks":"10,20,30",
    1:2
    
}
# methods of dictionary
print(list(myDict.keys())) # print the keys of the dictionary
print(list(myDict.values())) # print the values of the dictionary
print(myDict.items()) # print the (keys,values) of the dictionary

newDict={
    "unknown":"love",
    "sahil":"A dancer" # it will change all sahil values to A dancer instead of coder
}
myDict.update(newDict) # update the dictionary by adding the key value of the newDict to myDict
# myDict.update({"keys":"value"}) # another method
print(myDict)
print(newDict)

print(myDict.get("sahil")) # this will print the value of sahil
print(myDict["sahil"]) # this will print the value of sahil

# print(myDict.get("sahil2")) # it print none
# print(myDict["sahil2"]) # it will throw an error
 