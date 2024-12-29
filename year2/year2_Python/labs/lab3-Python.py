import math

#zad1
# Napisz funkcję, która przyjmuje na wejście wartość w sekundach, a zwraca czas w postaci "x godzin, y minut, z sekund".
def zamiana(sekundy):
    minuty=sekundy//60
    reszta_sekundy = sekundy % 60
    godziny=sekundy//3600
    reszta_sekundy = sekundy % 3600
    return str(godziny) + ' godzin,' + str(minuty) + ' minut,' + str(reszta_sekundy) + ' sekund'
czas_w_sekundach = int(input('Wpisz wartosc w sekundach: '))
wynik = zamiana(czas_w_sekundach)
print(wynik)

"""
zad2
Napisz funkcję wyznaczają wartość poniższego wzoru, posiadającą dwa opcjonalne parametry: stopień logarytmu domyślnie 10, wartość k domyślnie 2.
f(x, n, k) = logn(x^2 + 5) · (k + 1) · x.
Wywołaj funkcję dla x = 2, k = 7 stosując argumenty nazwane.
"""
def zadanie2(x,n=10,k=2):
    wynik2 = math.log(x**2 +5,n)*(k+1)*x
    return wynik2
wynik2 = zadanie2(x=2,k=7)
print('Wynik to '+ str(wynik2))

"""
zad3
Wykorzystaj funkcję lambda do zaimplementowania następującego wzoru:
f(x) = sin(x + 1) + cos(x^4).
Oblicz wartość dla liczb całkowitych z przedziału < −5, 2 >, wynik zapisz w liści
"""
zad3 = lambda x: math.sin(x+1)+math.cos(x**4)
wyniki3 = []
for x in range(-5,2):
    wynik3 = zad3(x)
    wyniki3.append(wynik3)
print('Wyniki to ' + str(wyniki3))


#zad4
#Napisz funkcję, która przyjmie dowolną liczbę argumentów typu integer i wyznaczy oraz zwróci ich sumę.
def zad4(*args):
    wynik4=sum(args)
    return wynik4
wynik31 = zad4(1,2)
wynik32 = zad4(2,4,10)
print(wynik31)
print(wynik32)

#zad5
#Napisz funkcję, która oblicza objętości brył: kuli, prostopadłościanu, walca, stożka wykorzystuj¡c wyrażenie kwargs. Przetestuj napisaną funkcję dla każdej z brył
def oblicz_objetosc_bryly(bryla, **kwargs):
    if bryla == "kula":
        r = kwargs.get("promien", 1.0)
        objetosc = (4/3) * math.pi * r**3
    elif bryla == "prostopadloscian":
        a = kwargs.get("dlugosc", 1.0)
        b = kwargs.get("szerokosc", 1.0)
        h = kwargs.get("wysokosc", 1.0)
        objetosc = a * b * h
    elif bryla == "walec":
        r = kwargs.get("promien", 1.0)
        h = kwargs.get("wysokosc", 1.0)
        objetosc = math.pi * r**2 * h
    elif bryla == "stozek":
        r = kwargs.get("promien", 1.0)
        h = kwargs.get("wysokosc", 1.0)
        objetosc = (1/3) * math.pi * r**2 * h
    else:
        objetosc = None
        print("Nieznana bryła")
    
    return objetosc

print("Objetosc kuli o promieniu 2:", oblicz_objetosc_bryly("kula", promien=2))
print("Objetosc prostopadloscianu o wymiarach 2x3x4:", oblicz_objetosc_bryly("prostopadloscian", dlugosc=2, szerokosc=3, wysokosc=4))
print("Objetosc walca o promieniu 1 i wysokosci 5:", oblicz_objetosc_bryly("walec", promien=1, wysokosc=5))
print("Objetosc stożka o promieniu 3 i wysokosci 4:", oblicz_objetosc_bryly("stozek", promien=3, wysokosc=4))

#lub
def oblicz_objetosc_kuli(r):
    objetosc = (4/3)*math.pi*(r**3)
    return objetosc

def oblicz_objetosc_prostopadloscianu(a,b,wysokosc):
    objetosc = a * b * wysokosc
    return objetosc

def oblicz_objetosc_walca(r,h):
    objetosc = math.pi*(r**2)*h
    return objetosc

def oblicz_objetosc_stozka(r,h):
    objetosc = (1/3)*math.pi*(r**2)*h
    return objetosc

print(oblicz_objetosc_kuli(2))
print(oblicz_objetosc_prostopadloscianu(3,4,5))
print(oblicz_objetosc_walca(2,6))
print(oblicz_objetosc_stozka(3,4))

#zad6
#Napisz jedną linijkę kodu, która pozwoli rozpakowa¢ cztery wartości z listy do osobnych zmiennych na dwa sposoby: bez zastosowania funkcji oraz z zastosowaniem funkcji.
#bez zastosowania funkcji 
lista = [1, 2, 3, 4]
a, b, c, d = lista
##z zastosowaniem funkcji
def rozpakowanie(lista):
    a, b, c, d = lista
    return a, b, c, d

lista = [1, 2, 3, 4]  
a, b, c, d = rozpakowanie(lista)

#zad7
#Napisz funkcję obliczającą silnię na dwa sposoby: z wykorzystaniem rekurencji oraz wersję tradycyjną.
#rekurencja
def silnia_rekurencyjnie(n):
    if n == 0:
        return 1
    else:
        return n * silnia_rekurencyjnie(n - 1)
#tradycyjnie
def silnia_tradycyjnie(n):
    if n == 0:
        return 1
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

"""
zad8
Zaimplementuj funkcję obliczająca w sposób rekurencyjny n-ty wyraz ciągu Tribonacciego.
        0                  dla n = 0
Fn ={   0                  dla n = 1
        1                  dla n = 2
        Fn−1 + Fn−2 + Fn−3 dla n > 2
"""
def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
m=5
wynik = tribonacci(m)
print('N-ty wyraz ciagu Tribonacciego dla n = '+ str(m) + ' to ' + str(wynik))