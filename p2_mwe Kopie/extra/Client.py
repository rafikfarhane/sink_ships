# Run with:
# uvicorn Server:rest_api --port 8000 --reload
# cmake -S . -B build && cmake --build build && cmake --install build

import requests
from schiffeversenken import Schiffe, Spielbrett

# Eingabe des Spielernamens durch den Benutzer
name = input("Gib deinen Namen ein: ")

# Senden einer GET-Anfrage an den Server, um sich mit dem eingegebenen Namen in die Lobby einzutragen
r = requests.get("http://127.0.0.1:8000/lobby/%s" % name)

# Konvertieren der Antwort in JSON-Format
r_json = r.json()

# Speichern der erhaltenen Benutzer-ID
my_id = r_json['user_id']
print(my_id)

print("Suche nach Spiel...")

# Warten, bis ein Spiel gefunden wird
waiting = True
while waiting:
    resp = requests.get("http://127.0.0.1:8000/lobby")
    resp_json = resp.json()
    a = resp_json['q_size']

    if a == 0:
        waiting = False

print("Spiel startet")

# Testen des Spiel-Arrays
re = requests.get("http://127.0.0.1:8000/spiele")
re_json = re.json()
spielesize = re_json['s_size']
print(spielesize)

# Erhalten der Spiel-ID für den Client
r = requests.get("http://127.0.0.1:8000/%s" % my_id)
r_json = r.json()
my_game_id = r_json['current_game']

# Erhalten der Gegner-ID
print(my_game_id)
r = requests.get("http://127.0.0.1:8000/get_gid/%s" % my_id)
r_json = r.json()
gid = r_json["gid"]

# Initialisieren des Spielfeldes und der Schiffe
sb = Spielbrett()
s = Schiffe()
Schiffgrößen = [2, 3, 4]

# Funktion zum Eingeben der Koordinaten für die Platzierung der Schiffe
def eingaben_loop(schiffgröße: int) -> list:
    print("Gebe die x-Koordinate an für die Schiffgröße: ", schiffgröße)
    x_koordinate = input()
    while True:
        try:
            while int(x_koordinate) < 0 or int(x_koordinate) > 9:
                print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
                x_koordinate = int(input())
            break
        except:
            x_koordinate = input("Es wurde kein Integer Wert übergeben. Gebe eine Zahl von 1 - 9 an! \n")

    print("Gebe die y-Koordinate an für die Schiffgröße: ", schiffgröße)
    y_koordinate = input()
    while True:
        try:
            while int(y_koordinate) < 0 or int(y_koordinate) > 9:
                print("Das eingegebene Element ist keine Zahl von 1 - 9. Gebe eine Zahl an von 1 - 9")
                y_koordinate = int(input())
            break
        except:
            y_koordinate = input("Es wurde kein Integer Wert übergeben. Gebe eine Zahl von 1 - 9 an! \n")

    print("Gebe v (vertikal) oder h (horizontal) für die Richtung der Schiffgröße: ", schiffgröße, " an")
    richtung = input()
    while richtung != "v" and richtung != "h":
        print("Das eingegebene Element ist weder v (vertikal) noch h (horizontal). Gebe entweder v oder h ein")
        richtung = input()

    eingaben = [x_koordinate, y_koordinate, richtung]
    return eingaben

