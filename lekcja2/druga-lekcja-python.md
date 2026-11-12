# Python — zajęcia 2

Przypomnisz sobie typy danych, przećwiczysz wybór jednej z dwóch ścieżek za pomocą `if` i `else`, a następnie poznasz podstawy pętli `for` i `while`.

Każde zadanie zapisz w osobnym pliku `.py`. Każda linia przykładowego wejścia odpowiada jednemu wywołaniu `input()`. Używaj `input()` bez komunikatu w nawiasach. Możesz przyjąć, że użytkownik podaje dane zgodne z treścią zadania.

## Powtórzenie typów danych

| Typ | Przykład | Zastosowanie |
|---|---|---|
| `str` | `"Ada"` | Tekst |
| `int` | `12` | Liczba całkowita |
| `float` | `4.5` | Liczba zmiennoprzecinkowa |
| `bool` | `True`, `False` | Wynik warunku |

`input()` zwraca tekst. Przed obliczeniami zamień go na liczbę za pomocą `int()` lub `float()`. W liczbach zmiennoprzecinkowych wpisuj kropkę dziesiętną.

### Zadanie 1. Tekst i liczba

Wczytaj imię oraz wiek. Wypisz powitanie i wiek użytkownika za rok. Zapisz rozwiązanie w `zadanie_01.py`.

**Przykładowe wejście**

```text
Ada
19
```

**Przykładowe wyjście**

```text
Cześć, Ada!
Za rok: 20
```

Do umieszczania wartości wewnątrz tekstu możesz użyć f-stringa, np. `print(f"Cześć, {imie}!")`.

### Zadanie 2. Cena i liczba sztuk

Wczytaj cenę jednej sztuki jako `float` oraz liczbę sztuk jako `int`. Oblicz i wypisz koszt zakupu. Zapisz rozwiązanie w `zadanie_02.py`.

**Przykładowe wejście**

```text
2.5
4
```

**Przykładowe wyjście**

```text
Koszt: 10.0
```

### Zadanie 3. Wynik porównania

Wczytaj dwie liczby całkowite. Wypisz wartość logiczną informującą, czy pierwsza liczba jest większa od drugiej. Użyj operatora `>`. Przetestuj także dwie równe liczby. Zapisz rozwiązanie w `zadanie_03.py`.

**Przykładowe wejście**

```text
8
3
```

**Przykładowe wyjście**

```text
True
```

## Instrukcje `if` i `else`

Jeżeli warunek jest prawdziwy, program wykonuje blok `if`. W przeciwnym przypadku wykonuje blok `else`. Wykona się dokładnie jeden z tych dwóch bloków.

```python
liczba = int(input())

if liczba > 0:
    print("Liczba dodatnia")
else:
    print("Liczba niedodatnia")

print("Koniec sprawdzania")
```

`else` ustaw na tym samym poziomie wcięcia co odpowiadające mu `if`. Instrukcje wewnątrz obu bloków wsuń o cztery spacje. Ostatni `print()` wykona się niezależnie od wyniku warunku.

### Zadanie 4. Parzystość

Wczytaj liczbę całkowitą. Wypisz `Parzysta`, jeśli jest podzielna przez 2, albo `Nieparzysta` w przeciwnym przypadku. Użyj `if` i `else`. Operator `%` zwraca resztę z dzielenia, a `==` porównuje wartości. Przetestuj liczby 4, 5 i 0. Zapisz rozwiązanie w `zadanie_04.py`.

| Przykładowe wejście | Przykładowe wyjście |
|---|---|
| `4` | `Parzysta` |
| `5` | `Nieparzysta` |

### Zadanie 5. Próg zaliczenia

Wczytaj liczbę punktów. Jeśli student uzyskał co najmniej 10 punktów, wypisz `Zaliczone`. W przeciwnym przypadku wypisz `Niezaliczone` oraz liczbę brakujących punktów. Użyj `if` i `else`. Przetestuj wartości 9, 10 i 11. Zapisz rozwiązanie w `zadanie_05.py`.

**Przykładowe wejście A**

```text
7
```

**Przykładowe wyjście A**

```text
Niezaliczone
Brakuje punktów: 3
```

**Przykładowe wejście B**

```text
10
```

**Przykładowe wyjście B**

```text
Zaliczone
```

### Zadanie 6. Dzielenie

Wczytaj dwie liczby jako `float`. Jeśli druga liczba jest różna od zera, wypisz iloraz pierwszej przez drugą. W przeciwnym przypadku wypisz `Nie można dzielić przez zero`. Użyj `if` i `else`. Operator `!=` oznacza „różne od”. Zapisz rozwiązanie w `zadanie_06.py`.

**Przykładowe wejście A**

```text
9
2
```

**Przykładowe wyjście A**

```text
4.5
```

**Przykładowe wejście B**

```text
9
0
```

**Przykładowe wyjście B**

```text
Nie można dzielić przez zero
```

## Pierwsze pętle

Pętla pozwala wielokrotnie wykonać ten sam blok instrukcji. Tak jak w `if`, po nagłówku wpisujemy dwukropek i stosujemy wcięcia.

Pętla `for` przechodzi przez kolejne wartości. `range(3)` daje kolejno 0, 1 i 2, więc poniższy program trzykrotnie wypisze `Python`.

```python
for i in range(3):
    print("Python")
```

Pętla `while` powtarza blok, dopóki jej warunek jest prawdziwy. W poniższym programie licznik przyjmuje przed każdym wykonaniem bloku wartości 0, 1 i 2. Po zwiększeniu go do 3 warunek staje się fałszywy i pętla kończy działanie.

```python
licznik = 0

while licznik < 3:
    print("Python")
    licznik = licznik + 1
```

Jeśli usuniesz zwiększanie licznika, warunek pozostanie prawdziwy i pętla będzie działać bez końca. Program uruchomiony w terminalu możesz przerwać skrótem Ctrl+C.

### Zadanie 7. Powtarzanie komunikatu

Wczytaj nieujemną liczbę całkowitą `n`. Wypisz dokładnie `n` wierszy zawierających słowo `Python` oraz liczbę oddzieloną spacją. W pierwszym wierszu wypisz `Python 0`. W kolejnych wierszach wypisuj potęgi liczby 2, zaczynając od `2`, czyli kolejno `Python 2`, `Python 4`, `Python 8`, `Python 16` i tak dalej. Początkowe zero jest osobnym elementem ciągu. Do potęgowania służy operator `**`, np. `2 ** 3` daje `8`.

Napisz dwie wersje rozwiązania — z pętlą `for` w pliku `zadanie_07_for.py` i z pętlą `while` w pliku `zadanie_07_while.py`. Sprawdź obie wersje dla `n = 0`, `n = 1` i `n = 5`. Dla zera program ma zakończyć się bez wypisywania tekstu. Dla jedynki ma wypisać tylko `Python 0`.

**Przykładowe wejście**

```text
5
```

**Przykładowe wyjście obu wersji**

```text
Python 0
Python 2
Python 4
Python 8
Python 16
```

## Oddanie rozwiązań

1. Umieść wszystkie pliki `.py` z tej lekcji w folderze `zajęcia_2`.
2. Dodaj cały folder do swojego repozytorium na GitHubie i sprawdź, czy wszystkie pliki są widoczne.
3. Jeśli repozytorium jest prywatne, udostępnij je prowadzącemu. Wyślij prowadzącemu link do folderu `zajęcia_2` w repozytorium.
