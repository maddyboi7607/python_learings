

word = input("Enter a word: ")

if len(word) % 3 == 0:
    print(word[::-1])  

elif len(word) % 2 == 0:
    print(word.upper())  

else:
    print(word.lower()) 




