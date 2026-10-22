print("Program starting.")
num1 = int(input("\nInsert starting value: "))
num2 = int(input("Insert stopping value: "))

print("\nStarting while-loop: ")

while  True:
    print(num1, end=" ")
    num1 += 1
    if num1 > num2:
        break
print("\n\nProgram ending.")