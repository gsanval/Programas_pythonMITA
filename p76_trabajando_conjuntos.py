# Trabjando conjuntos

muns = {"Zacatecas", "Guadalupe", "Jerez", "Fresnillo"}

print(muns,len(muns),type(muns))

for mun in muns:
    print(mun, end=" ")

muns.add("Teul")
print("\n",muns,len(muns))

muns.update({"Luis Moya", "Ojocaliente", "Tepetongo"})
print(muns,len(muns))

muns.remove("Zacatecas")
print(muns,len(muns))

muns.discard("Cañitas")
muns.discard("Ojocaliente")
print(muns,len(muns))

#print("Luis Moya" in muns)
if("Zacatecas" in muns):
    print("Si esta")
else:
    print("no esta")

print(muns.pop())
print(muns,len(muns))

muns.clear()
print(muns,len(muns))

