# conditional statement
# if-elif-else ladder in python
''''
a=45
if(a<10):
    print("The value of a is greater than 10")
elif(a>20):
    print("The value of a is greater than 20")
else:        
    print("The value of a is not greater than 10 and 20")
    
print("done!") 
'''
# if statement
'''   
if(a>10):
    print("The value of a is greater than 10")
if(a>30):
    print("The value of a is greater than 20")
    
if(a>20):
    print("The value of a is greater than 20")
else:        
    print("The value of a is not greater than 10 and 20")
'''    
# WAP to print "yes" when the age entered by the user is greater than or equal 18    

age=int(input("Enter your age\n"))
if(age>=18)and(age<=99):    # or we can write (age>=18 and age<=99): both will work
    print("yes")
else:
    print("no")    