import sqlite3

import Ruokalistaaja.Yleishyödyllinen.foodlister as foodlister
import dates as dates
#while True:
#syote = "ruoka Saarni -nw"
syote = input()
syote = syote.split(" ")

if syote[0] == "ruoka":
    if syote[1] == "Saarni":
        foodlister.Ruoka("Saarnilaakso", syote[2])
elif syote == "date":
    dates.todaysdate()
elif syote == "quit":
    exit()

else:
    print("Virheellinen syote")
    #if syote[0] == "ruokapaikat":
    #    
    #    break
       

