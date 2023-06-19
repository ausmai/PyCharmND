
# class Knyga:
#     def __init__(self, pavadinimas, autorius, puslapiai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.puslapiai = puslapiai
#         #parasyti metoda ar knyga turi > 300 psl
#     def virs_300_psl(self):
#         if self.puslapiai > 300:
#             return True
#         else:
#             return False
#
# Knyga1 = Knyga("Haris Poteris", "Rasytoja", 600)
# Knyga2 = Knyga("Karsonas kuris gyvena ant stogo", "Rasytoja2", 250)
#
# print(Knyga1.virs_300_psl())
# print(Knyga2.virs_300_psl())

#
"""__________________________________________________________________________________________________"""


# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
#         #parasyti metoda kuris padidins darbuotojui atlyginima tam tikru %
#     def padidinti_atlyginima(self, procentai):
#         padidinimas = self.atlyginimas * procentai / 100
#         self.atlyginimas += padidinimas
#
#     def pakeisti_pavarde(self, nauja_pavarde):
#         self.pavarde = nauja_pavarde
#         print("Pavarde pakeista sekmingai")
#
#     def visa_informacija(self,):
#         print(f"informacija apie darbuotoja: ")
#         print(f"Vardas: {self.vardas}")
#         print(f"Pavarde: {self.pavarde}")
#         print(f"Atlyginimas: {self.atlyginimas}")
#
#
# Darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 1000)
# Darbuotojas2 = Darbuotojas("Petras", "Petraitis", 1200)
#
#
#
#
# Darbuotojas1.padidinti_atlyginima(10)
# print(f"Naujas atlyginimas: {Darbuotojas1.atlyginimas}")
# #arba
# #print(f"{Darbuotojas1.vardas} gavo {Darbuotojas1.pavarde} Nauja atlyginima: {Darbuotojas2.atlyginimas}")
#
# Darbuotojas1.pakeisti_pavarde("Kazlauskas")
# print(Darbuotojas1.pavarde)
# #arba
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} pasikeite pavarde!")
#
# Darbuotojas1.visa_informacija()
#
#
# Darbuotojas2.padidinti_atlyginima(10)
# print(f"Naujas atlyginimas: {Darbuotojas1.atlyginimas}")
# #arba
# #print(f"{Darbuotojas2.vardas} gavo {Darbuotojas2.pavarde} Nauja atlyginima: {Darbuotojas2.atlyginimas}")
#
# Darbuotojas2.pakeisti_pavarde("Kazlauskas")
# print(Darbuotojas1.pavarde)
# #arba
# print(f"{Darbuotojas2.vardas} {Darbuotojas2.pavarde} pasikeite pavarde!")
#
# Darbuotojas2.visa_informacija()
#
#

"""__________________________________________________________________________________"""
class Preke:
    def __init__(self, pavadinimas, kaina, kiekis):
        self.pavadinimas = pavadinimas
        self.kaina = kaina
        self.kiekis = kiekis
        #atnaujinti kaina

    def atnaujinti_kaina(self, nauja_kaina):
        self.kaina = nauja_kaina
        print(f"{self.pavadinimas} nauja kaina {nauja_kaina}")

    # reikia pranesti pirkejui, kad neturime tiek prekiu
    def sandelio_likutis(self, pardavimo_kiekis):
        if pardavimo_kiekis <= self.kiekis:
            self.kiekis -= pardavimo_kiekis
            print(f"Parduota {self.pavadinimas} {pardavimo_kiekis}")
        else:
            print(f"Nepakanka prekiu: {self.pavadinimas}")

    def sandelio_papildymas(self, pdidintas_likutis):
        self.kiekis += pdidintas_likutis
        print(f"Padidintas kiekis {self.pavadinimas} {pdidintas_likutis}")


Preke1 = Preke ("Pienas", 2, 10)
Preke2 = Preke ("Duona", 3, 5)

Preke1.atnaujinti_kaina(3)
Preke2.atnaujinti_kaina(1)


Preke1.sandelio_likutis(5)
Preke2.sandelio_likutis(7)

Preke1.sandelio_papildymas(20)
Preke2.sandelio_papildymas(15)
print("Sandelio likutis", Preke1.kiekis)


"""_________________________________________________________________________________________________________"""
# # #BLOGO KURIMAS
#
# class Blog:
#     def __init__(self):
#        #listas - []
#        self.posts = []
#
#     def create_post(self, pavadinimas, aprasymas):
#         post = {
#             "pavadinimas": pavadinimas,
#             "aprasymas": aprasymas
#         }
#         self.posts.append(post)
#         print("Irasas sekmingai sukurtas")
#
#
#     def display_all_posts(self):
#         if not self.posts:
#             print("No Blog post found")
#         else:
#             print("Blog posts: ")
#             for post in self.posts:
#                 print(f" pavadinimas: {post['pavadinimas']}")
#                 print(f" aprasymas: {post['aprasymas']}")
#                 print("------------")
#
#     def update_post(self, pavadinimas, atnaujintas_aprasymas):
#         for post in self.posts:
#             if post["pavadinimas"] == pavadinimas:
#                 post["aprasymas"] = atnaujintas_aprasymas
#                 print("Blog post buvo atnaujintas")
#                 print(atnaujintas_aprasymas)
#                 break
#         else:
#             print("Blog post nerastas")
#
#     def delete_post(self, pavadinimas):
#         for post in self.posts:
#             if post["pavadinimas"] == pavadinimas:
#                 self.posts.remove(post)
#             print("Post buvo istrintas!")
#             print(post)
#             break
#         else:
#             print("Post nerastas!")
#
#
# post1 = Blog() #NAUDOJAME TA PATI OBJEKTA, NES IS NETURI ATRIBUTU
#
#
# post1.create_post("Duomenu analitikos studentai uzkariavo pasauli", "Karta gyveno analitikai, kurie ismoks programuoti")
# post1.create_post("Mokslininkai isrado nauja metoda", "Kaip greiciau ismokti duomenu analize")
# post1.create_post("Kulinarijos sedevrai", "Tukstantis ir vienas receptas")
#
#
# post1.display_all_posts()
#
# post1.update_post("Duomenu analitikos studentai uzkariavo pasauli", "Jie jau moka programuoti")
#
# post1.delete_post("Jie jau moka programuoti")
# #
# # #CRUD, CREATE, READ, UPDATE, DELETE.



