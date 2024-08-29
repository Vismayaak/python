tuple_elements=('a','b','c','d')
list_elements=list(tuple_elements)
list_elements[1]='z'
new_tuple=tuple(list_elements)
print(new_tuple)