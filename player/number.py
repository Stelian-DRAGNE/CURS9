import random

numere = [random.randint(1, 49) for _ in range(6)]
numere_jucate = [int(input("Introduceti un numar :\n")) for i in range(6)]
numere_comune = [nr for nr in numere_jucate if nr in numere]

print(numere_jucate)
print(numere)
print(numere_comune)

print("Categoria : ", 7 - len(numere_comune) if len(numere_comune) >= 3 else 0)

# for nr in numere:
#     if nr not in range(1, 50):
#         print(f" {nr} nu se afla in range.")
#         break
# else:
#     print("Toate numerele se afla intre 1 si 49")

print(all([nr in range(1, 50) for nr in numere]))
print(all([nr in range(1, 50) for nr in numere_jucate]))

## Verificam daca numerele sunt unice
print(len(numere) == len(set(numere)))
print(len(numere_jucate) == len(set(numere_jucate)))