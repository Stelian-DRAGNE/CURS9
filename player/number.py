import random

numere = [random.randint(1, 49) for _ in range(6)]
numere_jucate = [int(input("Introduceti un numar :\n ")) for i in range(6)]
numere_comune = [nr for nr in numere_jucate if nr in numere]

print(numere_jucate)
print(numere)
print(numere_comune)

categorii = {6:1, 5:2, 4:3, 3:4}
print("Categoria : ", categorii.get(len(numere_comune), 0))
print("Categoria : ", categorii[len(numere_comune)] if len(numere_comune) in categorii else 0)