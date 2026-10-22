print("Program starting")

print("\nCheck multiplicative persistence.")

n = int(input("Insert an intenger: "))
count = 0

while n >= 10:
    temp = n
    product = 1
    line = ""

    while temp > 0:
        digit = temp % 10
        product *= digit
        line += str(digit) + (" * " + line if line else "")
        temp //= 10
line = line.rstrip(" * ")
print(line + " = " + str(product))

n = product
count += 1

print("No more steps.")

print("\nThis program took", count, "step(s)")

print("\nProgram ending.")