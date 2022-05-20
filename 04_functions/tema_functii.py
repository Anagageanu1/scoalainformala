def your_function(*lista):
    msg = " "
    if len(list(lista)) == 0:
        msg = 0
    else:
        print(sum([d for d in lista if isinstance(d, int)]))

your_function()
your_function(1, 5, -3, "abc", [12, 56, "cad"])
your_function(2, 4, "abc", "param_1=2")


def functie():
    msg = " "
    nr_introdus = input ("Introdu o valoare: ")
    value = nr_introdus
    if value.isnumeric():
        msg = value
    else:
        msg = ("0")
    return msg
msg = functie()
print(msg)