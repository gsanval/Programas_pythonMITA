# Nos permite ejemplificara con conjuntos logicas

c1 = {1,2,3,4,5}
c2 = {5.6,7,8,9,10}
c3 = {9,10,11,12,13}
c4 = {3,4,5}

print(c1,c2,c3,c4)

print("\nUnion")
print("C1 union C3",c1.union(c2))
print("C1 union C3",c1 | c3)

print("\nInterseccion")
print("c1 interseccion c2", c1.intersection(c2))
print("c1 interseccion c3", c1 & c3)

print("\nDiferencia")
print("c1 difrencia c4", c1.difference(c4))
print("c2 diferecnia c3", c2 - c3)

print("\nDiferencia simentrica")
print("c1 dif simentrica c2", c1.symmetric_difference(c2))
print("c2 dif simentrica c3", c2 ^ c3)

print("\nComprobamos subconjuntos")
print("c4 es subconjnto c1", c4.issubset(c1))
print("c3 es subconjnto c2", c3 <= c2)

print("\nComprobar superconjunto")
print("c1 es superconjunto c4", c1.issuperset(c4))
print("c2 es superconjunto c3", c1 >= c3)

print("\nVerificar")
print("2 esta en c1", 2 in c1)
print("6 no esta en 1", 6 is not c1)

