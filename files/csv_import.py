import csv

masini = [
    ['Dacia', 'Logan', 2005, 75],
    ['Renault', 'Clio', 2005, 75]
]

with open ('data.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for masina in masini:
        csv_writer.writerow(masina)
        #
        # trebuie pus in while pt aia cu numar infinit de taskuri
        # un fisier cu categorii unul cu taskuri
        # 4. if a in stringul respectiv