print("Program starting.")
print("String comparisons")
First_word = input("Insert first word: ")
Charecter = input("Insert a character: ")
if Charecter in First_word:
    print(f'"{First_word}" conatains charecter "{Charecter}"')
else:
    print(f'"{First_word}" doese not contains charecter "{Charecter}"')

Second_word = input("Insert second word: ")
if First_word < Second_word:
    print(f'The first word "{First_word}" is before the second word "{Second_word}" alphabetically.')
elif Second_word < First_word:
    print(f'The second word "{Second_word}" is before the first word "{First_word}" alphabetically.')
else:
    print(f'Both inserted words are the same alphabetically, "{First_word}"')
    print("Program ending") 