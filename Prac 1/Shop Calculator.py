totalCost = 0
i = float(input("Number of items: "))
numberOfItems = i
while numberOfItems < 1:
    print("Invalid number of items!")
    i = float(input("Number of items: "))
    numberOfItems = i
while i > 0:
    itemCost = float(input("Price of item: "))
    totalCost = totalCost + itemCost
    i = i -1
print("Total price for {}".format(numberOfItems) + " items is ${:.2f}".format(totalCost))