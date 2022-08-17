#!/usr/bin/python3
import random

def randomMonster(name):

    pv = random.randint(5, 20)
    Force = random.randint(3, 8)
    Armure = random.randint(0, 5)
    monstre = [name, pv,Force,Armure]
    return monstre

def function_generation_du_monstre() :
    name  = input('Entrez le nom du monstre : ')
    print ( name)
    result = randomMonster(name)

    return  result

# Creation d'un personnage

# titre
# print ("Crée ton personnage !")
def personnage (Pseudo, PV, Force, Armure):
    result = [Pseudo, PV, Force, Armure]
    return result

def function_gestion_degats():
    personnagedefault =personnage ("alpha", 50,100,200)
    monsterDefault = randomMonster(function_generation_du_monstre())
    resultPv = monsterDefault[1]-(personnagedefault[2]-monsterDefault[3])
    return resultPv

