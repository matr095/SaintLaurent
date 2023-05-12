import pygame

pygame.init()

#Ouverture de la fentre Pygame
fenetre = pygame.display.set_mode((640, 480))

fenetre = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Le Saint Laurent - Niveau 1")

Toronto = pygame.image.load("TEX/Toronto.jpg").convert()
positionX = -200
positionY = 0
positionVX = 2


Protagoniste = pygame.image.load("TEX/Protagoniste.png").convert()
protaX = 640/4
protaY = 480/4
protaVY = 1
rotate = 0
rotateV = 0.01

Ennemi1 = pygame.image.load("TEX/Ennemi.png").convert()
Ennemi1X = 600
Ennemi1Y = 300
Ennemi1VX = 3

music1 =  pygame.mixer.music.load("SON/Sinclar.wav")
pygame.mixer.music.play()

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = 0
		if event.type == pygame.KEYDOWN:
			pressed = pygame.key.get_pressed()
			if event.key == pygame.K_LEFT:
				protaX -= 25
			elif event.key == pygame.K_RIGHT:
				protaX += 25
			elif event.key == pygame.K_UP:
				protaY -= 25
			elif event.key == pygame.K_DOWN:
				protaY += 25

	if protaY > 480:
		protaY = 0
	elif protaY < 0:
		protaY = 480

	elif (Ennemi1X <= protaX <= Ennemi1X+45) and (Ennemi1Y <= protaY <= Ennemi1Y+45):
		import MainMenu
                
	protaY += protaVY
	positionX -= positionVX
	Ennemi1X -= Ennemi1VX
	fenetre.blit(Toronto, (positionX,positionY))
	fenetre.blit(Protagoniste, (protaX,protaY))
	fenetre.blit(Ennemi1, (Ennemi1X, Ennemi1Y))
	pygame.display.flip()
	pygame.time.Clock().tick(60)
