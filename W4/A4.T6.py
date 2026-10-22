print("Program starting.")
n = int(input("Insert a positive intenger: "))

count = 0

while n != 1:
    print(n, end=" -> ")

    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1

    count += 1

print(1)
print(f"Sequence had {count} total steps.")
print("\nProgram ending.")