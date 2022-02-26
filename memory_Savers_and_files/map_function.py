# def adunare(n):
#     return n + n
#
lista_numere = [1, 2, 3, 4]
lista_numere2 = [5, 6, 7, 8]
# rezultat = map(adunare, lista_numere)
# print(list(rezultat))

rezultat = map(lambda n, m: n + m, lista_numere, lista_numere2)
print(list(rezultat))

# def adunare(lista_numere, lista_numere2):
#     suma = 0
#     lista_adunare = []
#     for i, v in enumerate(lista_numere):
#         for j, w in enumerate(lista_numere2):
#             lista_numere[i] + lista_numere2[j]
#             suma = v + w
#             if i == j:
#                 lista_adunare.append(suma)
#     return lista_adunare
# print(adunare(lista_numere, lista_numere2))