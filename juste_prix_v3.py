from random import randint
print("!!bienvenue au juste prix!!")
proposition_mode=int(input("veuillez choisir un niveau de difficulté,tapez 1 pour facile,2 pour le normal ou 3 pour le personnalisé:"))




prix=randint(1, 100)
tentative= 10
nombre_de_tentative=0
# pour le mode 1
if proposition_mode == 1:
      proposition_prix= int(input("veuillez proposer un prix entre 1 et 100 :"))
      while True:
        
          if proposition_prix < prix:
              
             proposition_prix=int(input("c'est plus veuillez réecrire un prix: "))
    
          elif proposition_prix>prix:
             proposition_prix=int(input("c'est moins, veuillez réecrire un prix: "))

          elif proposition_prix==prix:
             print(f"félicitation vous avez trouver le prix qui était de {prix} ")
             exit()
# pour le mode 2
if proposition_mode==2:
      proposition_prix=int(input("veuillez proposer un prix entre 1 et 100. ATTENTION vous n'avez que 10 tentatives:"))

      while True:
                           
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
    
              
              elif proposition_prix==prix:
                 print(f"Félicitation vous avez trouver le juste prix qui était {prix} en {nombre_de_tentative} tentatives!")
                 exit()
              elif tentative == 1:
                  print(f"Malheureusement vous avez perdu, la bonne réponse était {prix}. ")
                  exit()
#   pour le mode 3
if proposition_mode==3:
      max=int(input("veuillez choisir votre prix maximum:"))
      prix2=randint(1,max)
      choix_tentative=int(input("veuillez choisir votre nombre de tentative maximum(si vous choisisez le 0 vous vos tentatives seront illimité):"))
      tentative2=choix_tentative
      nombre_tentative2=0
      tentative3=tentative2-1
# pour le chiffre illimiter
      if tentative2==0:
            proposition_prix= int(input(f"veuillez proposer un prix entre 1 et {max} :"))
            while True:
                 

                  if proposition_prix < prix2:
                         proposition_prix=int(input("C'est plus veuillez réecrire un prix: "))

                  elif proposition_prix > prix2:
                     proposition_prix=int(input("C'est moins, veuillez réecrire un prix: "))

                  elif proposition_prix==prix2:
                     print(f"Félicitation vous avez trouver le juste prix qui était {prix2}!")
                     exit()


      if choix_tentative!=0:
         proposition_prix= int(input(f"veuillez proposer un prix entre 1 et {max}. ATTENTION vous n'avez que {tentative2} tentative :"))
         while True:
            if nombre_tentative2 == tentative3:
                 print(f"Malheureusement vous avez perdu, la bonne réponse était {prix2}. ")
                 exit()  
            tentative2-=1
            nombre_tentative2+=1
              
  
            if proposition_prix < prix2:
                 print(f"Il vous reste {tentative2} tentatives.")
                 proposition_prix=int(input("C'est plus veuillez réecrire un prix: "))
    
            elif proposition_prix>prix2:
                 print(f"Il vous reste {tentative2} tentatives.")
                 proposition_prix=int(input("C'est moins, veuillez réecrire un prix: "))
    
            elif tentative2 == 1:
                 print(f"Malheureusement vous avez perdu, la bonne réponse était {prix2}. ")
                 exit()
            elif proposition_prix==prix2:
                 print(f"Félicitation vous avez trouver le juste prix qui était {prix2} en {nombre_tentative2} tentatives!")
                 exit()