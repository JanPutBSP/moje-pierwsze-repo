# Python — zajęcia 3. Pętle `for` i `while`

Przećwiczysz powtarzanie instrukcji, obliczanie sumy i wczytywanie danych w pętli. Na końcu połączysz pętle `for` i `while` w jednym programie.

Każde zadanie zapisz w osobnym pliku `.py`. Każda linia przykładowego wejścia odpowiada jednemu wywołaniu `input()`. Używaj `input()` bez komunikatu w nawiasach. Przyjmij, że użytkownik wpisuje liczby całkowite. W zadaniu 7 sprawdzaj dodatkowo podany zakres wyniku.

## Przypomnienie

`for` pozwala przechodzić przez kolejne wartości. `range(1, 4)` daje liczby 1, 2 i 3. Górna granica nie należy do zakresu.

```python
for liczba in range(1, 4):
    print(liczba)
```

`while` wykonuje blok, dopóki warunek jest prawdziwy. Zmiana licznika pozwala zakończyć pętlę.

```python
liczba = 1
while liczba <= 3:
    print(liczba)
    liczba = liczba + 1
```

Oba programy wypisują ten sam wynik. Instrukcje należące do pętli muszą mieć wcięcie. Jeżeli wewnątrz pętli umieścisz kolejną pętlę lub `if`, ich bloki wymagają następnego poziomu wcięcia.

## Zadanie 1. Liczby od 1 do n

Wczytaj dodatnią liczbę całkowitą `n`. Wypisz liczby od 1 do `n`, każdą w nowej linii. Przygotuj dwie wersje rozwiązania — z `for` w pliku `zadanie_01_for.py` i z `while` w pliku `zadanie_01_while.py`. Sprawdź także `n = 1`.

**Przykładowe wejście**

```text
4
```

**Przykładowe wyjście obu wersji**

```text
1
2
3
4
```

## Zadanie 2. Odliczanie

Wczytaj nieujemną liczbę całkowitą `n`. Używając `while`, wypisz liczby od `n` do 0 włącznie, a po zakończeniu pętli wypisz `Start!`. Sprawdź także `n = 0`. Zapisz rozwiązanie w `zadanie_02.py`.

**Przykładowe wejście**

```text
3
```

**Przykładowe wyjście**

```text
3
2
1
0
Start!
```

## Zadanie 3. Liczby parzyste

Wczytaj dodatnią liczbę całkowitą `n`. Użyj `for` oraz `if`, aby wypisać tylko liczby parzyste z przedziału od 1 do `n` włącznie. Operator `%` zwraca resztę z dzielenia. Dla `n = 1` program ma zakończyć się bez wypisywania tekstu. Zapisz rozwiązanie w `zadanie_03.py`.

**Przykładowe wejście**

```text
7
```

**Przykładowe wyjście**

```text
2
4
6
```

## Zadanie 4. Piramida

Wczytaj dodatnią liczbę całkowitą `n`. Wypisz `n` wierszy z symbolami `#`. Pierwszy wiersz ma zawierać jeden symbol, drugi dwa, a każdy następny o jeden więcej. Użyj pętli `for`. Zapisz rozwiązanie w `zadanie_04.py`.

**Przykładowe wejście**

```text
4
```

**Przykładowe wyjście**

```text
#
##
###
####
```

**Rozszerzenie.** Uzyskaj ten sam wynik za pomocą dwóch zagnieżdżonych pętli `for`. Wypisuj symbole pojedynczo przez `print("#", end="")`. Samo `print()` rozpoczyna nową linię. Zapisz tę wersję w `zadanie_04_petle.py`.

## Zadanie 5. Suma liczb

Wczytaj dodatnią liczbę całkowitą `n`. Za pomocą pętli oblicz sumę liczb od 1 do `n` włącznie. Przed pętlą utwórz zmienną przechowującą sumę, a w każdym obiegu dodaj do niej kolejną liczbę. Wypisz tylko końcowy wynik. Zapisz rozwiązanie w `zadanie_05.py`.

**Przykładowe wejście**

```text
5
```

