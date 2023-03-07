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
'''
set={18,"18"}
print(type(set))
print(set)
'''

# what will be the length of the following set s:
'''
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
'''

# what is the type of s ?
'''
s={}
print(type(s))
'''

# create an empty dictionary allow 4 friends to enter their favourite language as value and use keys as their name , Assume that the names are unique
'''
Dict1={}

a=input("enter your fav language\n")
b=input("enter your fav language\n")
c=input("enter your fav language\n")
d=input("enter your fav language\n")
Dict1['sahil']= a
Dict1['sadik']= b
Dict1['saklen']= c
Dict1['sufiyan']= d

print(Dict1)
'''

# if names of 2 friends are same what will happen to the program in problem 6 ?
'''
Dict1['sahil']= a
Dict1['sadik']= b
Dict1['sahil']= c # it will takes the values of the latest value enter
Dict1['sufiyan']= d
'''

# if language of 2 friends are same what will happen to the program in problem 6 ?
# answer , no problem will display

# can you change the values inside a list which is contained in set s ?

#s ={8,7,12,"sahil"[1,2]} # question was wrong because list can't be stored in a set
