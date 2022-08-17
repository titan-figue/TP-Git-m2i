import random

def randomMonster(name):
    
    pv = random.randint(5, 20)
    Force = random.randint(3, 8)
    Armure = random.randint(0, 5)
    monstre = [name, pv,Force,Armure]
    return monstre


print(randomMonster("Kraken"))