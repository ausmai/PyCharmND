"""1. Parašykite programą, studentų valdymo sistemą ir leistų vartotojui įvesti komandas, kad galėtų manipuliuoti studentų duomenimis."""

class Studentas:

    def __init__(self):
        self.sarasas = []

    def naujas_studentas(self, vardas, pavarde, id):
        for i in self.sarasas:
            if i['id'] == id:
                print(f"Studentas su ID jau egzistuoja ")
                return

        naujokas = {
            "vardas": vardas,
            "pavarde": pavarde,
            "id": id
        }

        self.sarasas.append(naujokas)
        print("Naujas studentas sekmingai ivestas")


    def istrinti(self, id):
        for i in self.sarasas:
            if i['id'] == id:
                self.sarasas.remove(i)
                print(f" Studentas pasalintas")
                return
            print(f"Studentas nerastas")

    def studento_informacija(self, id):
        for i in self.sarasas:
            if i['id'] == id:
                print("Informacija apie studenta:")
                print(f" Vardas: {i['vardas']}")
                print(f" Pavarde: {i['pavarde']}")
                print(f" ID: {i['id']}")
                return
        print(f"Studentas su ID nerastas")


    def visi_studentai(self):
        if not self.sarasas:
            print("Nerastas sarasas")
        else:
            print("Studentai: ")
            for i in self.sarasas:
                print(f" vardas: {i['vardas']}")
                print(f" pavarde: {i['pavarde']}")
                print(f" id: {i['id']}")
                print("------------")

studentas1 = Studentas()
studentas1.naujas_studentas("Jonas", "Jonaitis", 1)
studentas1.naujas_studentas("Antanas", "Antanaitis", 2)
while True:
    print("Pasirinkite veiksma: ")
    print("1. Prideti nauja studenta ")
    print("2. Pasalinti studenta ")
    print("3. Gauti informacija apie studenta pagal ID ")
    print("4. Rodyti visus studentus")
    print("5. Baigti programa ")

    pasirinkimas = input("Iveskite pasirinkimo numeri: ")

    if pasirinkimas == "1":
        vardas = input("Įveskite studento vardą: ")
        pavarde = input("Įveskite studento pavardę: ")
        id = input("Įveskite studento ID: ")
        studentas1.naujas_studentas(vardas, pavarde, id)
        print()

    elif pasirinkimas == "2":
        id = input("Įveskite studento ID, kurį norite pašalinti: ")
        studentas1.istrinti(id)
        print()

    elif pasirinkimas == "3":
        id = input("Įveskite studento ID, apie kurį norite gauti informaciją: ")
        studentas1.studento_informacija(id)
        print()

    elif pasirinkimas == "4":
        studentas1.visi_studentai()
        print()

    elif pasirinkimas == "5":
        print("Programa baigta.")
        break

    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")
        print()