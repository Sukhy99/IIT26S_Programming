print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

choice = input("Your choice: ")
if choice == "1":
    length = ("\n Length options: ")
    print("1 - Meters to Kilometers")
    print("2 - Kilometers to Meters")
    print("0 - Exit")
    
    length_choice = input("\nYour choice: ")
    if length_choice == "1":
        Meters = float(input("Enter length in meters: "))
        Kilometers = Meters / 1000
        print(f"{Meters} meters is equal to {Kilometers} kilometers")
    elif length_choice == "2":
        Kilometers = float(input("Enter length in kilometers: "))
        Meters = Kilometers * 1000
        print(f"{Kilometers} kilometers is equal to {Meters} meters")
    elif length_choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == "2":
    weight = ("\n Weight options: ")
    print("1 - Grams to Pounds")
    print("2 - Pounds to Grams")
    print("0 - Exit")
    weight_choice = input("Your choice: ")
    if weight_choice == "1":
        Grams = float(input("Enter weight in grams: "))
        Pounds = Grams / 453.592
        print(f"{Grams} grams is equal to {Pounds} pounds")
    elif weight_choice == "2":
        Pounds = float(input("Enter weight in pounds: "))
        Grams = Pounds * 453.592
        print(f"{Pounds} pounds is equal to {Grams} grams")
    elif weight_choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
        