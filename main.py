import pygame

class Main:

	pygame.init()

	fenetre = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Le Saint Laurent")

	fond = pygame.image.load("TEX/MatR.png").convert()
	positionX = 0
	positionY = 0

	MatRSound =  pygame.mixer.music.load("SON/MatR.wav")
	pygame.mixer.music.play()

	continuer = 1
	while continuer:
		fenetre.blit(fond, (positionX,positionY))			
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				continuer = 0
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					import MainMenu
					Main = MainMenu()
					Main.Afficher()
	    

	
