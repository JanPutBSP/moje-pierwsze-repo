imie = input("Podaj imie")
wynik1 = int(input("Podaj wynik 1"))
wynik2 = int(input("Podaj wynik 2"))
suma = wynik1 + wynik
if suma >= 15 and wynik1 >= 5 and wynik2 >= 5:
    print(f"Student {imie} Suma: {suma} Status: zaliczone")
else:
    print(f"Student {imie} Suma: {suma} Status: niezaliczone")