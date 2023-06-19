from staty import *

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