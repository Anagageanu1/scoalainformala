# 1. vehicul
# 1.1 vehicul de apa
# 1.2. vehicul de apa
# 1.3 vehicul de aer
# 1.4 vehicul terestru
# 1.4.1 vehicul de teren
# 1.4.2 vehicul de curs

# 2. Animale
# 2.1 Mamifere
# 2.1.1 Animale salbatice
# 2.1.2 Animale domestice
# 2.2 Reptile
# 2. pentru 2.1 si 2.2 este superclasa
# 2.1.1 si 2.1.2 pentru 2.1 sub subclase
# 2.1.1 si 2.1.2 pentru 2 sub subclase

#  Max este un caine mare care doarme toata ziua.
# obiectul - > Max (substantiv)
# clasa -> caine (substantiv)
# proprietatea -> mare (adjectiv)
# activitatea -> doarme toata ziua (verb) -> metode

# Un logan verde merge incet
# obiect  - Un logan
# clasa - masina
# proprietate -> verde
# activitate -> merge

# Rudolph este o pisica mare care mananca multe boabe.
# obiect - rudolph
# clasa - pisica
# proprietate - mare
# activitate - mananca multe

# Lenovo-ul gri se poate cumpara la pret mai mic pe un magazin online.
# obiect - lenovo
# clasa - laptop
# proprietate - gri
# activitate - se poate cumpara

#  Sa se realizeze jocul x si 0 intre doi jucatori in care:
# primul jucator este mereu calculatorul
# exista reguli de joc pentru mutari
# obiecte -> calculator / omul
# clasa -> jocul
#  proprietatea -> primul jucator
# activitatea -> mutarile

# class MyFirstClass:
#     pass
#
# my_object = MyFirstClass

# PROBLEMA STIVEI
# intr-o stiva

stack = []

# def push(val):
#     stack.append(val)
#     return stack
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())
#
# class Stack:
#
#     def __init__(self):
#         self.__stack.list = []
#
#     def push(self, val):
#         self.__stack_list.append()
#
#     def pop(self):
#         val = self._stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#     def __str__(self):
#         return f"{self.__stack_list}"
#
#
# obiect_stiva = Stack()
# obiect_stiva.push(3)
# print(obiect_stiva)
# obiect_stiva.push(2)
# print(obiect_stiva)
# obiect_stiva.push(1)
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())
# obiect_stiva = stack()
# print(obiect_stiva.stack_list)

class ClasaExemplu:

    def __init__(self, val=1):
        self.first = val
        self.second = 0

    def set_second(self, val=2):
        self.second = val

    def __str__(self):
        return f"{self.first} {self.second}"

obiect_1 = ClasaExemplu()
obiect_2 = ClasaExemplu(2)

print(obiect_1)
print(obiect_2)





