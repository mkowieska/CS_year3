import random
import math
from collections import namedtuple

#zad1
# Napisz funkcję analizujProsokat, która na podstawie współrzędnych dwóch przeciwległych narożników prostokąta obliczy i zwróci jego obwód oraz pole powierzchni.
def analizujProsokat(x1, x2, y1, y2):
    szerokosc = abs(x1 - x2)
    wysokosc = abs(y1 - y2)
    obwod = 2 * (szerokosc + wysokosc)
    pole_powierzchni = szerokosc * wysokosc
    return obwod, pole_powierzchni

x1, y1 = 1, 2  
x2, y2 = 4, 5  
obwod, pole = analizujProsokat(x1, x2, y1, y2)
print('Obwod prostokata: ' + str (obwod))
print('Pole powierzchni prostokata: ' + str(pole))

#zad2
# Dodaj nazwaną krotkę (namedtuple) reprezentującą prostokąt w oparciu o jego dwa narożniki, a następnie nadpisz funkcję analizujProsokat przyjmującą  tylko jeden parametr krotkę prostokąt.
Prostokat = namedtuple('Prostokat', ['x1', 'x2', 'y1', 'y2'])

def analizujProsokat(prostokat):
    szerokosc = abs(prostokat.x1 - prostokat.x2)
    wysokosc = abs(prostokat.y1 - prostokat.y2)
    obwod = 2 * (szerokosc + wysokosc)
    pole_powierzchni = szerokosc * wysokosc
    return obwod, pole_powierzchni

p = Prostokat(x1=1, x2=4, y1=2, y2=5)
obwod, pole = analizujProsokat(p)
print("Obwod prostokata: " + str(obwod))
print("Pole powierzchni prostokata: " + str(pole))

#zad3
# Nie wykorzystując pętli wypełnij listę wartościami od 1 do 1001 z krokiem 2.
lista = list(range(1, 1001, 2))
print(lista)

"""
zad4
Utwórz listę wypełnioną wartościami od 1 do 10, a  następnie wykonaj jej kopie.
W celu sprawdzenia czy kopia została utworzona prawidłowo, zmień dowolną wartość w nowej liście i wyświetl obie listy.
"""
lista = list(range(1, 11))
kopia_listy = lista.copy()
kopia_listy[0] = 99  # Zmiana pierwszego elementu w kopii
print("Oryginalna lista: ", lista)
print("Kopia listy: ", kopia_listy)

"""
zad5
Utwórz dwie listy wypełnione losowymi wartosciami, pierwsza z nich liczbami całkowitymi, a druga zmiennoprzecinkowymi (ta część mo»e zosta¢ wykonana z użyciem pętli).
Następnie dodaj elementy z drugiej listy na koniec pierwszej bez wykorzystania pętli. 
Znajdź funkcje, która wybierze n-losowych próbek z utworzonej listy i wypisz trzy wylosowane próbki.
"""
lista_calkowite = [1, 2, 3, 4, 5]
lista_zmiennoprzecinkowe = [1.1, 2.2, 3.3, 4.4, 5.5]

lista_calkowite.extend(lista_zmiennoprzecinkowe)  # Łączenie list
print(lista_calkowite)

wylosowane_probki = random.sample(lista_calkowite, 3)  # Wybieranie 3 losowych próbek
print("Wylosowane probki:", wylosowane_probki)

"""
zad6
Wykorzystując listy zaimplementuj odległość Levenshteina, zdeniowaną następująco (wikipedia):
• działaniem prostym na napisie nazwiemy:
wstawienie nowego znaku do napisu,
usunięcie znaku z napisu,
zamianę znaku w napisie na inny znak,
• odległością pomiędzy dwoma napisami jest najmniejsza liczba działań prostych, przeprowadzających jeden napis na drugi, w oparciu o podany pseudokod wykorzystujący programowanie dynamiczne. 
Jaka jest odległość między słowami kot a kocioł?
"""
def odleglosc_levenshteina(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] != s2[j - 1]:
                substitution_cost = 1
            else:
                substitution_cost = 0

            dp[i][j] = min(
                dp[i - 1][j] + 1,  
                dp[i][j - 1] + 1,  
                dp[i - 1][j - 1] + substitution_cost  
            )

    return dp[m][n]

s1 = "kot"
s2 = "kociol"
odleglosc = odleglosc_levenshteina(s1, s2)
print("Odleglosc Levenshteina miedzy" + str(s1)+" a " + str(s2) + " : " + str(odleglosc))
