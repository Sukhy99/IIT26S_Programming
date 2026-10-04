print("Program starting.")
print("insert two integers.")
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print("Comparing inserted integers.")
if num1 > num2:
    print("The first integer is greater than the second.")
elif num2 > num1:
    print("The second integer is greater than the first.")
else:
    print("Integers are same.")

print("\nAdding integers together.")
total = num1 + num2
print(f"{num1} + {num2} = {total}")

print("\nChecking the pairity of the sum....")
if total % 2 == 0:
        print("The sum is even.")
else:
        print("The sum is odd.")

        print("Program ending.")
