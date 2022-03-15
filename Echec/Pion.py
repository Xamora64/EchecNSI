
import sys, pygame
from Case import *

class Pion:
    def __init__(self, ecran, id, x, y):
        self.__x = x
        self.__y = y
        self.__id = id
        self.__ecran = ecran
        self.__suiviSouris = False

        if(self.__id > 0 and self.__id < 16):
            self.__couleur = "Noir"
        else:
            self.__couleur = "Blanc"

        self.__imagePionNoir = pygame.image.load("PionNoir/PionNoir.png")
        self.__imageTourNoir = pygame.image.load("PionNoir/TourNoir.png")
        self.__imageChevalNoir = pygame.image.load("PionNoir/ChevalNoir.png")
        self.__imageFouNoir = pygame.image.load("PionNoir/FouNoir.png")
        self.__imageReineNoir = pygame.image.load("PionNoir/ReineNoir.png")
        self.__imageRoiNoir = pygame.image.load("PionNoir/RoiNoir.png")

        self.__imagePionBlanc = pygame.image.load("PionBlanc/PionBlanc.png")
        self.__imageTourBlanc = pygame.image.load("PionBlanc/TourBlanc.png")
        self.__imageChevalBlanc = pygame.image.load("PionBlanc/ChevalBlanc.png")
        self.__imageFouBlanc = pygame.image.load("PionBlanc/FouBlanc.png")
        self.__imageReineBlanc = pygame.image.load("PionBlanc/ReineBlanc.png")
        self.__imageRoiBlanc = pygame.image.load("PionBlanc/RoiBlanc.png")

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def setPosition(self, x, y):
        self.__x = x
        self.__y = y

    def drawPion(self):
        if(not self.__suiviSouris):
            self.drawPionSecond(self.__x,self.__y)
        else:
            pos = pygame.mouse.get_pos()
            self.drawPionSecond(pos[0]-20, pos[1]-20)

    def drawPionSecond(self, x, y):
        if(self.__id == 0 or self.__id == 7):
            self.__ecran.blit(self.__imageTourNoir, (x, y))
        elif(self.__id == 1 or self.__id == 6):
            self.__ecran.blit(self.__imageChevalNoir, (x, y))
        elif(self.__id == 2 or self.__id == 5):
            self.__ecran.blit(self.__imageFouNoir, ( x, y))
        elif(self.__id == 3):
            self.__ecran.blit(self.__imageReineNoir, ( x, y))
        elif(self.__id == 4):
            self.__ecran.blit(self.__imageRoiNoir, (x, y))
        elif(self.__id > 7 and self.__id < 16):
            self.__ecran.blit(self.__imagePionNoir, ( x, y))

        elif(self.__id == 24 or self.__id == 31):
            self.__ecran.blit(self.__imageTourBlanc, (x, y))
        elif(self.__id == 25 or self.__id == 30):
            self.__ecran.blit(self.__imageChevalBlanc, (x, y))
        elif(self.__id == 26 or self.__id == 29):
            self.__ecran.blit(self.__imageFouBlanc, ( x, y))
        elif(self.__id == 27):
            self.__ecran.blit(self.__imageReineBlanc, ( x, y))
        elif(self.__id == 28):
            self.__ecran.blit(self.__imageRoiBlanc, (x, y))
        elif(self.__id > 15 and self.__id < 24):
            self.__ecran.blit(self.__imagePionBlanc, ( x, y))

    def setSuiviSouris(self, suiviSouris):
        self.__suiviSouris = suiviSouris

    def getSuiviSouris(self):
        return self.__suiviSouris

    def getPionCouleur(self):
        return self.__couleur

    def restrictions(self, case, newCase, echec):
        L = [(case.getI(), case.getJ())]
        if self.__id > 7 and self.__id < 16: #Pion Noir
            if case.getI() < 8 and newCase.getPion() == None:
                L.append((case.getI() + 1, case.getJ()))
                if case.getI() == 1:
                    L.append((case.getI() + 2, case.getJ()))
            if newCase.getPion() != None and (newCase.getI() == case.getI() + 1 and newCase.getJ() == case.getJ() - 1):
                L.append((case.getI() + 1, case.getJ() - 1))
            if newCase.getPion() != None and (newCase.getI() == case.getI() + 1 and newCase.getJ() == case.getJ() + 1):
                L.append((case.getI() + 1, case.getJ() + 1))

        elif self.__id > 15 and self.__id < 24: #Pion Blanc
            if case.getI() > 0 and newCase.getPion() == None:
                L.append((case.getI() - 1, case.getJ()))
                if case.getI() == 6:
                    L.append((case.getI() - 2, case.getJ()))
            if newCase.getPion() != None and (newCase.getI() == case.getI() - 1 and newCase.getJ() == case.getJ() - 1):
                L.append((case.getI() - 1, case.getJ() - 1))
            if newCase.getPion() != None and (newCase.getI() == case.getI() - 1 and newCase.getJ() == case.getJ() + 1):
                L.append((case.getI() - 1, case.getJ() + 1))
        elif self.__id == 1 or self.__id == 6 or self.__id == 25 or self.__id == 30: #Cheval
            L.append((case.getI() + 2, case.getJ() + 1))
            L.append((case.getI() + 1, case.getJ() + 2))
            L.append((case.getI() + 1, case.getJ() - 2))
            L.append((case.getI() - 1, case.getJ() + 2))
            L.append((case.getI() - 1, case.getJ() - 2))
            L.append((case.getI() - 2, case.getJ() + 1))
            L.append((case.getI() - 2, case.getJ() - 1))
        elif self.__id == 0 or self.__id == 7 or self.__id == 24 or self.__id == 31:

            for i in range(1, 8):
                if(echec.getCasePosition(case.getI() + i,  case.getJ()) != None):
                    L.append((case.getI() + i, case.getJ()))
                    if(echec.getCasePosition(case.getI() + i,  case.getJ()).getPion() != None):
                        break

            for i in range(1, 8):
                if(echec.getCasePosition(case.getI() - i,  case.getJ()) != None):
                    L.append((case.getI() - i, case.getJ()))
                    if(echec.getCasePosition(case.getI() - i,  case.getJ()).getPion() != None):
                        break

            for j in range(1, 8):
                if(echec.getCasePosition(case.getI(),  case.getJ() + j) != None):
                    L.append((case.getI(), case.getJ() + j))
                    if(echec.getCasePosition(case.getI(),  case.getJ() + j).getPion() != None):
                        break

            for j in range(1, 8):
                if(echec.getCasePosition(case.getI(),  case.getJ() - j) != None):
                    L.append((case.getI(), case.getJ() - j))
                    if(echec.getCasePosition(case.getI(),  case.getJ() - j).getPion() != None):
                        break
            print(L)
        return(L)