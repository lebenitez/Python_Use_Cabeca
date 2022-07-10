vowels = {'a', 'e', 'i', 'o', 'u'}
# uma outra opção para a linha acima seria vowels = set('aeiou')

word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
print(found)
