import random
def main():
    quickPicks = int(input('How many quick picks? '))
    randomGenerator(quickPicks)



def printList(list):
    listString = ''
    for number in list:
        listString = '{} {:>2s}'.format(listString, str(number))
    print(listString)


def randomGenerator(quickPicks):
    list = [0, 0]
    for i in range(0, quickPicks):
        while len(list) != len(set(list)):
            list = []
            list.append(random.randint(0, 45))
            list.append(random.randint(0, 45))
            list.append(random.randint(0, 45))
            list.append(random.randint(0, 45))
            list.append(random.randint(0, 45))
            list.append(random.randint(0, 45))
        printList(list)
        list = [0, 0]

main()