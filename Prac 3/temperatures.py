"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsiusInput = float(input("Celsius: "))
            print("Result: {:.2f} F".format(celsius(celsiusInput)))
        elif choice == "F":
            farenheitInput = float(input("Farenheit: "))
            print("Result: {:.2f} F".format(farenheit(farenheitInput)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius(celsiusInput):

    fahrenheit = celsiusInput * 9.0 / 5 + 32
    return fahrenheit

def farenheit(farenheitInput):

    celsius = (farenheitInput - 32) * 5 / 9
    return celsius


main()