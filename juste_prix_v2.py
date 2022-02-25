
from random import randint


prix=randint(1, 100)
tentative= 10
nombre_de_tentative=0
proposition_prix= int(input(f"Bienvenue à vous, proposer un prix entre 1 et 100, ATTENTION vous n'avez que {tentative} tentatives:"))
while proposition_prix != prix:
    if nombre_de_tentative == 9:
          print(f"Malheureusement vous avez perdu, la bonne réponse était {prix}. ")
          exit()  
    tentative-=1
    nombre_de_tentative+=1
  
    if proposition_prix < prix:
          print(f"Il vous reste {tentative} tentatives.")
          proposition_prix=int(input("C'est plus veuillez réecrire un prix: "))
    
    elif proposition_prix>prix:
          print(f"Il vous reste {tentative} tentatives.")
          proposition_prix=int(input("C'est moins, veuillez réecrire un prix: "))
    
    elif tentative == 1:
          print(f"Malheureusement vous avez perdu, la bonne réponse était {prix}. ")
          exit()

print(f"Félicitation vous avez trouver le juste prix qui était {prix} en {nombre_de_tentative} tentatives!")
      