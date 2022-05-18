import random
msg = ""
lista = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def joc():
    intrebare = input('Do you want to start the game? "y/n" ')
    if intrebare == "y":
        valoare_utilizator = int(input("Write a number between 1 and 9"))
        if lista[valoare_utilizator-1] == "-":
            lista[valoare_utilizator-1] = '[X]'

    while "-" in lista:

        if lista[4] == "-":
            lista[4] = "[0]"
        elif lista[0] == "-":
            lista[0] = "[0]"
        elif lista[2] == "-":
            lista[2] = "[0]"
        elif lista[6] == "-":
            lista[6] = "[0]"
        elif lista[8] == "-":
            lista[8] = "[0]"
        else:
            ramas = [1, 3, 5, 7]
            computer_choice = random.choice(ramas)
            while computer_choice not in ramas:
                lista[computer_choice] = "[0]"
                break
        print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{}".
              format(lista[0], lista[1], lista[2], lista[3],
                     lista[4], lista[5], lista[6], lista[7], lista[8]))

        valoare_utilizator = int(input("Write a number between 1 and 9 "))
        if lista[valoare_utilizator - 1] == "-":
            lista[valoare_utilizator - 1] = '[X]'


def rezultat():
    joc()
    if (lista[0] == lista[1] == lista[2] and lista[0] != "-" and lista[0] == '[X]')\
        or (lista[3] == lista[4] == lista[5] and lista[3] != "-" and lista[3] == "[X]")\
        or (lista[6] == lista[7] == lista[8] and lista[6] != "-" and lista[6] == "[X]")\
        or (lista[0] == lista[4] == lista[8] and lista[0] != "-" and lista[0] == "[X]")\
        or (lista[2] == lista[4] == lista[6] and lista[2] != "-" and lista[2] == "[X]")\
        or (lista[0] == lista[3] == lista[6] and lista[0] != "-" and lista[0] == "[X]") \
        or lista[2] == lista[5] == lista[8] and lista[2] != "-" and lista[2] == "[X]"\
        or (lista[1] == lista[4] == lista[7] and lista[1] != "-" and lista[1] == "[X]"):
        print('You won, [X]')
    else:
        print('You won, [0]')


rezultat()