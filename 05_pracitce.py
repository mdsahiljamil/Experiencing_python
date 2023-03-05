# WAP tp create a dictionary of hindi words with values as their english translation provide user with an option to look it up!
'''
Dict={
    "kalam":" A pen",
    "pustak":" The book",
    "pani":" water",
}
print("options are",Dict.keys())
a=input("Enter the hindi word\n")
# print("the value of the key is:",Dict[a])
print("the value of the key is:",Dict.get(a)) # if user input wrong input then,this will not show an error
'''

#WAP to input eight number from the user and display all the unique number(once)
'''
a=int(input("enter a 1st number\n"))
b=int(input("enter a 2nd number\n"))
c=int(input("enter a 3th number\n"))
d=int(input("enter a 4th number\n"))
e=int(input("enter a 5th number\n"))
f=int(input("enter a 6th number\n"))
g=int(input("enter a 7th number\n"))
h=int(input("enter a 8th number\n"))

print(a,b,c,d,e,f,g,h)
list={a,b,c,d,e,f,g,h}
print(list)
'''

# can we have a set with 18(int) and "18"(str) as a values in it ?

set={18,"18"}
print(type(set))
print(set)