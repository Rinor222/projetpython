from ast import In
from random import randint


prix=randint(1, 100)

proposition_prix= int(input("bienvenu à vous, proposer un prix: "))

while proposition_prix != prix:
      if proposition_prix < prix:
          
          proposition_prix=int(input("c'est plus veuillez réecrire un prix: "))
    
      elif proposition_prix>prix:
          proposition_prix=int(input("c'est moins, veuillez réecrire un prix: "))
print("félicitation vous avez trouver le juste prix ",prix)