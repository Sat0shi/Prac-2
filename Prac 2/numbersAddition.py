numbersIn = open('numbers', 'r')
total = 0
for line in numbersIn:
    number = int(line)
    total += number
print(total)
numbersIn.close()