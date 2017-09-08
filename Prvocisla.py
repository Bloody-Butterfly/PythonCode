import math


# Tested:
def poznej_prvocislo(x):
    if x % 2 == 0:
        return False
    for y in range(3, math.ceil(x / 2), 2):
        if x % y == 0:
            return False
    return True

def poznej_prvocislo2(x, bublifuk):
    z = x / 2
    for y in bublifuk:
        if y > z:
            return True
        if x % y == 0:
            return False
    return True


def vypis_prvocisla(t):
    cisla = list()

    if t == 0:
        print("[]")
        return

    cisla.append(2)
    z = 3
    while z > 1:
        if len(cisla) < t:
            if poznej_prvocislo2(z, cisla):
                cisla.append(z)
        else:
            break
        z += 1
    print(cisla)


def zobraz_menu():
    print("\n\n--------------")
    print("1: Je to prvočíslo?")
    print("2: Vypiš provočísla!")
    print("3: Ukonči!")
    vlozil = input()
    vlozil = int(vlozil)

    if vlozil == 1:
        print("Vložte číslo, o kterém chcete vědět, jestli je to prvočíslo:")
        cislo = input()
        if poznej_prvocislo(int(cislo)):
            print("Je to prvočíslo!")
        else:
            print("Není to prvočíslo!")
        zobraz_menu()

    elif vlozil == 2:
        print("Vložte množství prvočísel, která chcete vypsat: ")
        vypis_prvocisla(int(input()))
        zobraz_menu()

    elif vlozil == 3:
        print("Ukončuji.... Bye bye... ZZZ.... Im sleeping now!.... Buahuaaaaaaaaa")

    else:
        print("Ty demente, chci číslo 1-3!")
        zobraz_menu()


if __name__ == "__main__":
    zobraz_menu()
