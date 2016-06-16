import pygame

class MainMenu:

	pygame.init()

	fenetre = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Le Saint Laurent - Menu principal")

	fond = pygame.image.load("TEX/MTL.png").convert()
	positionX = -200
	positionY = 0
	positionVX = 1

	menuoption = pygame.image.load("TEX/menu.png").convert()

	musique =  pygame.mixer.music.load("SON/Theme.wav")
	pygame.mixer.music.play()

	continuer = 1
	while continuer:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				continuer = 0
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					import quit
					Quit()
				if event.key == pygame.K_UP:
					import Map
		positionX += positionVX
		fenetre.blit(fond, (positionX,positionY))
		fenetre.blit(menuoption, (170,0))
		pygame.display.flip()
		if positionX <= -200:
			positionVX = 1
			fenetre.blit(fond, (positionX,positionY))
			fenetre.blit(menuoption, (200,200))
			pygame.display.flip()
		elif positionX >= 0:
			positionVX = -1
			fenetre.blit(fond, (positionX,positionY))
			fenetre.blit(menuoption, (200,200))
			pygame.display.flip()
