# def transform_cnp_from_int_to_list(cnp):
#     cnp = str(cnp)
#     the_list = []
#     for nr in cnp:
#         the_list.append(int(nr))
#     return the_list
#
#
# def is_valid_cnp(cnp):
#     cnp = str(cnp)
#     sex = int(cnp[0])
#     if sex not in (1, 2, 3, 4, 5, 6, 7, 8, 9):  # fie folosim range(1,10)
#         print('sex invalid')
#         return False
#
#     an = int(cnp[1:3])
#     if an not in range(1, 100):
#         print('an invalid')
#         return False
#
#     luna = int(cnp[3:5])
#     if luna not in range(1, 12):
#         print("luna invalida")
#         return False
#
#     zi = int(cnp[5:7])
#     if zi not in range(0, 31):
#         print("zi invalida")
#         return False
#
#     judet = int(cnp[7:9])
#     if judet not in range(1, 47) and (51, 53):
#         print("judet invalid")
#         return False
#
#     numere_judete = int(cnp[9:11])
#     if numere_judete not in range(0, 999):
#         print("numar judet invalid")
#         return False
#
#     nr_control = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
#     cnp_as_list = transform_cnp_from_int_to_list(cnp)
#     val = sum(a * int(b) for a, b in zip(nr_control, cnp_as_list)) % 11
#
#     variabila = 1 if val == 10 else int(val)
#     # daca valoarea din return este diferita de valoarea cnp 12, atunci return False
#     if variabila != int(cnp[12]):
#         print("cifra de control invalida")
#         return False
#     return True
#
#
# CNP = input("Introdu CNP-ul tau: ")
# is_valid_cnp(CNP)
#
# class Validator:
#
#     def __init__(self, cnp):
#         self.CNP = cnp
#
#     def lungime(self, ):
#         if len(self.CNP) != 13:
#             return False
#         return True
#
#
#     def __str__(self):
#         if self.lungime() is True:
#             return f'Cnp-ul {self.CNP} este valid'
#         return f"Cnp=ul {self.CNP} nu este valid"
#
# obiect_1 = Validator(input("Introdu CNP-ul: "))
# print(obiect_1)

text = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
for i,j in text:

