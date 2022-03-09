#class MyFirstclass:
#    pass
#
# my_first_object = MyFirstclass()

class Dog:
    nr_picioare = 4 # atribut

    def __init__(self, name):
        self.nume = name

    def __str__(self):
        return f"{self.nume}"

# print(Caine.nr_picioare)

cainele_meu = Caine("Rex")
print(cainele_meu.nume)





