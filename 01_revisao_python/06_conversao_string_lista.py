s='python'
#converter uma string em lista

print("String:")
print(s)
print(type(s))

print("Lista:")
l = list(s)
print(l)
print(type(l))
l[1]='i'
print("Lista com alteração via atribuição")
print(l)

#como converter de uma lista para uma string
print("Refiz a string pela lista")
w=''
w = w.join(l)
print(w)
print(type(w))
