print("Program starting")
starting_value = int(input("\nInsert starting point: "))
stopping_value = int(input("Insert stopping point: "))
inspection_value = int(input("Insert inspection point: "))

if starting_value >= stopping_value:
    print("Starting value must be less than stopping value.")
if not (starting_value <= stopping_value <= inspection_value): 
    print("Inspection value must be within the range of starting and stopping values.")
    if (starting_value < stopping_value) and (starting_value <= inspection_value <= stopping_value):
        print("\nFirst loop - inspection with break: ")
        for i  in range (starting_value, inspection_value):
            if i == inspection_value:
                break
            print(i, end=" ")
        print(f"\nSecond loop - inspection with continue: ")
        for i in range(starting_value, stopping_value):
                if i == inspection_value:
                     continue
                print(i, end=" ")
                
print("\n\nProgram ending.")
              