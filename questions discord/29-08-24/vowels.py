vowel=input("enter a character: ")
if len(vowel)!=1:
    print("enter single character")
else:
    vowel=vowel.lower()
    vowels='aeiou'
    if vowel in vowels:
        print("it is a vowel")
    else:
        print("it is a consonant")
    
       
    