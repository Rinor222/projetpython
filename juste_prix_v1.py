from ast import In
from random import randint


prix=randint(1, 100)

proposition_prix= int

while proposition_prix != prix:
      proposition_prix= input("bienvenu à vous, proposer un prix: ")
      if proposition_prix < prix:
          
          proposition_prix=input("c'est plus veuillez réecrire un prix ")
    
      elif proposition_prix>prix:
          proposition_prix=input("c'est moins","\n","veuillez réecrire un prix ")

      elif proposition_prix==prix:
          print("félicitation vous avez trouver le juste prix ",prix)
          exit()

       