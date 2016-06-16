import pygame

class Quit:

	pygame.init()

	fenetre = pygame.display.set_mode((640, 480))
	pygame.display.set_caption("Le Saint Laurent")

	Salutations = pygame.image.load("TEX/QUIT.png").convert()
	positionX = 0
	positionY = 0

	continuer = 1
	while continuer:
		fenetre.blit(Salutations, (positionX,positionY))			
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				continuer = 0
		pygame.time.delay(4500)
		continuer = 0
	    

	
