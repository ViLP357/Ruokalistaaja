import sqlite3
import urllib.request
import json
import datetime

sqliteConnection = sqlite3.connect('ruokapaikat.db')
sqliteConnection.isolation_level = None
cursor = sqliteConnection.cursor() 

def haeTiedotWeek(paikka, week):
    data=sqliteConnection.execute("SELECT * FROM Ruokapaikat WHERE nimi = ?", [paikka]).fetchall()


    #for row in data:
    #if week == 0:
    linkki = data[0][week + 2]
    
    cursor.close()
    #print(linkki)
    pyynto = urllib.request.urlopen(linkki)

    data = pyynto.read()
        
    return json.loads(data)

def tulostaRuokaToday(tieto):
    dayNumero = datetime.datetime.today().weekday()
    if dayNumero > 4:
        print("Nyt on viikonloppu! Katso sen sijaan ensi viikon ruoat(-nw)")
        return
    paiva = tieto["result"]["pageContext"]["menu"]["Days"][dayNumero]
    print(f"Päivän ruoka: {paiva["Date"]}")
    for ateria in paiva["Meals"]:
        print(ateria["Name"])

def tulostaRuokaWeek(tieto):
    paivat = tieto["result"]["pageContext"]["menu"]["Days"]
    for paiva in paivat:
        print()
        print(f"Päivän ruoat: {paiva["Date"]}")
        ateriat = paiva["Meals"]
        for ateria in ateriat:
            print(ateria["Name"])
        


def Ruoka(paikka, laajuus):
    if len(laajuus) == 2:
        week = 0
    if len(laajuus) == 3:
        week = 1
    
    tieto = haeTiedotWeek(paikka, week) #hakee viikon json tiedostosta kaikille päiville ruoat
    if laajuus == "-t":
        tulostaRuokaToday(tieto)
    if laajuus == "-w" or laajuus == "-nw": #Jos halutaan kaikki tämän tai seuraavan viikon ruoat
        tulostaRuokaWeek(tieto)

    #print(f"tieto: {tieto}")

        
        



