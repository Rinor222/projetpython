
from random import randint


prix=randint(1, 100)

tries=3

proposition_prix= int(input("bienvenu à vous, proposer un prix entre 1 et 100: "))
while tries > 0:
    
   while proposition_prix != prix:
      if proposition_prix < prix:
          
          proposition_prix=int(input("c'est plus veuillez réecrire un prix: "))
    
      elif proposition_prix>prix:
          proposition_prix=int(input("c'est moins, veuillez réecrire un prix: "))
print(f"félicitation vous avez trouver le juste prix qui est de {prix}")