# Funktion zur Überprüfung der eingegebenen Koordinaten und zur Platzierung der Schiffe
def eingabe_überprüfen(schiffgröße: int, x_koordinate: int, y_koordinate: int, richtung: str) -> list:
    tupelarray = []

    if richtung == "h":
        for i in range(0, schiffgröße):
            tupel = (int(x_koordinate) + i, int(y_koordinate))
            tupelarray.append(tupel)
            for i in range(0, s.get_size()):
                for j in tupelarray:
                    if j == s.get_tupel(i):
                        tupelarray.clear()
                        print("Du kannst das Schiff leider nicht platzieren, da das Schiff sonst ein anderes Schiff überschneidet. Gebe neue Koordinaten an \n")
                        ergebnis_eingaben = eingaben_loop(schiffgröße)
                        x_koordinate1 = ergebnis_eingaben[0]
                        y_koordinate1 = ergebnis_eingaben[1]
                        richtung1 = ergebnis_eingaben[2]
                        return eingabe_überprüfen(schiffgröße, x_koordinate1, y_koordinate1, richtung1)

        if (int(x_koordinate) + int(schiffgröße)) > 10:
            print("Du kannst das Schiff leider nicht horizontal platzieren, da das Schiff sonst das Spielfeld überschreitet. Gebe neue Koordinaten an", "\n")
            ergebnis_eingaben = eingaben_loop(schiffgröße)
            x_koordinate2 = ergebnis_eingaben[0]
            y_koordinate2 = ergebnis_eingaben[1]
            richtung2 = ergebnis_eingaben[2]
            return eingabe_überprüfen(schiffgröße, x_koordinate2, y_koordinate2, richtung2)

    if richtung == "v":
        for i in range(0, schiffgröße):
            tupel = (int(x_koordinate) + i, int(y_koordinate))
            tupelarray.append(tupel)
            for i in range(0, s.get_size()):
                for j in tupelarray:
                    if j == s.get_tupel(i):
                        tupelarray.clear()
                        print("Du kannst das Schiff leider nicht platzieren, da das Schiff sonst ein anderes Schiff überschneidet. Gebe neue Koordinaten an", "\n")
                        ergebnis_eingaben = eingaben_loop(schiffgröße)
                        x_koordinate3 = ergebnis_eingaben[0]
                        y_koordinate3 = ergebnis_eingaben[1]
                        richtung3 = ergebnis_eingaben[2]
                        return eingabe_überprüfen(schiffgröße, x_koordinate3, y_koordinate3, richtung3)

        if (int(y_koordinate) + int(schiffgröße)) > 10:
            print("Du kannst das Schiff leider nicht vertikal platzieren, da das Schiff sonst das Spielfeld überschreitet. Gebe neue Koordinaten an")
            ergebnis_eingaben = eingaben_loop(schiffgröße)
            x_koordinate4 = ergebnis_eingaben[0]
            y_koordinate4 = ergebnis_eingaben[1]
            richtung4 = ergebnis_eingaben[2]
            return eingabe_überprüfen(schiffgröße, x_koordinate4, y_koordinate4, richtung4)

    meine_Liste = [int(x_koordinate), int(y_koordinate), richtung]
    return meine_Liste

# Anzeige des Spielbretts
sb.druckeSpielbrett()

# Platzierung der Schiffe durch den Spieler
while len(Schiffgrößen) != 0:
    print("Es stehen dir folgende Schiffgrößen zur Verfügung: ", Schiffgrößen, " 'reset' = Schiffe neu anordnen \n", "Gebe eine Schiffgröße ein")
    schiffgröße = input()

    while True:
        try:
            if schiffgröße == "reset":
                Schiffgrößen.clear()
                s.koordinaten_löschen()
                Schiffgrößen = [2, 3, 4]
                print("Du kannst deine Schiffe nun nochmal neu anordnen")
                break

            if int(schiffgröße) in Schiffgrößen:
                ergebnis_eingaben = eingaben_loop(int(schiffgröße))
                x_koordinate_er = ergebnis_eingaben[0]
                y_koordinate_er = ergebnis_eingaben[1]
                richtung_er = ergebnis_eingaben[2]

                ergebnis = eingabe_überprüfen(int(schiffgröße), x_koordinate_er, y_koordinate_er, richtung_er)
                x_koordinate = ergebnis[0]
                y_koordinate = ergebnis[1]
                richtung = ergebnis[2]

                Schiffgrößen.remove(int(schiffgröße))
                s.koordinaten_einfügen(int(schiffgröße), int(x_koordinate), int(y_koordinate), richtung)

                for i in s.get_koordinaten():
                    sb.setzeSchiff(i)
                sb.druckeSpielbrett()
            break

        except:
            print("Element ist nicht in den Schiffgrößen. Wähle eine der folgenden Schiffgrößen", Schiffgrößen, "\n")
            schiffgröße = input()

# Senden der platzierten Schiffe an den Server
for i in s.get_koordinaten():
    x_koordinate = i[0]
    y_koordinate = i[1]
    requests.get("http://127.0.0.1:8000/add_to_array/%s/%s/%s" % (my_id, x_koordinate, y_koordinate))
    rj = resp.json()

