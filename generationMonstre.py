import random

def randomMonster(name):
    
    pv = random.randint(5, 20)
    Force = random.randint(3, 8)
    Armure = random.randint(0, 5)
    monstre = [pv,Force,Armure]
    print("Monstre:", name , "Valeurs:", monstre)


randomMonster("Kraken")