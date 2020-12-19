import random

# def gra_w_kosci():
#     print( f'kość 1 {random.randint(1,6)}')
#     print(f'kość 2 { random.randint(1,6)}')

# gra_w_kosci()

obiekty=['kamień','papier','nożyce']

#komputer losuje swoj obiekt
def losowanie_komputera():
    wybor_komputera = obiekty[random.randint(0,2)]
    return wybor_komputera

#człowiek wybiera swoj obiekt
def losowanie_czlowieka():
    print('1-kamień\2-papier\3-nożyce')
    wybor_czlowieka = obiekty[int(input('Podaj numer od 1 do 3, aby wybrać obiekt:'))-1]
    return wybor_czlowieka


def sprawdzenie_wynikow(losowanie_komputera,losowanie_czlowieka):
    print(losowanie_czlowieka)
    print(losowanie_komputera)
    
    if losowanie_komputera == losowanie_czlowieka:
        print('Remis')
    elif losowanie_czlowieka == 'kamień':
            if losowanie_komputera  == 'papier':
                print('Komputer wygrał')
            elif losowanie_komputera == 'nożyce':
                print('Człowiek wygrał')
    elif losowanie_czlowieka == "papier":
            if losowanie_komputera  == 'nożyce':
                print('Komputer wygrał')
            elif losowanie_komputera == 'kamień':
                print('Człowiek wygrał')
    elif losowanie_czlowieka == "nożyce":
            if losowanie_komputera  == 'papier':
                print('Człowiek wygrał')
            elif losowanie_komputera == 'kamień':
                print('Komputer wygrał')
    
#następuje porównanie wyników
#ewaluacja
# 1. kamien - papier -> papier
# 2. papier - nożyce -> nożyce
# 3. nożyce - kamień -> kamień
# 4. kamień - kamień -> remis
# 5. nożyce - nożyce -> remis
# 6. papier - paier ->  remis

#wyświetlenie wyniku
def start_gry():
    lk = losowanie_komputera()
    lc = losowanie_czlowieka()
    sprawdzenie_wynikow(lk,lc)
    
start_gry()