# 1. Scrie un program care sa calculeze suma
# dintre trei numere. Daca valorilesunt egale,
# returnati de trei ori suma acestora.(1 punct)

def sumaa():
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))
    c = int(input("Enter the third value: "))
    suma = []
    if a == b and b == c and a == c:
        suma = [(a * b * c) * 3]
    else:
        suma = a + b + c
    return suma


print(sumaa())
