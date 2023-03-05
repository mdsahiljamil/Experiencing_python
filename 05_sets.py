# sets in python
# sets represent the values of set in increasing manner and dont repeat
a={1,5,2,4,3,6,2,2,1}
print(a)
print(type(a))  # show set type

b={}
print(b)
print(type(b)) # show dictionary type

# for empty set :
c=set()
print(c)
print(type(c))
c.add(2)
c.add(6)
c.add(5)
c.add(9)
c.add(3)
# c.add([4,5,6]) # we can't add list in set and also u can't enter a dictionary
c.add ((7,8,9)) # we can add a tuple in a tuple
print(c)

# method of sets
'''
print(len(a)) # it will print the length of a set
print(len(b))
print(len(c))
'''

c.remove(6) # it will remove an elements from set (6)
print(c)


print(c.pop()) # removes an arbitrary element from the set and returns the element removed
print(c)

# c.clear() # it remove all the elements from a list
 
# there are 2 more method regrading union and intersection
 
'''
c.union({8,11})
c.intersection({8,11})
'''