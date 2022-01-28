# reguli
# daca primul caracter si ultimul se repetau in cuvant, caracterul trebuie afisat
# restul caracterelor erau ascunse
# 7 sanse de a ghici
# word = o _ o _ _ _ o _ e e

word = "onomataopee"
# litera_cuvant = input("alege o litera: ")
# print(litera_cuvant)
lista_cuvant = []
for iterator in word:
    lista_cuvant.append("_")
    if iterator == word[0] or iterator == word [-1]:
        lista_cuvant[-1] = iterator
print(" ".join(lista_cuvant))
numar_incercari = 1
lista_litere_incercate = []
while numar_incercari <= 7:
    litera = input("Alege o litera: ")
    lista_litere_incercate.append(litera)
    if litera in word:
        for index, valoare in enumerate(word):
            print(index, valoare)
            if valoare == litera:
                lista_cuvant[index] = litera
        print("de adaugat in lista cuvant")
    else:
        lista_litere_incercate.append(litera)
        print("litera nu exista, deja ai f"incercat, urmatoarele litere:{",". join(lista litere incercate)}")
        print(f"mai ai {7 - numar incercari} incercari")
        if litera not in lista_numere_incercate:
             numar_incercari += 1
        if 8 - int(numar_incercari) == 0:
            print("ai pierdut! cuvantul era: {word}")
        elif "".join(lista_cuvant) == word:
            print("Ai castigat!")
        break
    else:
    print(" ".join(lista_cuvant))

