# Python — zajęcia 1

Na tych zajęciach przećwiczysz zmienne, typy `str`, `int`, `float` i `bool`, funkcje `print()` i `input()` oraz instrukcje `if` i `else`.

Każde rozwiązanie zapisz w osobnym pliku `.py`. W blokach „Wejście” każda linia odpowiada jednemu wywołaniu `input()`. Wypisuj wyniki w formacie pokazanym w blokach „Wyjście”. Używaj `input()` bez tekstu w nawiasach. W zadaniach liczbowych możesz przyjąć, że dane są poprawne.

## Przed zadaniami

- `print()` wypisuje wartości na ekranie. Argumenty oddzielone przecinkami pojawiają się w jednej linii, rozdzielone spacjami. Kolejne wywołanie domyślnie zaczyna nową linię.
- `input()` wczytuje jedną linię i zwraca ją jako tekst (`str`). Użyj `int(input())` dla liczby całkowitej lub `float(input())` dla liczby z częścią ułamkową.
- `if` wykonuje blok kodu, gdy warunek jest prawdziwy. `else` wykonuje drugi blok, gdy warunek jest fałszywy. Po nagłówkach wpisz dwukropek, a wiersze wewnątrz bloków wciśnij o cztery spacje.
- `=` przypisuje wartość do zmiennej, a `==` sprawdza, czy dwie wartości są równe.

```python
liczba = int(input())

if liczba == 0:
    print("Wpisano zero")
else:
    print("Wpisano liczbę:", liczba)
```

Dla wejścia `0` program wypisze `Wpisano zero`. Dla wejścia `3` wypisze `Wpisano liczbę: 3`.

## Zadanie 1. Zmienne i typy danych

Zapisz w czterech zmiennych nazwę użytkownika (`str`), liczbę punktów (`int`), czas wykonania w sekundach (`float`) i informację o zaliczeniu (`bool`). Wyświetl wartości za pomocą `print()`. Następnie zwiększ liczbę punktów o 2 i wypisz nową wartość. Zapisz rozwiązanie w `zadanie_01.py`.

**Wejście**

Brak. Ustaw wartości początkowe na `"Ada"`, `3`, `4.5` i `True`.

**Wyjście**

```text
Użytkownik: Ada
Punkty: 3
Czas: 4.5
Zaliczone: True
Punkty po aktualizacji: 5
```

## Zadanie 2. Powitanie

Wczytaj imię i kierunek studiów w dwóch osobnych liniach. Zapisz je w zmiennych i wypisz komunikat zawierający obie wartości. Zapisz rozwiązanie w `zadanie_02.py`.

**Wejście**

```text
Ada
informatyka
```

**Wyjście**

```text
Cześć, Ada! Twój kierunek to informatyka.
```

## Zadanie 3. Wiek za rok

Wczytaj wiek użytkownika i wypisz jego wiek za rok. Funkcja `input()` zwraca tekst, więc przed dodaniem `1` przekonwertuj odpowiedź na `int`. Zapisz rozwiązanie w `zadanie_03.py`.

**Wejście**

```text
19
```

**Wyjście**

```text
Za rok: 20
```

## Zadanie 4. Łączenie i dodawanie

Wczytaj dwie liczby całkowite jako tekst. W pierwszej linii wypisz wynik połączenia obu tekstów. W drugiej linii wypisz sumę tych samych wartości po konwersji na `int`. Dane wczytaj tylko raz. Zapisz rozwiązanie w `zadanie_04.py`.

**Wejście**

```text
2
3
```

**Wyjście**

```text
Połączenie: 23
Suma: 5
```

## Zadanie 5. Próg zaliczenia

Wczytaj liczbę punktów i przekonwertuj ją na `int`. Jeśli wynik wynosi co najmniej 10, wypisz `Zaliczone`. W pozostałych przypadkach wypisz `Niezaliczone`. Użyj `if` i `else`. Przetestuj wartości 9, 10 i 11. Zapisz rozwiązanie w `zadanie_05.py`.

**Przykład A**

| Wejście | Wyjście |
|---|---|
| `9` | `Niezaliczone` |

**Przykład B**

| Wejście | Wyjście |
|---|---|
| `10` | `Zaliczone` |

## Zadanie 6. Koszt zakupu

Wczytaj cenę jednej sztuki jako `float` i liczbę sztuk jako `int`. Wypisz ich iloczyn. W danych wejściowych użyj kropki dziesiętnej. Zapisz rozwiązanie w `zadanie_06.py`.

**Wejście**

```text
4.50
3
```

**Wyjście**

```text
Koszt: 13.5
```

## Zadanie 7. Druga próba

Zapisz liczbę `7` w zmiennej jako `int`. Wczytaj odpowiedź użytkownika na pytanie o liczbę dni w tygodniu i porównaj ją z zapisaną wartością. Użyj `==` do porównania. Jeśli odpowiedź jest poprawna, wypisz `Poprawna odpowiedź` i zakończ program. W przeciwnym razie wypisz `Druga próba`, wczytaj kolejną odpowiedź i wypisz `Poprawna odpowiedź` albo `Błędna odpowiedź`. Sprawdź również przypadek dwóch błędnych odpowiedzi. Zapisz rozwiązanie w `zadanie_07.py`.

**Wejście**

```text
6
7
```

**Wyjście**

```text
Druga próba
Poprawna odpowiedź
```

## Zadanie 8. Wynik z dwóch części

Wczytaj imię studenta i wyniki z dwóch części sprawdzianu jako liczby całkowite. Oblicz sumę punktów. Wypisz imię, sumę i status. Warunkiem zaliczenia jest co najmniej 15 punktów łącznie oraz co najmniej 5 punktów z każdej części. Użyj `if`, `else` i operatora `and`, który wymaga spełnienia wszystkich połączonych warunków. Zapisz rozwiązanie w `zadanie_08.py`.

**Wejście A**

```text
Ada
8
7
```

**Wyjście A**

```text
Student: Ada
Suma: 15
Status: Zaliczone
```

**Wejście B**

```text
Ada
12
4
```

**Wyjście B**

```text
Student: Ada
Suma: 16
Status: Niezaliczone
```

## Oddanie rozwiązań

1. Umieść wszystkie pliki `.py` z zajęć w folderze o nazwie `zajęcia_1`.
2. Dodaj cały folder `zajęcia_1` do swojego repozytorium na GitHubie. W repozytorium pliki powinny być widoczne pod ścieżkami `zajęcia_1/zadanie_01.py`, `zajęcia_1/zadanie_02.py` i tak dalej.
3. Sprawdź na GitHubie, czy folder zawiera wszystkie rozwiązania. Jeśli repozytorium jest prywatne, udostępnij je prowadzącemu.
4. Wyślij prowadzącemu link do folderu `zajęcia_1` w repozytorium.
