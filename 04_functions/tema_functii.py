# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă numere întregi sau reale.
#           ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
#
#           ○ your_function() va returna 0.
#
#           ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4)

def your_function(*lista):
    msg = " "
    if len(list(lista)) == 0:
        msg = 0
    else:
        print(sum([d for d in lista if isinstance(d, int)]))

your_function()
your_function(1, 5, -3, "abc", [12, 56, "cad"])
your_function(2, 4, "abc", "param_1=2")

# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează valoarea 0.
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