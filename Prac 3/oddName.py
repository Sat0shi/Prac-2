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
def main():
    isValid = False
    name = getName()

    while isValid == False:
        if len(name) < 1:
            name = getName()
        else:
           printName(name)
           isValid = True

def getName():
    name = input('Please enter your name: ')
    return name

def printName(name):
    skipLength = input("Please enter a number for how many letters you would like skipped: ")
    print(name[::int(skipLength)])
main()