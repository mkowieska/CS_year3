# pobranie danych
imie = input ("Jak masz na imie? ") 
print ('Witaj ', imie)

"""
zad7
Pobierz od uytkownika nastepujace informacje: kierunek studiów, rok studiów, średnią uzyskaną w poprzednim semestrze studiów. 
Pamiętaj, aby dokonać odpowiedniej konwersji pobranych danych. 
Wyświetl pobrane informacje w następujęcej postaci: "Kierunek: xxx, Rok studiów: yyy, średnia: zzz"
"""
kierunek_studiow = str(input("Wpisz swoj kierunek studiow: "))
rok_studiow = int(input("Wpisz, na ktorym roku studiow jestes: "))
srednia_semestry = input("Wpisz jaka srednia uzyskales w poprzednim semestrze studiow: ")
print("Kierunek: " + kierunek_studiow + ', ' + "Rok studiow: " + str(rok_studiow) + ', ' + "Srednia: " + srednia_semestry)

"""
zad8
Pobierz od użytkownika: adres zamieszkania, kod pocztowy i miasto.
Wyświetl pobrane informacje w jednej linii rozdzielając je przecinkami. 
W tym celu zastosuj wywołanie funkcji print z odpowiednim parametrem.
"""
adres = input("Wpisz swoj adres zamieszkania: ")
kod_pocztowy = input("Wpisz swoj kod pocztowy: ")
miasto = input("Wpisz w jakim miescie mieszkasz: ")
print(adres, kod_pocztowy, miasto, sep=", ")

"""
zad9
Wykorzystując funkcje konwersji danych (int(), foat()) oraz funkcję input, utwórz skrypt, który pobierze od użytkownika jego wzrost w centymetrach oraz wagę w gramach, 
a następnie wyświetli wagę w kilogramach i wzrost w metrach wraz ze stosownym komunikatem oraz obliczy wskaźnik BMI i go wyświetli.
"""
wzrost_cm =input("Wpisz swoj wzrost w centymetrach: ")
waga_g =input("Wpisz swoja wage w gramach: ")
wzrost_m = float(wzrost_cm) / 100
waga_kg = float(waga_g) / 1000
bmi = waga_kg / (wzrost_m ** 2) #do drugiej potegi
print("Wzrost: " + str(wzrost_m) + "m", "Waga: " + str(waga_kg) + "kg", "Bmi: " + str(bmi), sep=", ")

#zad10
#Napisz program, bez wykorzystania instrukcji warunkowych, który pobierze od użytkownika pewną liczbę i sprawdzi, czy jej wartość jest większa od 10.
liczba = float(input("Wpisz liczbe: "))
czy_wieksza = liczba > 10
print("Czy wartosc liczby " + str(liczba) + " jest wieksza od 10? " + str(czy_wieksza))

#zad11
# Napisz program, bez wykorzystania instrukcji warunkowych, który pobierze od użytkownika pewną liczbę i sprawdzi, czy:
liczba = float(input("Podaj liczbe: "))
#a) podana liczba jest większa od 10 i jednocześnie mniejsza od 20;
czy_wieksza_10_i_mniejsza_20 = 10 < liczba < 20
#b) podana liczba jest mniejsza od 0 lub większa od 20.
czy_mniejsza_0_lub_wieksza_20 = liczba < 0 or liczba > 20

print("a) Czy liczba jest wieksza od 10 i jednoczesnie mniejsza od 20? " + str(czy_wieksza_10_i_mniejsza_20))
print("b) Czy liczba jest mniejsza od 0 lub wieksza od 20? " + str(czy_mniejsza_0_lub_wieksza_20))