**Przykładowe wyjście**

```text
15
```

## Zadanie 6. Wczytywanie do zera

Wczytuj liczby całkowite za pomocą `while`, aż użytkownik poda `0`. Wypisz sumę oraz liczbę wprowadzonych wartości. Końcowe zero nie jest liczone. Dopuszczalne są liczby ujemne. Sprawdź również przypadek, w którym pierwszą podaną liczbą jest zero — suma i liczba wartości powinny wtedy wynosić 0. Zapisz rozwiązanie w `zadanie_06.py`.

**Przykładowe wejście**

```text
5
-2
7
0
```

**Przykładowe wyjście**

```text
Suma: 10
Liczba wartości: 3
```

## Zadanie 7. Poprawny wynik każdego studenta

Wczytaj dodatnią liczbę studentów `n`. Następnie wczytaj wynik każdego studenta jako liczbę całkowitą od 0 do 100 włącznie. Jeśli wynik nie należy do tego przedziału, wypisz `Niepoprawny wynik` i ponawiaj odczyt dla tego samego studenta, aż otrzymasz poprawną wartość. Na końcu wypisz sumę poprawnych wyników.

Użyj `for` do obsługi kolejnych studentów oraz wewnętrznej pętli `while` do ponawiania odczytu. Błędna wartość nie zwiększa liczby obsłużonych studentów i nie trafia do sumy. Do zapisania warunku możesz użyć operatora `or`, który daje `True`, gdy przynajmniej jeden z połączonych warunków jest prawdziwy. Zapisz rozwiązanie w `zadanie_07.py`.

**Przykładowe wejście**

```text
3
80
-5
105
60
100
```

**Przykładowe wyjście**

```text
Niepoprawny wynik
Niepoprawny wynik
Suma: 240
```

W przykładzie drugi student otrzymuje wynik 60 dopiero po dwóch błędnych wartościach. Sprawdź też wyniki graniczne 0 i 100.

## Zadanie 8. Trzy próby dla każdej liczby

Wczytaj dodatnią liczbę całkowitą `n`. Dla każdej liczby od 1 do `n` wypisz komunikat `Podaj kwadrat liczby X`, zastępując `X` bieżącą liczbą. Następnie wczytuj odpowiedzi użytkownika. Na każdą liczbę przysługują maksymalnie trzy próby.

Po błędnej odpowiedzi wypisz `Błędna odpowiedź`. Po poprawnej odpowiedzi wypisz `Poprawna odpowiedź` i przejdź od razu do kolejnej liczby. Po trzech błędnych odpowiedziach również przejdź do kolejnej liczby. Na końcu wypisz, ile przykładów użytkownik rozwiązał poprawnie, niezależnie od liczby wykorzystanych prób.

Użyj `for` do wybierania kolejnych liczb, `while` do obsługi prób oraz `if` i `else` do sprawdzania odpowiedzi. Kwadrat możesz obliczyć jako `liczba * liczba`. W warunku `while` możesz użyć `and`, który wymaga spełnienia obu połączonych warunków. Zapisz rozwiązanie w `zadanie_08.py`.

**Przykładowe wejście**

```text
3
1
3
4
8
10
12
```

**Przykładowe wyjście**

```text
Podaj kwadrat liczby 1
Poprawna odpowiedź
Podaj kwadrat liczby 2
Błędna odpowiedź
Poprawna odpowiedź
Podaj kwadrat liczby 3
Błędna odpowiedź
Błędna odpowiedź
Błędna odpowiedź
Poprawnie rozwiązane: 2
```

Przed napisaniem programu ustal, które zmienne trzeba ustawić ponownie dla każdej liczby, a które przechowują wynik całego programu. Sprawdź poprawną odpowiedź w pierwszej i trzeciej próbie oraz trzy błędne odpowiedzi.

## Oddanie rozwiązań

1. Umieść wszystkie pliki `.py` z tej lekcji w folderze `zajęcia_3`.
2. Dodaj cały folder do swojego repozytorium na GitHubie i sprawdź, czy wszystkie rozwiązania są widoczne.

