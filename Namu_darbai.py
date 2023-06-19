#1.Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai.
#Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą.


# def nelyginiai_skaiciai(sarasas):
#     tuscias_sarasas = []
#     for reiksme in sarasas:
#         if reiksme % 2 != 0:
#             tuscias_sarasas.append(reiksme)
#     return sum(tuscias_sarasas)
# sarasas = [10, 13, 15, 20, 22, 27, 30, 36, 39, 43, 45, 50]
# a = nelyginiai_skaiciai(sarasas)
# print(a)


# 2.Raskite didžiausią skaičių iš Jūsų sukurto skaičių sąrašo.
# Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina didžiausią skaičių.

# def didziausias_skaicius(sarasas):
#     didziausias = sarasas[0]
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias
# skaiciu_sarasas = [10, 5, 30, 85, 100, 3, 73]
# rezultatas = didziausias_skaicius(skaiciu_sarasas)
# print(rezultatas)

#
# 3.Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius.
# def pirminis(skaicius):
#     if number < 2:
#         return False
#     for daliklis in range(2, skaicius):
#         if skaicius % daliklis == 0:
#             return False
#     return True
# number = 17
# if pirminis(skaicius):
#     print(skaicius, "yra pirminis skaicius.")
# else:
#     print(skaicius, "nera pirminis skaicius.")





