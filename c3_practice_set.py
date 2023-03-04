# display a user entered name followed by good afternoon using input function
# a="Good afternoon,"
# b=input("enter your name\n")
# print(a+b)

# WAP to fill in a letter template given below with name and date?
# name=input("enter your name\n")
# date=input("enter date\n")
# letter='''Dear <|NAME|>
# you are selected!

# <|DATE|>
# '''
# letter=letter.replace("<|NAME|>",name)
# letter=letter.replace("<|DATE|>",date)
# print(letter)

# WAP to find double space in a string
# st="this is a string with  double  spaces"
# find=st.find("  ")
# print(find)

# replace the double space from problem 3 with single spaces
st="this is a string with    double spaces"
# find=st.find("  ")
re_st=st.replace("  "," ")
# print(find)
print(re_st)

# WAP to format the following letter using escape sequence character

letter ="Dear Harry,this python course is nice. thanks!"
print(letter)
formatted_letter ="Dear Harry,\n\tthis python course is nice.\nthanks!"
print(formatted_letter)

