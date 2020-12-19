#Napisz kod generujący 2 liczby i spytaj użytkownika o ich różnicę
# W przypadku powodzenia wyświetl komunikat
import random
from zipfile import *

def losowe():
    a = random.randint(1,100)
    print("1 Wysolowana liczba:", a)
    b= random.randint(1,100)
    print("2 Wylosowana liczba:", b)
    liczba =int (input("Podaj różnicę tych liczb: "))
    roznica = a-b
    punkty =0
    if liczba == roznica:
        punkty+= 1
        print("Zdobywasz punkt!")
        print(f'Twoja liczba punktów to {punkty}')
    else:
        print("Nie zdobywasz punktu!")

def zapis_losowy():
    plik= open("liczbaLosowa.txt","w")
    plik.write(str(random.randint(1,1000)))
    plik.write("\n")
    plik.close()

# zapis_losowy()

#wygenerowac liczbe od 1 do 1000
# zapisaac wygenerowane liczby 10 x oddzielając śrdnikiem
# zapisać w 3 liniach  
# 12;23;1;543;4;34;34;453;435;243;
# 12;23;1;543;4;34;34;453;435;243;
# 12;23;1;543;4;34;34;453;435;243;

def zapis_losowy_csv():
    plik= open("liczbaCsv.csv","w")
    for a in range(3):
        for i in range(10):
            plik.write(str(random.randint(1,1000)))
            plik.write(";")
        plik.write("\n")
    plik.close()

# zapis_losowy_csv()


def zapis_losowy_xrazy_csv():
    for p in range(10):
        plik= open(f"liczbaCsv{p}.csv","w")
        for a in range(3):
            for i in range(10):
                plik.write(str(random.randint(1,1000)))
                plik.write(";")
            plik.write("\n")
        plik.close()

# zapis_losowy_xrazy_csv()

def czytaj_losowy_plik():
    for p in range(15):
        try:
            plik= open(f"liczbaCsv{p}.csv","r")
            print(plik.read())
            plik.close()
        except:
            print(f"W folderze nie ma pliku liczbaCsv{p}.csv")

# czytaj_losowy_plik() 

def dziel_dwie_liczby(a,b):
    try:
        wynik=a/b
    except:
        print("Coś poszło nie tak")

# dziel_dwie_liczby(10,0)
def pakuj():
    with ZipFile("pliki_spakowane.zip","w") as z:
        z.write('liczbaCsv.csv')
        z.write('liczbaCsv0.csv')
        z.write('liczbaCsv1.csv')
        z.close()

pakuj()