import pygame

pygame.init()

#Ouverture de la fentre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("TEX/pc.jpg").convert()
fenetre.blit(fond, (0,0))

#Rafrachissement de l'cran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    continuer = int(input())