
muni = {"Apozol" : 1863, "Calera" : 1868, "Fresnillo" : 1554, "Guadalupe" : 1821, "Jalpa" : 1824, "Jerez" : 1824, "Loreto" : 1931,
"Mazapil" : 1824, "Momax" : 1857}

print(f"\nDiccionario original: \n {muni}")

del muni["Apozol"]
muni.pop("Fresnillo")
muni.popitem()
print(f"\nDiccionario modificado: \n {muni}")
muni.clear()
print(f"\nDiccionario modificado: \n {muni}")

