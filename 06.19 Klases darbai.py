"""1. arašykite programą, kuri atspausdina visus lyginius skaičius nuo 1 iki 10"""

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

"""arba"""
# for i in range(1, 11):
#     for i in range(2, 11, 2):
#         print(i)


"""2. Sukurkite sąrašą, kuriame yra keletas skaičių. Naudojant for ciklą, apskaičiuokite sąrašo skaičių sumą"""

# sarasas = [10, 7, 23]
# skaicius = 0
# for i in sarasas:
#     skaicius += i
#
# print(skaicius)

"""3. Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 20, tačiau jei skaičius yra dalijamas iš 3, 
atspausdinkite "Fizz", jei skaičius yra dalijamas iš 5, atspausdinkite "Buzz", 
jei skaicius dalinasi is 3 ir 5 atspausdinti "FizzBuzz;"""

# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

"""4. Sukurkite klasę "KnygosBiblioteka", turinčią atributą "knygos" (sąrašą) ir metodus "pridėti_knygą" ir 
"rodyti_knygas". Pridėkite funkcionalumą, kad galėtumėte pridėti knygas į sąrašą ir atspausdinti visas 
bibliotekoje esančias knygas"""

# class KnygosBiblioteka:
#     def __init__(self):
#         self.knygos = []
#
#     def prideti_knyga(self, autorius, pavadinimas):
#         knyga = {
#             "autorius": autorius,
#             "pavadinimas": pavadinimas
#         }
#
#         self.knygos.append(knyga)
#         print("Nauja knyga prideta")
#
#
#     def rodyti_knygas(self):
#         if not self.knygos:
#             print("Nerasta knyga")
#         else:
#             print("knygos: ")
#             for i in self.knygos:
#                 print(f" autorius: {i['autorius']}")
#                 print(f" pavadinimas: {i['pavadinimas']}")
#                 print("------------")
#
# knyga1 = KnygosBiblioteka()
#
# while True:
#     print("Pasirinkite veiksma: ")
#     print("1. Prideti nauja knyga ")
#     print("2. Rodyti knygas ")
#
#     pasirinkimas = input("Iveskite pasirinkimo numeri: ")
#     if pasirinkimas == "1":
#         autorius = input("Prideti nauja autoriu: ")
#         pavadinimas = input("Įveskite pavadinima: ")
#         knyga1.prideti_knyga(autorius, pavadinimas)
#         print()
#
#     elif pasirinkimas == "2":
#         knyga1.rodyti_knygas()
#         print()

"""arba"""

class KnygosBiblioteka:
    def __init__(self):
        self.knygos = []
    def prideti_knyga(self, knyga):
        self.knygos.append(knyga)
        print(f" Knyga {knyga} prideta")
    def rodyti_knygas(self):
        if self.knygos:
            print("Bibliotekos visos knygos: ")
            for knyga in self.knygos:
                print(knyga)
        else:
            print("Biblioteka tuscia")
knyga = KnygosBiblioteka()
knyga.prideti_knyga("Altoriu seselyje")
knyga.prideti_knyga("Brisiaus galas")
knyga.rodyti_knygas()


"""5.Sukurkite žodyną su prekių pavadinimais ir jų kainomis. Parašykite programą, 
kuri suskaičiuoja ir atspausdina visų prekių kainų sumą"""

# prekes = {
#     "Kompiuteris": 1200,
#     "Telefonas": 800,
#     "Televizorius": 1500,
#     "Ausinės": 100,
#     "Klaviatūra": 50
# }
#
# suma = sum(prekes.values())
# print("Visų prekių kainų suma:", suma)

"""arba"""
# prekes = {
#     "obuolys": 1.98,
#     "persikai": 3.29,
#     "agurkai": 4.50
# }
# suma = 0
# for kaina in prekes.values():             #Kaina-raktas, prekes-
#     suma += kaina
# print(f" Visu prekiu kainu suma: {suma}")

"""----------------------------------------------------------------------------------"""
#parasyti is *** trikampi
# eilutes = 5
# for i in range(1, eilutes + 1):             #pradeda nuo pirmos * ir daugina is i
#     print(" " * (eilutes - i), end="")
#     print("*" * (2 * i - 1))
#
# #eglute su kotu
# aukstis = 5
# eilutes = aukstis + 1
# for i in range(1, eilutes):
#     tarpu_skaicius = aukstis - i
#     print(" " * tarpu_skaicius + "*" * (2 * i - 1))
#
# pagrindas_skyrikliais = " " * (aukstis - 1) + "|"
# print(pagrindas_skyrikliais)

"""arba"""
# aukstis = 5
# eilutes = aukstis + 1
# for i in range(1, eilutes + 1):
#     print(" " * (eilutes - i), end="")
#     print("*" * (2 * i - 1))
# print(" " * (eilutes - 1), end="")
# print("|")