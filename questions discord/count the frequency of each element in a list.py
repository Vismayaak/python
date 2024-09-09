element=input("Enter elements in a list")
string_elements=element.split()
elements=[]
for i in string_elements:
    elements.append(int(i))
frequency={}
for j in elements:
    if j in frequency:
        frequency[j]+=1
    else:
        frequency[j]=1
print("frequency of each element in the list:")
for element in frequency:
    print(f"{element}:{frequency[element]}")