from bagna import bagna

miecz = 1
poziom = 1
walka = poziom + miecz
def bagna():
    global poziom, miecz, walka 
    print("wchodzisz na bagna")
    print("atakuje cię utopiec\n"
          "a.atakujesz go\n"
          "b.uciekasz")
    x = input()
    if x == "a":
        sila_utopca = 5
        if sila_utopca < walka:
            print("pokonałeś utopca")
            poziom += 1
        else:
            print("Umierasz.Przegrywasz.tamtamtamtam.posempna muzyka")
            exit()
    if x == "b":
        print("spanikowany wracasz do wioski")

def las():
    global poziom, miecz, walka
    print("Spotykasz goblina.\n"
          "a.atakujesz go\n"
          "b.uciekasz")
    x = input()
    if x == "a":
        if walka > 1:
            print("pokonujesz go")
            poziom += 1
            print("widzisz ścieszke\n"
                  "a.idziesz scieszka\n"
                  "b.zaglembiasz się w las")
            x = input()
            if x == "a":
                print("Dochodzisz do kaplicy. Modli się przy niej pielgrzym\n"
                      "a.zagadujesz do niego\n"
                      "b.modlisz sie\n")
                x = input()
                if x == "a":
                    print("Nic nie odpowiada, ale w głębi duszy słyszysz głós. - zabić, nakarmić, pilnować, światło-. Wtedy pielgrzym rospływa się, a ty odczuwasz dziwny ciężar w kieszeni. Wkładasz tam dłoń, i wyciągasz piękny błyszczący\n"
                          "klejnot władcy")
                    klejnot_władcy_1 = True
                    pielgrzym_1 = True
                    walka += 10
                    print("co robisz\n"
                          "a.zawracasz\n"
                          "b.idziesz w las")
                    x = input()
                    if x == "a":
                        print("Wracasz do wioski. Uznajesz, że twoją jedyną szansą jest pójście na bagna")
                        bagna()
                    if x == "b":
                        print("Idziesz i idziesz. Las staje się coraz gęstrzy i gęstrzy a mgla utrudnia orietacje\n"
                              "a.zawracasz\n"
                              "b.idziesz dalej")
                        x = input()
                        if x == "a":
                            print("Wracasz do wioski. Uznajesz, że twoją jedyną szansą jest pójście na bagna")
                            bagna()
                        if x == "b":
                            print("Po chwili twoją duszę ogarnia mrok, a ty, czujesz się coraz bardziej słaby i zmęczony. Po kilku przebytych metra czujesz na karku ciepło krwi, a potem pustke.")
                            print("umierasz")
                            exit()
                if x == "b":
                        print("odczuwasz dziwny ciężar w kieszeni. Wkładasz tam dłoń, i wyciągasz piękny błyszczący\n"
                              "klejnot władcy")
                        klejnot_władcy_1 = True
                        pielgrzym_1 = False
                        walka += 10
                        print("co robisz\n"
                          "a.zawracasz\n"
                          "b.idziesz w las")
                        x = input()
                        if x == "a":
                            print("Wracasz do wioski. Uznajesz, że twoją jedyną szansą jest pójście na bagna")
                            bagna()
                            if x == "b":
                                print( "Po chwili twoją duszę ogarnia mrok, a ty, czujesz się coraz bardziej słaby i zmęczony. Po kilku przebytych metra czujesz na karku ciepło krwi, a potem pustke.")
                                print("umierasz")
                                exit()
            if x == "b":
                print("Idziesz i idziesz. Las staje się coraz gęstrzy i gęstrzy a mgla utrudnia orietacje\n"
                      "a.zawracasz\n"
                      "b.idziesz dalej")
                x = input()
                if x == "a":
                    print("Dochodzisz do kaplicy. Modli się przy niej pielgrzym\n"
                      "a.zagadujesz do niego\n"
                      "b.modlisz sie\n")
                    x = input()
                    if x == "a":
                        print("Nic nie odpowiada, ale w głębi duszy słyszysz głós. - zabić, nakarmić, pilnować, światło-. Wtedy pielgrzym rospływa się, a ty odczuwasz dziwny ciężar w kieszeni. Wkładasz tam dłoń, i wyciągasz piękny błyszczący")
                        print("klejnot władcy")
                        klejnot_władcy_1 = True
                        pielgrzym_1 = True
                        print("")
                    if x == "b":
                        print("odczuwasz dziwny ciężar w kieszeni. Wkładasz tam dłoń, i wyciągasz piękny błyszczący\n"
                            "klejnot władcy")
                        klejnot_władcy_1 = True
                        pielgrzym_1 = False
    if x == "b":
        print("Uciekasz mu.")
        print("spanikowany wracasz do wioski\n"
              "a.idziesz do lasu\n"
              "b.idziesz na bagna")
        x = input()
        if x == "a":
            las()
        if x == "b":
            bagna()

        


