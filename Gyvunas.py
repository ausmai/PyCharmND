#---------------------------------METODO PERRASYMAS
#
# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print("The animal makes a sound")
#
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def make_sound(self):
#         print("The dog barks")
#
# dog = Dog("Bob", 5)
# dog.make_sound()
# print(dog.name, dog.age)

#arba

#print(f"My dog name is {dog.name}" + " and age is " + str(dog.age))

"""----------------------------------------------------------------------------------------------------"""
# class Vehicle:
#
#     def __init__(self, brand):
#         self.brand = brand
#
#     def start_engine(self):
#         print("Engine started!")
#
#     def stop_engine(self):
#         print("Engine stopped!")
#
# class Car(Vehicle):

#     def drive(self):
#         print("Car is driving!")
#
#
# car = Car("Toyota")
# print(car.brand)
# car.start_engine()
# car.drive()
# car.stop_engine()

"""-----------------------------------------------------------------------------"""

#sukurti Zmogu
#
# class Zmogus:       #sukuriame tevine klase
#     def __init__(self, vardas, amzius):     #isvardiname savybes
#         self.vardas = vardas        #aprasome savybes
#         self.amzius = amzius
#
#     def informacija(self):      #Metodas rodyti informacija apie zmogu
#         print(f" Zmogaus vardas yra {self.vardas}")
#         print(f" Zmogaus amzius yra {self.amzius}")
#
#
# class Darbuotojas(Zmogus):          #Sukuriame vaikine klase
#     def __init__(self, vardas, amzius, atlyginimas):    #isvardiame kokias savybes tures darbuotojas
#         super().__init__(vardas, amzius)        #nurodome, kurias savybes tures is Zmogaus klases
#         self.atlyginimas = atlyginimas      #aprasome papildoa darbuotojo savbe
#
#     def informacija(self):
#         super().informacija()          #panaudosiu tevynes klases metoda. print vardas, amzius
#         print(f"Darbuotojo atlyginimas yra {self.atlyginimas}")
#
# zmogus = Zmogus("Jonas", 12)            #suuriame tevynes klases objekta
# darbuotojas = Darbuotojas("Lina", 30, 2000)         #sukuriame vaikines klases objekta
#
# zmogus.informacija()
# print()
# darbuotojas.informacija()

"""---------------------------------------------------------------------------------------------------"""

#Pirkiniu krepselio funkcionalumas: produktas ir krepselis

class Produktas:
    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

    def informacija(self):
        print(f" Produkto pavadinimas yra {self.pavadinimas}")
        print(f" Produkto kaina yra {self.kaina} $")

class Prekiu_krepselis(Produktas):
    def __init__(self):
        super().__init__(pavadinimas = None, kaina = None)
        self.produktai = []

    def add_produktas(self, produktas):
        self.produktai.append(produktas)
        print(f" Produktas {produktas.pavadinimas} idetas i krepseli ")

    def istrinti_produkta(self, produktas):
        if produktas in self.produktai:
            self.produktai.remove(produktas)
            print(f" Produktas {produktas.pavadinimas} pasalintas is krepselio ")
        else:
            print(f" Produktas {produktas.pavadinimas} nerastas")

    def suskaiciuoti_visa_kaina(self):
        visa_kaina = 0
        for produktas in self.produktai:        #jei naudoji for, turi buti return
            visa_kaina += produktas.kaina
        return visa_kaina

class Akcija_Produktas(Produktas):
    def __init__(self, pavadinimas, kaina, akcija_procentais):
        super().__init__(pavadinimas, kaina)
        self.akcija_procentais = akcija_procentais

    def suskaiciuoti_akcijos_kaina(self):
        akcijos_suma = self.kaina * (self.akcija_procentais / 100)
        nuolaidos_kaina = self.kaina - akcijos_suma
        return nuolaidos_kaina

    def informacija(self):
        super().informacija()
        print(f" Nuolaida {self.akcija_procentais} %")
        print(f" Galutine kaina {self.suskaiciuoti_akcijos_kaina()} $")

produk = Produktas("Obuolys", 2)
produk1 = Akcija_Produktas("Sokoladas", 3, 10)
produk2 = Produktas("Cipsai", 4)

krepselis = Prekiu_krepselis()
krepselis.add_produktas(produk)
krepselis.add_produktas(produk1)
krepselis.add_produktas(produk2)
print()
for produktas in krepselis.produktai:
    produktas.informacija()
    print()

visu_produktu = krepselis.suskaiciuoti_visa_kaina()
print(f" Bendra kaina {visu_produktu} $")
print()

krepselis.istrinti_produkta(produk1)

visu_produktu = krepselis.suskaiciuoti_visa_kaina()
print(f" Nauja galutine kaina {visu_produktu} $")
print()


