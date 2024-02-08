import random

numere = [random.randint(1, 49) for _ in range(6)]
numere_jucate = [int(input("Introduceti un numar :\n ")) for i in range(6)]
numere_comune = [nr for nr in numere_jucate if nr in numere]

print(numere_jucate)
print(numere)
print(numere_comune)

print("Categoria : ", 7 - len(numere_comune) if len(numere_comune) >= 3 else 0)