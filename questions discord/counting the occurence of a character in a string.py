user=input("Enter a string:")
char_count=input("Enter the character to count:")
count=0
if len(char_count)!=1:
    print("Please enter only one character")
else:
    for i  in user:
        if i==char_count:
         count=count+1
print(f" ",count)