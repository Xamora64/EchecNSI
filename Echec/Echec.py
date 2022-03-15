# Créé par etienne.rey, le 10/02/2022 en Python 3.7

import sys, pygame
from Case import *
from Pion import *

class Echec:

    def __init__(self):

        self.__ecran = pygame.display.set_mode((550,550))
        pygame.display.set_caption("Echec")

        self.__imageEchiquier = pygame.image.load("Echiquier.jpg")

        self.__tour = "Blanc"

        #Création échiquier, case et pion
        self.__echiquier = []
        compteur = 0
        idCase = 0
        for i in range(0,8):
            for j in range(0,8):
                if (i > -1 and i < 2) or (i > 5 and i < 8):
                #if(j == 1 and i == 1):
                    self.__echiquier.append(Case(i,j,38 + (j*59),36 +(i*59), self.__ecran, Pion(self.__ecran,compteur, 38 + (j*59) + 12, 36 +(i*59) + 5), True))
                    compteur += 1
                else:
                    self.__echiquier.append(Case(i,j,38 + (j*59),36 +(i*59), self.__ecran, None, False))
        #for i in range(0,64):
            #print(self.__echiquier[i])

    def run(self):
        running = True
        pionEnMainPion = None
        ancienneCase = None

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Quand il clique sur stop
                    running = False

                elif event.type == pygame.MOUSEBUTTONUP: #Quand le joueur clique
                  pos = pygame.mouse.get_pos()
                  for case in self.__echiquier:
                    if(pionEnMainPion == None and (not case.getPion() == None) and (pos[0] > case.getX() and pos[0] < case.getLargeur() + case.getX()) and (pos[1] > case.getY() and pos[1] < case.getHauteur() + case.getY())): #attrape le pion
                        if(case.getPion().getPionCouleur() == self.__tour):    # Savoir si c'est son tour
                            case.getPion().setSuiviSouris(True)                # Modifier la varible pour que le pion suis la souris
                            pionEnMainPion = case.getPion()                    # Récupéré le pion en main
                            ancienneCase = case                                # Récupéré la case d'où il vient

                    elif(pionEnMainPion != None and (pos[0] > case.getX() and pos[0] < case.getLargeur() + case.getX()) and (pos[1] > case.getY() and pos[1] < case.getHauteur() + case.getY())): #lache le pion
                        for posibiliteListCase in pionEnMainPion.restrictions(ancienneCase, case, self):
                            if(posibiliteListCase == (case.getI(), case.getJ())):
                                print("test")
                                if(case.getPion() != None and case.getPion().getPionCouleur() != pionEnMainPion.getPionCouleur()):
                                    case.setPion(None)
                                    pionEnMainPion = self.putPion(pionEnMainPion, ancienneCase, case)

                                    break
                                elif (case.getPion() == None or case == ancienneCase):
                                    pionEnMainPion = self.putPion(pionEnMainPion, ancienneCase, case)

                                    break

            self.__ecran.blit(self.__imageEchiquier, (0,0))   # Dessine l'échiquier
            for case in self.__echiquier:                  	  # Dessine les pions
                if(not case.getPion() == None):
               	    if(not case.getPion().getSuiviSouris()):
                        if(pionEnMainPion != None):
                            pionEnMainPion.drawPion()
                        case.getPion().drawPion()
                #case.drawCase()
            pygame.display.update()
        pygame.quit()

    def putPion(self, pionEnMainPion, ancienneCase, case):
        ancienneCase.setPion(None)             # Supprime le pion de la case d'où il vient
        pionEnMainPion.setSuiviSouris(False)   # Le pion arrête de suivre le pion
        case.setPion(pionEnMainPion)           # Met le pion sur la case
        pionEnMainPion = None                  # Je supprime le pion dans la main

        case.getPion().setPosition(case.getX()+ 12, case.getY()+ 5) # Je modifie la position du pion sur la case

        #Changement de tour
        if(case != ancienneCase):
            if(self.__tour == "Blanc"):
                self.__tour = "Noir"
            else:
                self.__tour = "Blanc"

        return pionEnMainPion

    def getCasePosition(self, i , j):
        for case in self.__echiquier:
            if case.getI() == i and case.getJ() == j:
                return case

pygame.init()
echec = Echec()
echec.run()

