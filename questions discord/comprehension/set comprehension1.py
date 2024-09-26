string =input("Enter a string:")
vowels = {'a', 'e', 'i', 'o', 'u'}
unique_vowels = {char for char in string.lower() if char in vowels}
print(unique_vowels)
