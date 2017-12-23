import time


def yl1():
    nimi = input("Nimeta end: ")

    if nimi == "Edgar":
        print("Tere, " + str(nimi))
    elif nimi == "Kersti Kaljulaid":
        print("Elagu Eesti, proua president!")
    else:
        print("Ma ei tea Teid, " + str(nimi))


def yl2():
    talvekuud = ["jaanuar", "veebruar", "detsember"]
    kevadkuud = ["märts", "aprill", "mai"]
    suvekuud = ["juuni", "juuli", "august"]
    sügiskuud = ["september", "oktoober", "november"]

    kuu = input("Sisesta kuu nimi: ")
    if kuu in talvekuud:
        print(kuu.title() + " on talvekuu")
    elif kuu in kevadkuud:
        print(kuu.title() + " on kevadkuu")
    elif kuu in suvekuud:
        print(kuu.title() + " on suvekuu")
    elif kuu in sügiskuud:
        print(kuu.title() + " on sügiskuu")
    else:
        print("Vigane kuu")


def yl3():
    arv = input("Sisesta arv: ")

    if int(arv) < 0:
        print("Negatiivne arv")
    elif int(arv) > 0:
        print("Positiivne arv")
    elif int(arv) == 0:
        print("See on null!!!")


def yl4_1():
    while True:
        nimi = input("Nimeta end: ")
        if nimi == "Edgar":
            print("Tere, " + str(nimi))
        elif nimi == "Kersti Kaljulaid":
            print("Elagu Eesti, proua president!")
        elif nimi == "stopp":
            break
        else:
            print("Ma ei tea Teid, " + str(nimi))


def yl4_2():
    talvekuud = ["jaanuar", "veebruar", "detsember"]
    kevadkuud = ["märts", "aprill", "mai"]
    suvekuud = ["juuni", "juuli", "august"]
    sügiskuud = ["september", "oktoober", "november"]

    while True:
        kuu = input("Sisesta kuu nimi: ")
        if kuu in talvekuud:
            print(kuu.title() + " on talvekuu")
        elif kuu in kevadkuud:
            print(kuu.title() + " on kevadkuu")
        elif kuu in suvekuud:
            print(kuu.title() + " on suvekuu")
        elif kuu in sügiskuud:
            print(kuu.title() + " on sügiskuu")
        elif kuu == "stopp":
            break
        else:
            print("Vigane kuu")


def yl4_3():
    while True:
        arv = input("Sisesta arv: ")

        if int(arv) < 0:
            print("Negatiivne arv")
        elif int(arv) > 0:
            print("Positiivne arv")
        elif int(arv) == 0:
            print("See on null!!!")
        elif arv == "stopp":
            break





def yl5a():
    i = 10
    while True:
        if i > 0:
            print(i)
            i -= 1
            time.sleep(1)
        else:
            print("Aeg on otsas!")
            break


def yl5b():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("Aeg on otsas!")


def yl5b2():
    arvud = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    for i in arvud:
        if i > 0:
            print(i)
            time.sleep(1)
        else:
            print("Aeg on otsas!")


def yl6():
    pin = "1234"
    kontojääk = 234.5
    logitud = False
    katseid = 3
    while True:
        pinkood = input("Sisestage palun enda pin kood: ")
        if pinkood == pin:
            print("Pin kood on õige!")
            logitud = True
            break
        else:
            katseid -= 1
            if katseid > 0:
                print("Sisestatud pin on vale! Katseid jäänud " + str(katseid))
                time.sleep(1)
            else:
                print("Sisestatud pin on vale! Kaart blokeeritakse!")
                break

    if logitud:
        while True:
            käsk = input("Palun sisestage operatsioon (lõpp, raha välja, raha sisse, kontojääk): ")
            if käsk == "lõpp":
                print("Programm lõpetab töö!")
                break
            elif käsk == "raha välja":
                while True:
                    raha = input("Sisestage soovitud summa: ")
                    if int(raha) > kontojääk:
                        print("Teil pole piisavalt raha, sisestage uus summa!")
                    else:
                        print("Väljastatud " + raha + " eurot")
                        kontojääk -= int(raha)
                        break
            elif käsk == "raha sisse":
                sisse = input("Sisestage sisestatav summa: ")
                kontojääk += int(sisse)
                print("Kontole lisatud " + str(sisse) + " eurot!")
            elif käsk == "kontojääk":
                print("Teie kontol on " + str(kontojääk) + " eurot!")
            else:
                print("Ei saanud käsust aru!")


