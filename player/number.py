import random

numere = [random.randint(1, 49) for _ in range(6)]

numere_jucate = []
for i in range(6):
    numar_jucat = int(input("Introduceti un numar : "))
    numere_jucate.append(numar_jucat)
print(numere_jucate)
print(numere)

numere_comune = []
for nr in numere_jucate:
    if nr in numere:
        numere_comune.append(nr)
print(numere_comune)

# for nr in numere:
#     if numar_jucat == nr:
#         print("Numarul jucat se afla in numerele extrase !")
#         break
# else:
#     print("Numarul jucat nu se afla in numerele extrase !")

# print(any([numar_jucat == nr for nr in numere]))