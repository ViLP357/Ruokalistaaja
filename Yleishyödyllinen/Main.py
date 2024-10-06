import sqlite3
import functions



#while True:
syote = "ruoka Saarni -nw"
    #syote = input()
syote = syote.split(" ")

if syote[0] == "ruoka":
    if syote[1] == "Saarni":
        functions.Ruoka("Saarnilaakso", syote[2])
    #if syote[0] == "ruokapaikat":
    #    
    #    break
       

