score = float(input("Enter score: "))
while score >= 0 and score <= 100:
    if score > 90:
        print("Excellent")
    elif score < 50:
        print("Bad")
    else:
        print("Passable")
    score = float(input("Enter score: "))