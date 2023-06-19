class Automobilis:
    def __init__(self, spalva, greitis):
        self.spalva = spalva
        self.greitis = greitis
        self.uzvesta = False


    def uzvedam_automobili(self):
        if not self.uzvesta:
            print("Automobilis užsivedė")
            self.uzvesta = True
        else:
            print("Automobilis jau yra užvestas")
    def didinam_greiti(self, kiekis):
        self.greitis += kiekis

    def uzgesom(self):
        if self.uzvesta:
            print("Automobilis sustojo")
            self.uzvesta = False
        else:
            print("Automobilis jau sustojo")

automobilis = Automobilis("Juoda", 100)
automobilis.uzvedam_automobili()

automobilis.didinam_greiti(20)
print(automobilis.greitis)
automobilis.uzgesom()


# print(automobilis.greitis)

# honda = Automobilis("Juoda", 100)
#
# # volvo = Automobilis("Melyna", 120)
# # print(volvo.greitis)
#
#
# honda.didinam_greiti(50)
#
# print("Jūsų esamas greitis: ", honda.greitis)