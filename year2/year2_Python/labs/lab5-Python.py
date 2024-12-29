import base64

#Zadanie 1
# Utwórz napis o treści:
tekst = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dolor sed viverra ipsum nunc aliquet bibendum enim. In massa tempor nec feugiat. Nunc aliquet bibendum enim facilisis gravida. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Amet luctus venenatis lectus magna fringilla. Volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in. Egestas egestas fringilla phasellus faucibus scelerisque eleifend. Sagittis orci a scelerisque purus semper eget duis. Nulla pharetra diam sit amet nisl suscipit. Sed adipiscing diam donec adipiscing tristique risus nec feugiat in. Fusce ut placerat orci nulla. Pharetra vel turpis nunc eget lorem dolor. Tristique senectus et netus et malesuada."""
tekst = tekst.lower().replace(".", "").replace(",", "")  #Zamiana na małe litery, usunięcie kropek i przecinków
slowa = tekst.split() # podział na słowa
unikatowe_slowa = set(slowa) # Znalezienie unikatowych słów przy użyciu zbioru (set)
print("Ilosc oryginalnych slow: " + str(len(slowa)))
print("Ilosc unikatowych slow: " + str(len(unikatowe_slowa)))

#Zadanie 2
# Utwórz dwa zbiory:
A = {1, 2, 3, 4, 5}
B = {2, 4, 5}
# Sprawdzenie, czy A jest podzbiorem B
czy_podzbiór = A.issubset(B)
print("A jest podzbiorem B: " + str(czy_podzbiór))
# Sprawdzenie, czy A jest nadzbiorem B
czy_nadzbiór = A.issuperset(B)
print("A jest nadzbiorem B: " + str(czy_nadzbiór))
# Przecięcie A i B
przeciecie = A.intersection(B)
print("Przeciecie A i B: " + str(przeciecie))
# Suma zbiorów A i B
suma = A.union(B)
print("Suma zbiorow A i B: " + str(suma))
# Różnica zbiorów A i B
roznica = A.difference(B)
print("Roznica zbiorow A i B: " + str(roznica))
# Różnica symetryczna zbiorów A i B
roznica_symetryczna = A.symmetric_difference(B)
print("Roznica symetryczna zbiorow A i B: " + str(roznica_symetryczna))

#Zadanie 3 
# Wyznacz iloczyn kartezjański zbiorów A i B.
iloczyn_kartezjanski = {
    (a, b) for a in A for b in B
    }
print("Iloczyn kartezjanski A i B: " + str(iloczyn_kartezjanski))

#Zadanie 4
# Wykorzystując słownik napisz skrypt, który zapyta o liczbę z zakresu < 0, 99 >, a następnie wyświetli jej słowną reprezentację. Słownik nie powinien zawierać wszystkich kombinacji liczb
slownik_liczby = {
    0: "zero",
    1: "jeden",
    2: "dwa",
    3: "trzy",
    4: "cztery",
    5: "piec",
    6: "szesc",
    7: "siedem",
    8: "osiem",
    9: "dziewiec"
}
liczba = int(input("Podaj liczb od 0 do 99: "))

dziesiatki = liczba // 10  # to operator dzielenia całkowitego 47
jednosci = liczba % 10  #to operator reszty z dzielenia 7

reprezentacja = ""
if dziesiatki > 0:
    reprezentacja += slownik_liczby[dziesiatki] + "dziesiat "
if jednosci > 0:
    reprezentacja += slownik_liczby[jednosci]

print("Slowna reprezentacja liczby " + str(liczba) + " to " + str(reprezentacja))

#Zadanie 5
# Implementacja kodowania Base64.
def custom_base64_encode(text):
    bytes_text = text.encode('ascii') # Zamiana na bajty
    base64_encoded = base64.b64encode(bytes_text)  # Kodowanie Base64
    return base64_encoded.decode('ascii')

napis = "TEST"
base64_encoded = custom_base64_encode(napis)
print("Base64('" + str(napis) + "') to '" + str(base64_encoded))