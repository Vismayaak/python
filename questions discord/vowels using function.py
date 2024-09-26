def count_vowels(s):
    vowels="aeiouAEIOU"
    a=0
    for char in s:
        if char in vowels:
            a=a+1
    return a
s="world"
print(count_vowels(s))