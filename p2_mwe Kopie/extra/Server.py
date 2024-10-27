from fastapi import FastAPI

# Versuch, das schiffeversenken-Modul zu importieren. Falls dies fehlschlägt, wird eine Fehlermeldung ausgegeben und das Programm beendet.
try:
    import schiffeversenken
except ImportError as e:
    print(f"Importieren der Shared Library 'schiffeversenken' hat nicht funktioniert.")
    print(f"Ist die Shared Library 'schiffeversenken.____.so' (oder ein Link darauf) im gleichen Verzeichnis wie dieses Python-Skript?")
    print(f"Der Import verursachte folgenden Fehler: '{e}'")
    print(f"Programm wird beendet")
    exit(1)

# Importieren spezifischer Klassen und Funktionen aus dem schiffeversenken-Modul
from schiffeversenken import Lobby, Schiffe
import os
from fastapi import FastAPI
import uvicorn
from typing import List, Tuple

# Erstellen einer Instanz der Lobby-Klasse
lob = Lobby()

# Initialisieren der FastAPI-Instanz
rest_api = FastAPI()


# Definieren der verschiedenen Endpunkte der API

# Wurzelpfad - gibt eine einfache Nachricht zurück, um die Funktionalität der API zu testen
@rest_api.get("/")
async def wurzel_pfad():
    return {"coole_nachricht": "Fast API funktioniert"}

# Endpunkt zur Rückgabe einer Benutzer-ID, basierend auf der angegebenen Benutzer-ID
@rest_api.get("/user/{uid}")
async def get_user_by_id(uid: int):
    return {"user_id": uid}

# Endpunkt zum Erstellen eines Spielers in der Lobby und Rückgabe der zugehörigen Benutzer-ID
@rest_api.get("/lobby/{name}")
async def create_player(name: str):
    return {"user_id": lob.spieler_erstellen(name).get_id()}

# Endpunkt zur Rückgabe der Anzahl der Spieler in der Warteschlange
@rest_api.get("/lobby")
async def get_queue():
    return {"q_size": lob.queue_size()}

# Endpunkt zur Rückgabe der Anzahl der laufenden Spiele
@rest_api.get("/spiele")
async def spiele_size():
    return {"s_size": lob.spiele_size()}

# Endpunkt zur Rückgabe der aktuellen Spiel-ID für einen bestimmten Spieler
@rest_api.get("/{id}")
async def get_in_game(id: int):
    return {"current_game": lob.player_by_id(id).get_in_game()}

# Endpunkt zur Rückgabe der Gegner-ID für einen bestimmten Spieler
@rest_api.get("/get_gid/{id}")
async def get_gid(id: int):
    return {"gid": lob.player_by_id(id).get_gid()}

# Endpunkt zur Rückgabe der ID des Spielers, der momentan am Zug ist, für ein bestimmtes Spiel
@rest_api.get("/{game}/turn")
async def get_turn(game: int):
    return {"current_turn": lob.game_by_id(game).get_turn()}

# Endpunkt zur Abhandlung eines Schusses im Spiel. Gibt zurück, ob der Schuss ein Treffer war oder nicht.
@rest_api.get("/shoot/{sid}/{x}/{y}")
async def shoot(sid: int, x: int, y: int):
    if lob.hit(sid, x, y):
        return {"Hit": "Hit"}
    else:
        return {"Hit": "Miss"}

# Endpunkt zum Empfangen und Speichern von Schiffskoordinaten für ein bestimmtes Spiel
@rest_api.get("/postkoordinaten/{game}/{sid}/{x}/{y}")
async def post_koordinaten(game: int, sid: int, x: int, y: int):
    lob.add_t(x, y, game, sid)
    return {"Status": "Koordinaten empfangen"}

# Endpunkt zum Hinzufügen von Koordinaten zu einem bestimmten Spieler-Array
@rest_api.get("/add_to_array/{sid}/{x}/{y}")
async def add_to_array(sid: int, x: int, y: int):
    lob.add_array(x, y, sid)
    return {"status": "Koordinaten empfangen"}

# Endpunkt zur Rückgabe der Größe des Koordinaten-Arrays für einen bestimmten Spieler
@rest_api.get("/array_by_id/{sid}")
async def array_by_id(sid: int):
    return {"size": lob.array_by_id(sid)}

# Endpunkt zum Wechseln des Spielzugs im Spiel
@rest_api.get("/set_turn/{game}")
async def set_turn(game: int):
    a = lob.game_by_id(game)
    a.set_turn()
    lob.edit_game(game, a)
    return {"status": "Zug gewechselt"}

# Endpunkt zum Markieren eines Spiels als beendet
@rest_api.get("/set_over/{game}")
async def set_over(game: int):
    a = lob.game_by_id(game)
    a.set_over()
    lob.edit_game(game, a)
    return {"status": "Spiel beendet"}

# Endpunkt zur Überprüfung, ob ein Spiel beendet ist
@rest_api.get("/get_over/{game}")
async def get_over(game: int):
    a = lob.game_by_id(game)
    if a.get_over():
        return {"over": "True"}
    else:
        return {"over": "False"}

# Endpunkt zum Entfernen eines Spiels aus der Lobby
@rest_api.get("/erase_game/{game}")
async def erase_game(game: int):
    lob.erase_game(game)
    return {"status": "Spiel wurde entfernt"}
