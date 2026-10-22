print("Program starting.")
Word = input("Insert word (empty stops): ")
Word_Count = 0
Char_Count = 0

while Word != "":
    Word_Count += 1
    Char_Count += len(Word)
    Word = input("Inser word (empty stops): ")
print("You inserted:")
print(f"-{Word_Count} words")
print(f"-{Char_Count} characters")
print("\nProgram ending.")
