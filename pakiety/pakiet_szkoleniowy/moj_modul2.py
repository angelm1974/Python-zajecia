import time
import locale
# Korzystając z bibiloteki time oraz metody sleep():

# Program 1
# Napisz program, który odlicza od 1 do 5, wypisując liczby co sekundę. 

def count_down1(number):
    for i in range(number):
        print(i+1)
        time.sleep(1)
#count_down(5)

# for a in range(1,6):
#     time.sleep(1)
#     print(a)
    
# x = 1
# while x < 6:
#     print(x)
#     x +=1
#     time.sleep(1)

# Program 2
# Napisz podobny program który odlicza od 1 do 5, wypisując liczby co sekundę. 
# Dodatkowo liczba zapisywana jest do zmiennej T inkrementując ją za każdym razem o swoją wartość

def dodawanie_do_zmiennej1(number):
    T = 0
    for i in range(1, number+1):
        T += i
        print(f'sekundy:{i},  Suma: {T}')
        time.sleep(1)
        
#wywołanie metody z parametrem
#dodawanie_do_zmiennej(5)

# Program 3
# Napisz podobny program który pobiera liczbę sekund od użytkownika i jeśli użytkownik podał
# liczbę mniejszą od 10 to program zatrzyma się na tak długo jaką użytkownik podał liczbę.
# Jeżeli liczba jest większa od 10 to użytklownik otrzyma komunikat że program nie będzie 
# czekał tak długo
def pobierz_czekaj1(number):
    if number<10:
        print(f'Będę czekał {number} sekund.')
        time.sleep(number)
        print('Koniec czekania!')
    else:
        print('Nie będę czekał tak długo!')
        
def pobierz_czekaj21():
    number=int(input("Podaj ile sekund mam poczekać:"))
    if number<10:
        print(f'Będę czekał {number} sekund.')
        time.sleep(number)
        print('Koniec czekania!')
    else:
        print('Nie będę czekał tak długo!')
#wywołanie metody pobierz_czekaj
#pobierz_czekaj2()

# Program 4
# Napisz program który przy pomocy bibiloteki time i funkcji gmtime() pobiera aktualną datę
def pobierz_date1():
    data= time.gmtime()
    print(data.tm_year,'-',data.tm_mon,'-',data.tm_mday)


# Program 5
# Napisz program który przy pomocy bibiloteki time i funkcji strftime() pobiera aktualną datę
def pobierz_pelna_date1():
    locale.setlocale(locale.LC_ALL,'')
    print(time.strftime("%A %d %B %Y %H:%M:%S"))

# Program 6
# Napisz program używając metody time(), który zapamiętuje czas, a następnie prosi użytkownika
# o wpisanie wyniku mnożenia liczb 5x6. Potem pobiera nowy czas, liczy różnicę czasów
# i wyświetla je na ekranie.

def czas_reakcji1():
    czas =time.time()
    wynik=int(input("Podaj wynik działana 5x6:"))
    czas2=time.time()
    if wynik==30:
        print(f'Potrzebowałeś {czas2-czas}sekund na rozwiązanie zadania')
    else:
        print(f'Popełniłeś błąd!!!')

