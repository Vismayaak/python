numbers=[15,22,37,44,56,63,72,89]
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Number of even numbers:",even_count)
print("Numbers of odd numbers:",odd_count)