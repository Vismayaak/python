def anagram(a, b):
    if len(a) != len(b):
        print("not anagram")
    elif sorted(a)==sorted(b):
        print("are anagrams")
    else:
        print("not anagrams")
a= input("Enter a string: ")
b = input("Enter a string: ")
n=anagram(a,b)