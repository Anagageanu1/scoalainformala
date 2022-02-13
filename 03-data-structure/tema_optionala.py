mail = input("Introdu adresa de email: ")
if type(mail) is int or str:
    pass
if mail not in "@" or ".":
    print("Adresa trebuie sa contina '@' si/sau '.' cel putin o data in email")
if len(mail) < 3:
        print("Adresa de email trebuie sa aiba mai mult de 3 caractere: ")
else:
    print("Adresa e valida")