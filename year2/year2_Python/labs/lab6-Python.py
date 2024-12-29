from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import deque

#Zadanie 1
#Zliczanie wystąpień słów w tekście.
#Korzystając ze słownika typu Counter z pakietu collections zlicz wystąpienia słów z poniższego tekstu (podobnie jak na poprzednich zajęciach tekst wymaga podstawowej obróbki: zmiana wielkości liter, usunięcie kropek oraz przecinków).
tekst = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dolor sed viverra ipsum nunc aliquet bibendum enim. In massa tempor nec feugiat. Nunc aliquet bibendum enim facilisis gravida. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Amet luctus venenatis lectus magna fringilla. Volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in. Egestas egestas fringilla phasellus faucibus scelerisque eleifend. Sagittis orci a scelerisque purus semper eget duis. Nulla pharetra diam sit amet nisl suscipit. Sed adipiscing diam donec adipiscing tristique risus nec feugiat in. Fusce ut placerat orci nulla. Pharetra vel turpis nunc eget lorem dolor. Tristique senectus et netus et malesuada.'''

tekst = tekst.lower().replace(".", "").replace(",", "") #Zamiana na małe litery, usunięcie kropek i przecinków
slowa = tekst.split() # podział na słowa

licznik = Counter(slowa)

print(licznik)

#Zadanie 2
# Obliczanie prawdopodobieństw wystąpienia poszczególnych wartości dla każdej z kolumn (liczba wystąpie« wartości w danej kolumnie / liczba wierszy). W tym celu posłuż się słownikiem Counter
dane = [
    ("sunny", 85, 85, "FALSE", "no"),
    ("sunny", 80, 90, "TRUE", "no"),
    ("overcast", 83, 86, "FALSE", "yes"),
    ("rainy", 70, 96, "FALSE", "yes"),
    ("rainy", 68, 80, "FALSE", "yes"),
    ("rainy", 65, 70, "TRUE", "no"),
    ("overcast", 64, 65, "TRUE", "yes"),
    ("sunny", 72, 95, "FALSE", "no"),
    ("sunny", 69, 70, "FALSE", "yes"),
    ("rainy", 75, 80, "FALSE", "yes"),
    ("sunny", 75, 70, "TRUE", "yes"),
    ("overcast", 72, 90, "TRUE", "yes"),
    ("overcast", 81, 75, "FALSE", "yes"),
    ("rainy", 71, 91, "TRUE", "no")
]

# Przetwarzanie danych i obliczanie prawdopodobieństw
prawdopodobienstwa = {}
liczba_wierszy = len(dane)

for kolumna in range(1, len(dane[0]) - 1):
    wartosci = [rekord[kolumna] for rekord in dane]
    licznik = Counter(wartosci)
    prawdopodobienstwa[f"Kolumna {kolumna}"] = {wartosc: liczba / liczba_wierszy for wartosc, liczba in licznik.items()}

print(prawdopodobienstwa)

#Zadanie 3 
# Sortowanie wyników w słownikach Counter za pomocą OrderedDict.
tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
tekst = tekst.lower().replace(".", "").replace(",", "")
slowa = tekst.split()
licznik = Counter(slowa)

# Sortowanie licznika według wartości
posortowany_licznik = OrderedDict(sorted(licznik.items(), key=lambda x: x[1], reverse=True))

print(posortowany_licznik)

#Zadanie 4
# Zwiększanie wartości w słowniku defaultdict.
def zwiększ_wartosc(słownik, klucz):
    słownik[klucz] += 1

słownik = defaultdict(int)
klucze = [1, 2, 3, 4, 5]

for klucz in klucze:
    zwiększ_wartosc(słownik, klucz)

print(słownik)

#Zadanie 5
# Sprawdzanie, czy wyraz jest palindromem.
def czy_palindrom(wyraz):
    wyraz = wyraz.lower()
    wyraz = wyraz.replace(" ", "")  # Usunięcie spacji
    kolejka = deque(wyraz)
    while len(kolejka) > 1:
        if kolejka.popleft() != kolejka.pop():
            return False
    return True

wyraz = input("Podaj wyraz do sprawdzenia: ")
if czy_palindrom(wyraz):
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")
#Ten kod używa kolejki dwustronnej deque do sprawdzania, czy podany wyraz jest palindromem.Usuwa spacje i porównuje znaki z obu stron kolejki, aż dojedzie do środka wyrazu. Jeśli wszystkie pary znaków są takie same, wyraz jest uważany za palindrom.