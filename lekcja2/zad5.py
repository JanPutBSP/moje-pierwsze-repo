pkt= int(input("Podaj liczbe pkt: "))

if pkt >= 10:
    print("Zaliczone")
else:
    punkty = 10 - pkt
    print("Niezaliczone")
    print(f"Brakuje: {punkty}")
    