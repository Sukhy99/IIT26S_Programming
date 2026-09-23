print("Program starting.")
Compound_word = input("Insert a closed compound word: ")
Length = len(Compound_word)
Last_charecter = Compound_word[-1]
Reversed_word = Compound_word[::-1]
print(f"The word you inserted is '{Compound_word}' and in reverse it is '{Reversed_word}'.")
print(f"The inserted word length is {Length}.")
print(f"The last charecter is {Last_charecter}.\n")
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
print(" ")
substracting = Compound_word[start:end:step]
print(f"The word '{Compound_word}' sliced to the defined substring is '{substracting}'.")
print("Program ending.")
