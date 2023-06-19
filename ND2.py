# 3. Sukurkite tuščią žodyną, kuris bus naudojamas kaip studentų sąrašas.
# Leiskite vartotojui įvesti studento vardą, pavardę ir amžių.
# Sukurkite naują studento žodyną su įvestais duomenimis ir pridėkite jį prie studentų sąrašo.
# Po kiekvieno naujo studento pridėjimo, išveskite pranešimą apie sėkmingą pridėjimą.
# Leiskite vartotojui pasirinkti, ar nori pridėti dar vieną studentą. Jei taip, grįžkite į žingsnį 2. Jei ne, tęskite į žingsnį 6.
# Išveskite visus pridėtus studentus su jų vardais, pavardėmis ir amžiais.

class Studentai:
    def __init__(self):
        self.studentu_sarasas = []

    def naujas_studentas(self, vardas, pavarde, amzius):
        naujokas = {
            "vardas": vardas,
            "pavarde": pavarde,
            "amzius": amzius
        }

        self.studentu_sarasas.append(naujokas)
        print("Naujas studentas sekmingai ivestas")

studentai = Studentai()

while True:
    vardas = input("Iveskte studento varda: ")
    pavarde = input("Iveskite studento pavarde: ")
    amzius = input("Iveskite studento amziu: ")

    studentai.naujas_studentas(vardas, pavarde, amzius)

    pasirinkimas = input("Ar norite prideti dar viena studenta? (taip/ne): ")
    if pasirinkimas.lower() != "taip":
        break

print("Pridetu studentu sarasas: ")
for studentas in studentai.studentu_sarasas:
    print(f" Vardas: {studentas['vardas']}, Pavarde: {studentas['pavarde']}, Amzius: {studentas['amzius']} ")
