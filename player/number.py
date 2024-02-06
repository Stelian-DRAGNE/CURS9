import random

numere = [random.randint(1, 49) for _ in range(6)]
print(numere)

numar_jucat = int(input("Introduceti un numar : "))
print(numar_jucat)

# if numar_jucat in numere:
#     print("Numarul jucat se afla in numerele extrase !")
# else:
#     print("Numarul jucat nu se afla in numerele extrase !")

lista_noua = []
for nr in numere:
    if nr == numar_jucat:
        lista_noua.append(nr)
if lista_noua:
    print("Numarul jucat se afla in numerele extrase !")
else:
    print("Numarul jucat nu se afla in numerele extrase !")