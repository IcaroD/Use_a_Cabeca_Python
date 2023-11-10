vowels = set('aeiou')
word = input("Write a word: ") 
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)

        
