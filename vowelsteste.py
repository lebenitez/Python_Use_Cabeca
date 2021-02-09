vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for letter in word:
      if letter in vowels:
            if letter not in found:
                  found.append(letter)
for vowel in found:
      print(vowel)
