class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __add__(self):  #adunarea
        return self.numarator + self.numitor

    def __sub__(self):  #scaderea
        return self.numarator - self.numitor

    def rezultat_functie(self):  #impartirea
        return self.numarator/self.numitor

    def inversul_fractiei(self):  #inversa
        try:
            return self.numitor / self.numarator
        except ZeroDivisionError:
            return f"Nu se poate imparti la 0"

    def __str__(self):  #afisarea
        self.rezultat = self.numarator/self.numitor
        return f"Rezultatul adunarii este: {self.__add__()}\n " \
               f"Rezultatul scaderii este: {self.__sub__()}\n"\
               f"Rezultatul fractiei este: {self.rezultat_functie()}\n"\
               f"Inversa factiei este: {self.inversul_fractiei()}"


fractie1 = Fractie(9, 3)
print(fractie1)