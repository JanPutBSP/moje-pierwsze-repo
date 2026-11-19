n = int(input())
poprawne = 0



for liczba in range(1, n + 1):
    print(f"Podaj kwadrat liczby {liczba}")
    proby = 0
    odgadnieto = False
    while proby < 3 and not odgadnieto:
        odpowiedz =int(input())
        proby += 1
        
        if odpowiedz == liczba * liczba:
            print("Poprawna odpowiedź")
            poprawne += 1
            odgadnieto= True
        else:
            print("Błędna odpowiedź")
print(poprawne)