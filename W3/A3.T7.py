print("Program starting.")
print("Testing decision structures.")
Value = int(input("Insert an integer: "))
print("options: ")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    print("Using one multi-branched decision structure.")
    if Value >= 400:
        Value = Value + 44
    elif Value >= 200:
        Value = Value + 22
    elif Value >= Value:
        Value = Value + 11
        print("Result is", Value)
elif choice == 2:
    print("Using multiple independent if-statements.")
    if Value >= 400:
        Value = Value + 44
    if Value >= 200:
        Value = Value + 22
    if Value >= 100:
        Value = Value + 11
        print("Result is", Value)
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")


