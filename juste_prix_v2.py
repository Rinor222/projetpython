
from random import randint


prix=randint(1, 100)
tentative=10
proposition_prix= int(input("bienvenue à vous, proposer un prix entre 1 et 100: "))

while proposition_prix != prix:
    tentative-=1

    if proposition_prix < prix:
          
          proposition_prix=int(input("c'est plus veuillez réecrire un prix: "))
    
    elif proposition_prix>prix:
          proposition_prix=int(input("c'est moins, veuillez réecrire un prix: "))
print(f"félicitation vous avez trouver le juste prix qui est de {prix}")