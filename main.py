from pygame import *
from dodatki import *
from lib_1_main import *


muzyka()
print("Trzy klejnoty dla elfów. Trzy klejnoty dla orków. Trzy klejnoty dla ludzi. Ale tylko jeden, dla czarnego pana.")
print("")
print("jestes wojownikiem. Musisz odnalezc zaginione klejnoty królestwa elfów.")
print("")
miecz = 1
poziom= 1
walka = poziom + miecz
print("Idziesz lasem. Widzisz rozwidlenie.\n"
      "a.idziesz w prawo\n"
      "b.idziesz w lewo")

x = input()
if x == "a" :
    print("Spotykasz elfa. Mówi:\n- Król zielonego lasu chce abys do niego poszedl.\n"
          "a.idziesz za elfem\n"
          "b.atakujesz elfa")
    x = input()
    if x == "a" :
        print("Idziecie lasem. Atakuje was goblin. Goblin pokonuje elfa. Uciekasz i wracasz na trakt.")
    if x == "b" :
        if 10 < walka :
            print("Pokonales elfa")
            poziom + 1
        else:
            print("Elf cie pokonuje. Przegrywasz")
            exit()
if x == "b" :
    print("Atakuje cie goblin\n"
          "a.atakujesz goblina\n"
          "b.uciekasz")
    
    x = input()
    if x == "a" :
        if 1 < walka:
            print("Pokonales goblina")
            poziom += 1
        else:
             print("Goblin cie pokonuje. Przegrywasz")
             exit()
    if x == "b" :
        print("idziesz dalej")
print("Dochodisz do wioski. Gdy wchodzisz nie wita cię nic prucz zasłoniętyh zasłony i podejrzliwych spojrzeni. Poszedłeś do gospody. Jesteś zmęczony i musisz coś zjeść")
print("")
print("Gdy podhodzisz, zaczepia cię jakiś mężczyzna. - Czego szukasz w naszej wiosce.- Zostaw przybysza Ed.-Głos wydobył się z cienia, ale teraz gdy ten człowiek się poruszył, i tak było widać tylko jego zarys.\n"
      "Wyglądasz jagbyś szukał informacji.- Bo szukam. Chciałbym wiedzieć dlaczego wioska wygląda na opusztoszałą.\n"
      "- Wioska jest ostrożna wobec przyjezdnych bo gobliny stają się coraz śmielsze. Napadają na naszą wioską i rządają wysokiego harczu za oszczędzenie wioski. Muwisz- Sprubuje wam pomuc. Jestem wojownikiem.Porozmawiam z wujtem.")
print("Dobrze ale nie licz na wielką hojność. Nasza wioska bardzo zbiedniała od ataków goblinów.")
print("Idziesz do wójta. Ratusz przypominał bardiej zameczek. Dohodzisz do wniosku ,że musiała to kiedyś być bogata wioska. Kidyś bo teraz mały i rozpadający się zameczke wyglądał jak ruiny. Nie jak siediba urzędników i wujta.Wchodisz do ruin. Zahodzą ci drogę strażnicy.- Jeśli chcesz wejś musiż udowodnić że jesteś godny. Przynieś nam pięć głów goblinów.\n"
      "a.idziesz do  lasu\n"
      "b.idziesz na bagna")
x = input()
if x == "a":
    las()
if x == "b":
    bagna()










    
