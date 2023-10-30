nom1 = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
nom2 = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print(nom1,nom2)

print("\nUnion")
print("nom1 union nom2",nom1 | nom2)

print("\nInterseccion")
print("nom1 interseccion nom2", nom1 & nom2)

print("\nDiferencia")
print("nom1 diferecnia nom2", nom1 - nom2)

print("\nDiferencia simentrica")
print("nom1 dif simentrica nom2", nom1 ^ nom2)

print("\nComprobamos subconjuntos")
print("nom1 es subconjnto nom2", nom1.issubset(nom2))

print("\nComprobar superconjunto")
print("nom1 es superconjunto nom2", nom1.issuperset(nom2))

print("\nVerificar")
print("Pedro esta en nom1", "Pedro" in nom1)
print("Lilia no esta en nom2", "Lilia" is not nom2)