print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")
name = input("Before the menu, please insert your name: ")
print("\nOptions")
print("1 - Print Welcome message")
print("2 - Exit")

choice = input("Your choice: ")
if choice == "1":
    print(f"Welcome {name}!")
elif choice == "2":
    print("Unknown option.")
else:
    print("Exiting.")

print("\nProgram ending.")