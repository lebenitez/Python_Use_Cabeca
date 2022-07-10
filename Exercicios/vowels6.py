vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to search for vowels: ")

found = {}

for letter in word:
      if letter in vowels:
            found.setdefault(letter, 0) #Método nativo que identifica se o valor existe, caso não exista ele já seta 1. É uma alternativa ao uso do if. 
            found[letter] += 1
            
for k, v in sorted(found.items()):
            print(k, 'was found', v, 'time(s).')