resp = requests.get("http://127.0.0.1:8000/array_by_id/%s" % my_id)
resp_j = resp.json()
print(resp_j['size'])

# Initialisieren des Spielfeldes für die Schüsse
sb_shoot = Spielbrett()
sb_shoot.druckeSpielbrett()

running = True
printed = False
gegner_print = False
winner = False
schon_geschossen = []

# Hauptspielschleife, um abwechselnd zu schießen
while running:
    over_r = requests.get("http://127.0.0.1:8000/get_over/%s" % my_game_id)
    over_json = over_r.json()
    over = over_json['over']
    if over == "True":
        break

    r = requests.get("http://127.0.0.1:8000/%s/turn" % my_game_id)
    r_json = r.json()
    turn = r_json['current_turn']

    if turn == my_id:
        gegner_print = False
        if not printed:
            print("Feuer frei!")
            printed = True

        # Eingabe und Validierung der x-Koordinate
        x = input("Wähle x-Koordinate: ")
        while True:
            try:
                int_x = int(x)
                while int_x < 0 or int_x > 9:
                    x = input("Die x-Koordinate muss zwischen 0 und 9 liegen. Bitte wähle erneut: ")
                    break
                break
            except:
                x = input("Eingabe muss ein Integer Wert sein")

        # Eingabe und Validierung der y-Koordinate
        y = input("Wähle y-Koordinate: ")
        while True:
            try:
                int_y = int(y)
                while int_y < 0 or int_y > 9:
                    y = input("Die y-Koordinate muss zwischen 0 und 9 liegen. Bitte wähle erneut: ")
                    break
                break

            except:
                y = input("Eingabe muss ein Integer Wert sein")

        # Überprüfung, ob die Koordinaten bereits verwendet wurden
        tupel = (int(x), int(y))
        while tupel in schon_geschossen:
            print("Du hast schon diese Koordinaten eingegeben. Gebe eine neue Koordinate ein")
            x = input("Wähle x-Koordinate: ")
            while True:
                try:
                    int_x = int(x)
                    while int_x < 0 or int_x > 9:
                        x = input("Die x-Koordinate muss zwischen 0 und 9 liegen. Bitte wähle erneut: ")
                        break
                    break
                except:
                    x = input("Eingabe muss ein Integer Wert sein")

            y = input("Wähle y-Koordinate: ")
            while True:
                try:
                    int_y = int(y)
                    while int_y < 0 or int_y > 9:
                        y = input("Die y-Koordinate muss zwischen 0 und 9 liegen. Bitte wähle erneut: ")
                        break
                    break

                except:
                    y = input("Eingabe muss ein Integer Wert sein")

            tupel = (int_x, int_y)

        hit_tupel = (int(x), int(y))
        schon_geschossen.append((int(x), int(y)))
        print(schon_geschossen)

        # Senden der Schusskoordinaten an den Server und Überprüfung des Treffers
        r = requests.get("http://127.0.0.1:8000/shoot/%s/%s/%s" % (gid, x, y))
        r_json = r.json()

        if r_json['Hit'] == "Hit":
            print("Volltreffer!")
            sb_shoot.set_hit(hit_tupel)
            sb_shoot.druckeSpielbrett()

            resp = requests.get("http://127.0.0.1:8000/array_by_id/%s" % gid)
            resp_j = resp.json()
            if resp_j['size'] == 0:
                requests.get("http://127.0.0.1:8000/set_over/%s" % my_game_id)
                winner = True
                running = False
            else:
                print("Der Gegner hat noch: ", resp_j['size'], " Koordinaten bei dem sich ein Schiff befindet")

        else:
            print("Leider daneben")
            requests.get("http://127.0.0.1:8000/set_turn/%s" % my_game_id)
            sb_shoot.set_miss(hit_tupel)
            sb_shoot.druckeSpielbrett()

    else:
        if not gegner_print:
            print("Der Gegner ist am Zug")
            gegner_print = True

# Überprüfen, ob der Spieler gewonnen hat
if winner:
    print("Sieg! Sie haben alle gegnerischen Schiffe versenkt und die Schlacht gewonnen!")
else:
    print("Niederlage... Sie mussten sich nach einer glorreichen Schlacht geschlagen geben.")
    requests.get("http://127.0.0.1:8000/erase_game/%s" % my_game_id)

