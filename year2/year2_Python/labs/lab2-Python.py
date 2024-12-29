import math

#zad1
#Utwórz liste zawierającą 6 elementów 0, −2, 1, 7, 3, 4, a nastepnie wypisz jej zawartosc w odwrotnej kolejności, bez stosowania funkcji, czy petli.
lista = [0,-2,1,7,3,4]
print(lista[::-1])

"""
zad2
Zaimportuj modul matematyczny, a nastepnie napisz skrypt, którzy pobierze wartości dla dwóch zmiennych x, y. 
Wyznaczy oraz wyświetli wartość, dla podanej funkcji:
w komentarzu podaj wartość dla x = 2, y = 4 oraz x = -9.5, y = 6.4.
"""
def oblicz_wartosc(x, y):
    wynik = (math.exp(1)) + (math.log10((x**2) + 1)) * ((x - 1 ) / (math.cos((y**3) - 1) + 6))
    return wynik
x1 = 2
y1 = 4
x2 = -9.5
y2 = 6.4
wynik1 = oblicz_wartosc(x1, y1)
wynik2 = oblicz_wartosc(x2, y2)
print('Wartosc dla x = ' + str(x1) , 'y = ' + str(y1) , "\nWynik = " + str(wynik1), sep = ', ')
print('Wartosc dla x = ' + str(x2) , 'y = ' + str(y2) , "\nWynik = " + str(wynik2), sep = ', ')

"""
#zad3
Napisz skrypt, który pobierze od użytkownika trzy wartości x, y, z oraz numer opcji c. 
Jeśli c == 1 zwróć ich sumę, jeżeli c == 2 różnicy, dla c == 3 iloczyn, a w przeciwnym razie iloraz. 
Upewnij się, że nie dojdzie do dzielenia przez 0, jeśli taka sytuacja miała by miejsce, wyświetl odpowiedni komunikat.
"""
x = int(input('Wpisz wartosc x: '))
y = int(input('Wpisz wartosc y: '))
z = int(input('Wpisz wartosc z: '))
print('Numeru opcji c \n1 to obliczenie sumy \n2 to obliczenie roznicy\n3 to obliczenie iloczynu \n inna odpowiedz to obliczenie ilorazu')
c = int(input('Wpisz numer opcji c: '))
if c==1 :
   suma =  x + y + z
   print("Suma = " + str(suma))
elif c==2 :   
    roznica = x - y - z
    print("Roznica = " + str(roznica))
elif c==3 :   
    iloczyn = x * y * z
    print("Iloczyn = " + str(iloczyn))
else:
    if y==0 or z==0 :
        print('Blad. Dzielenie przez 0.')
    else:
        iloraz = x / y / z
        print("Iloraz = " + str(iloraz))
     
#zad4
#Rozszerz zadanie z poprzednich laboratoriów, które dotyczyło wyznaczania współczynnika BMI o wyświetlanie dodatkowej informacji o kategorii wagowej w zależności od wartości obliczonego BMI:
wzrost_cm =input("Wpisz swoj wzrost w cm: ")
waga_g =input("Wpisz swoja wage w g: ")
wzrost_m = float(wzrost_cm) / 100
waga_kg = float(waga_g) / 1000
bmi = waga_kg / (wzrost_m ** 2) 
print("Wzrost: " + str(wzrost_m) + "m" " Waga: " + str(waga_kg) + "kg")
print("Bmi: " + str(bmi))
if bmi < 16:
    print("Wyglodzenie")
elif 16 <= bmi < 17:
    print("Wychudzenie")
elif 17 <= bmi < 18.5:
    print("Niedowaga")
elif 18.5 <= bmi < 25:
    print("Waga prawidlowa")
elif 25 <= bmi < 30:
    print("Nadwaga")
elif 30 <= bmi < 35:
    print("Otylosc stopnia I")
elif 35 <= bmi < 40:
    print("Otylosc stopnia II")
else:
    print("Otylosc stopnia III")

"""
zad5
Napisz program drukujący na ekranie trójkąt o wysokości podanej przez użytkownika. Przykładowy trójkąt o wysokości 4:
X
XX
XX X
XXXX
"""
wysokosc = int(input('Wypisz jakiej wysokosci ma byc trojkat: '))
for i in range(1, wysokosc + 1): #funkcja służąca do generowania sekwencji liczb
    print("X" * i)

""" 
zad6
Utwórz poniższą macierz, wykorzystując jedną linijkę kodu (dwie pętlę for inicjalizujące listę):
1 4 7
1 4 7
1 4 7
"""
macierz = [[1, 4, 7] for _ in range(3)]
for wiersz in macierz:
    print(" ".join(map(str, wiersz))) 
    #join metoda ciągu znaków, która łączy elementy danej sekwencji w jedną ciągłą sekwencję
    #map funkcja wbudowana, która stosuje daną funkcję do każdego elementu sekwencji (np. listy) i zwraca nową listę z wynikami

#zad7 
# Napisz program, który znajdzie i wyswietli n pierwszych liczb pierwszych (zakladajac, ze pierwsza liczba pierwsza jest liczba 2).
def czy_pierwsza(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def pierwsze_n_liczb(n):
    liczba = 2
    liczby_pierwsze = []
    while len(liczby_pierwsze) < n:
        if czy_pierwsza(liczba):
            liczby_pierwsze.append(liczba)
        liczba += 1
    return liczby_pierwsze

n = int(input("Podaj liczbę pierwszych liczb pierwszych do znalezienia: "))
liczby_pierwsze = pierwsze_n_liczb(n)
print(str(n) + ' pierwszych liczb pierwszych to: ')
for liczba in liczby_pierwsze:
    print(liczba, end=" ")

#zad8 
# Napisz program, który wyznaczy i wyswietli na ekranie sumy liczb naturalnych mniejszych od n (liczba n podawana jest przez uzytkownika), które sa zakonczone liczba 3 lub 14.
def suma_liczb_zakonczonych_w_3_lub_14(n):
    suma = 0
    for i in range(1, n):
        if str(i).endswith("3") or str(i).endswith("14"):
            suma += i
    return suma

n = int(input("Podaj liczbe n: "))
wynik = suma_liczb_zakonczonych_w_3_lub_14(n)
print('Suma liczb naturalnych mniejszych od '+ str(n) + ' zakonczonych cyframi 3 lub 14 wynosi: ' + str(wynik))

#zad9
# Napisz program, który wyświetli na ekranie n pierwszych wierszy trójkąta Pascala (liczba n podawana jest przez użytkownika)
def trojkat_pascala(n):
    trojkat = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            trojkat[i][j] = trojkat[i - 1][j - 1] + trojkat[i - 1][j]
    return trojkat

n = int(input("Podaj liczbe wierszy trojkata Pascala: "))
wynik = trojkat_pascala(n)
for wiersz in wynik:
    print(wiersz)
