nameOut = open('name.txt', 'w')
name = input('Please enter your name(This is not a scam): ')
print(name, file=nameOut)
nameOut.close()