"""
vardas = "Ausrine"
print(vardas)
"""
"""
vardas = "Ausrine"
amzius = 46
print(vardas)
print(amzius)
"""
vardas = "Modestas"
amzius = 25
arVartotojasAktyvus = False
produktoKaina = 3.99

miestai = ["Vilnius", "Kaunas", "Klaipeda"]

# print("Mano vardas " + vardas + " As gyvenu " + miestai[0] + " Mano amzius " + str(amzius))

# print("As gyvenu" + miestai[0])
"""
if amzius >= 18:
    print("Pilnametis")
else:
    print("Nepilnametis")
"""

# if amzius == 18:
#     print("Pilnametis")
# elif amzius >= 24:
# else:
#     print("Nepilnametis")

# print(miestai)
# print(miestai[0])
# miestai[1] = "Siauliai"
# miestai.append("Silute")
# miestai.insert(1, "Anyksciai")
# miestai.pop()
# del miestai[2]

#print(type(miestai))

"""
miestai = ["Vilnius", "Kaunas", "Klaipeda"]
skaiciusSarasas = [1, 3, 53, 123, 1245, 12312]
print(len(miestai))
if len(skaiciuSarasas) > 0:
    print("Skaiciu sarasas pilnas")
else:
    print("Skaiciu sarasas tuscias")
"""

"""
zodis = "Kaunas"
miestai = ["Vilnius", "Kaunas", "Klaipeda"]
if zodis in miestai:
    print(" Zodis " + zodis + " Egzistuoja sarase")
else:
    print("Zodis nerastas")
"""

"""
Priskyrimo operatoriai
= Priskyrimas
+= Prideda ir priskiria
-= Atima ir priskiria
*=
/=
%=

Matematiniai operatoriai
+
-
*
/
% liekana
** kelimas laipsniu
// sveikoji dalyba

Palyginimo operatriai
==
!= nelygu
>
<
>=
<=

Loginiai operatoriai
and
or
not

Narystes operatoriai
in priklauso
not in nepriklauso

Tapatumo operatoriai
is yra
is not nera
"""
"""
Klases darbas 06.12

1.Patikrinkite, ar studentas išlaikė egzaminą
Pazymys = 3
if Pazymys > 0 and Pazymys < 11:
    if Pazymys >= 4:
        print("Islaike")
    else:
        print("Neislaike")
"""

"""
2.Patikrinkite, ar skaičius yra lyginis;
Skaicius = 888
if Skaicius %2 ==0:
    print("Lyginis")
else:
    print("Nelyginis")
"""

"""
3. Patikrinkite, ar sąraše yra bent du skaičiai
Skaiciai = [2, 4, 6, 8, 10, 3, 3]
a=Skaiciai.count(3)
if a >= 2:
    print("Yra")
else:
    print("Nera")
"""
"""vardai = ["Jonas","Saulius", "Lina", "Marius", "Ausra"]
for vardas in vardai:
    print(vardas)"""

"""ATRINKTI SKAICIUS"""
# skaiciai = [10, 20, 30, 40, 50, 23]
# atrinkti = []
# for skaicius in skaiciai:
#     if skaicius > 25:
#         atrinkti.append(skaicius)
# print("Atrinkti skaiciai: ", atrinkti)

"""
skaiciai = [10, 10, 20, 44, 50, 50, 23, 23, 2, 45, 44, 11, 21]
unikalios_reiksmes = []
for skaicius in skaiciai:
    if skaicius not in unikalios_reiksmes:       (NOT in panaikino pasikartojancius skaicius)
        unikalios_reiksmes.append(skaicius)
print("Unikalios reiksmes: ", unikalios_reiksmes)
"""

"""FUNKCIJOS"""
# def suma(a, b):
#     return a + b
# rezultatas = suma(2,5)
# print("Suma: ", rezultatas)

# def pasisveikinimas(vardas="Anonimas"):
#     print("Labas,", vardas)
#pasisveikinimas("Modestas")

# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas
#
# rezultatas = sujungti_sarasus([1,2,3],[4,5,6])
# print("Sujungtas sarasas: ", rezultatas)


"""Parašykite funkciją ar_lyginis, kuri priima vieną skaičių 
kaip argumentą ir patikrina, ar skaičius yra lyginis. 
Jei skaičius yra lyginis, tada funkcija turi grąžinti True, 
o jei nelyginis - False."""
# def ar_lyginis (skaicius):
#     if skaicius % 2 == 0:
#         return True
#     else:
#         return False
# print((ar_lyginis(9)))

"""Parašykite funkciją didziausias_skaicius, 
kuri priima sąrašą skaičių ir grąžina didžiausią skaičių iš sąrašo;"""
# def didziausias_skaicius(sarasas):
#     didziausias = sarasas[0]
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias
# skaiciu_sarasas = [1, 2, 7, 80, 50, 54, 6, 10]
# rezultatas = didziausias_skaicius(skaiciu_sarasas)
# print(rezultatas)

"""Parašykite funkciją unikalios_reiksmes, kuri priima sąrašą ir grąžina
 naują sąrašą, kuriame yra tik unikalios reikšmės iš pradinio sąrašo."""
# A variantas
# def unikalios_reiksmes(sarasas):
#     return list(set(sarasas))
# pradinis_sarasas = [1, 2, 3, 2, 4, 3, 5, 6, 5]
# naujas_sarasas = unikalios_reiksmes(pradinis_sarasas)
# print(naujas_sarasas)

# B variantas
# def unikalios_reiksmes(sarasas):
#     tuscias_sarasas = []
#     for reiksme in sarasas:
#         if reiksme not in tuscias_sarasas:
#             tuscias_sarasas.append(reiksme)
#     return tuscias_sarasas
# naujas_sarasas = [1,1,5,6,6,6,84,95,32,32,15]
# print(unikalios_reiksmes(naujas_sarasas))


# skaicius = 1
# while skaicius <= 5:
#     print(skaicius)
#     skaicius += 1



"""IVESTI SKAICIU IR ATSPAUSDINTI LYGINIUS SKAICIUS NUO IVESTO SKAICIAUS IKI 0"""
# skaicius = int(input("iveskite_skaiciu: "))
# while skaicius >= 0:
#     if skaicius % 2 == 0:
#         print(skaicius)
#     skaicius -= 1

def sujungti_sarasus(sarasas1, sarasas2):
    sujungtas_sarasas = sarasas1 + sarasas2
    return sujungtas_sarasas

sarasas1 = [1, 2, 3]
sarasas2 = [4, 5, 6]
rezultatas = sujungti_sarasus(sarasas1, sarasas2)
print("Sujungtas sarasas: ", rezultatas)
if __name__ == "__main__":
    sujungti_sarasus(sarasas1, sarasas2)

