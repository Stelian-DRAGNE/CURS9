import random

numere = [random.randint(1, 49) for _ in range(6)]
print(numere)

numar_jucat = int(input("Introduceti un numar : "))
print(numar_jucat)

if numar_jucat in numere:
    print("Numarul jucat se afla in numerele extrase !")
else:
    print("Numarul jucat nu se afla in numerele extrase !")
