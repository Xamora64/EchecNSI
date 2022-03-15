import sys, pygame

from Pion import *

class Case:
    def __init__(self,x,y, ecran, pion, presencePion):
        self.__x = x
        self.__y = y
        self.__ecran = ecran
        self.__largeur = 59
        self.__hauteur = 57
        self.__pion = pion
        self.__presencePion = presencePion

    def drawCase(self):
        pygame.draw.rect(self.__ecran,(0,0,0),((self.__x,self.__y),(59,57)))

    def setPion(self, Pion):
        self.__pion = Pion

    def getPion(self):
        return self.__pion

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getLargeur(self):
        return self.__largeur

    def getHauteur(self):
        return self.__hauteur

    def getPresencePion(self):
        return self.__presencePion

    def setPresencePion(self, presencePion):
        self.__presencePion = presencePion