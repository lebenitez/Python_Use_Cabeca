vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Provide a word to search for vowels: ")

found = {}

for letter in word:
      if letter in vowels:
            if letter in found: #Criei este if por conta própria e funcionou :-)
                  found[letter] += 1
            else:
                  found[letter] = 1
            
for k, v in sorted(found.items()):
            print(k, 'was found', v, 'time(s).')

