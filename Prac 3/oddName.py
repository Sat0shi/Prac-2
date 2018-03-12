'''
A
s
h
t
o
n
W
e
s
t
o
n
'''
isValid = False

name = input('Please enter your name: ')
while isValid == False:
    if len(name) < 1:
        name = input('Please enter a valid name: ')
    else:
       print(name[::2])
       isValid = True