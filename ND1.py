# 2. Sukurkite klasę "Mokinys", turinčią atributus "vardas", "pavarde" ir "pazymiai".
# Parasykite metodą, kuris pridės naują pažymį prie mokinio pažymių sąrašo.
# Parasykite metodą, kuris suskaičiuos mokinio pažymių vidurkį.
# Sukurkite kelis objektus iš šios klasės su skirtingais pažymiais ir patikrinkite, ar vidurkis skaičiuojamas teisingai.

class Mokinys:

    def __init__(self, vardas, pavarde, pazymiai):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pazymiai = pazymiai

    def naujas_pazymys(self, pazymys):
        self.pazymiai.append(pazymys)
        print("Nauja pazymys sekmingai ivestas")

    def vidurkis(self):
        if len(self.pazymiai) ==0:
            return 0
        else:
            return round(sum(self.pazymiai) / len(self.pazymiai),2)

#ivedam mokinius su skirtingais pazymiais
mokinys1 = Mokinys("Jonas", "Jonaitis", [8, 9, 7, 10, 6])
mokinys2 = Mokinys("Petras", "Petraitis", [7, 8, 9, 6, 8, 10, 7])
mokinys3 = Mokinys("Lina", "Linaite", [9, 10, 9, 8, 9])

#patikrinam vidurkius
print(f"{mokinys1.vardas} {mokinys1.pavarde} vidurkis: {mokinys1.vidurkis()}")
print(f"{mokinys2.vardas} {mokinys2.pavarde} vidurkis: {mokinys2.vidurkis()}")
print(f"{mokinys3.vardas} {mokinys3.pavarde} vidurkis: {mokinys3.vidurkis()}")

#pridedame naujus pazymius
mokinys1.naujas_pazymys(8)
mokinys2.naujas_pazymys(9)
mokinys3.naujas_pazymys(10)

#patikrina vidurius is naujo
print(f"{mokinys1.vardas} {mokinys1.pavarde} vidurkis: {mokinys1.vidurkis()}")
print(f"{mokinys2.vardas} {mokinys2.pavarde} vidurkis: {mokinys2.vidurkis()}")
print(f"{mokinys3.vardas} {mokinys3.pavarde} vidurkis: {mokinys3.vidurkis()}")