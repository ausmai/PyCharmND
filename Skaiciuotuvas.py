#sukurti skaiciuotuva

# Funkcija, kuri pritaiko operaciją
class Skaiciuotuvas:
    def __init__(self):
        self.rezultatas = 10

    def sudetis(self, skaicius):
        self.rezultatas += skaicius
    def atimtis(self, skaiciua):
        self.rezultatas -= skaicius
    def dalyba(self, skaicius):
        if skaicius != 0:
            self.rezultatas /= skaicius
        else:
            print("Dalyba is nulio negalima")

    def daugyba(self, skaicius):
        self.rezultatas *= skaicius
    def isvalyti(self):
        self.rezultatas = 0

    def get_rezultatas(self):
        return self.rezultatas

skaiciuoklis = Skaiciuotuvas()
while True:
    print("Pasirinkite norima veiksma_> ")
    print("1. Sudetis")
    print("2. Atimtis")
    print("3. Dalyba")
    print("4. Daugyba")
    print("5. Isvalyti")
    pasirinkimas = input("Iveskite pasirinkio numeri_> ")

    if pasirinkimas == "1":
        skaicius = int(input("Iveskite skaiciu_> "))
        skaiciuoklis.sudetis(skaicius)

    elif pasirinkimas == "2":
        skaicius = int(input("Iveskite skaiciu_> "))
        skaiciuoklis.atimtis(skaicius)
    elif pasirinkimas == "3":
        skaicius = float(input("Iveskite skaiciu_> "))
        skaiciuoklis.dalyba(skaicius)
    elif pasirinkimas == "4":
        skaicius =int(input("Iveskite skaiciu_> "))
        skaiciuoklis.daugyba(skaicius)
    elif pasirinkimas == "5":
        skaiciuoklis.isvalyti()

    else:
        print("Negalimas veiksmas")



    print("rezultatas: ", Fore.GREEN + str(skaiciuoklis.get_rezultatas()) + Style.RESET_ALL)
    print()