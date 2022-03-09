# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala.
#
# Lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def my_function():
    global lista
    new_list = []
    while len(lista) > 0:
        new_list = lista.pop(1::3)  # aici nu reusesc sa imi dau seama cum pot sa ii scot din 3 in 3
    return new_list

print(my_function())


