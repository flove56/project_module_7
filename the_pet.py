import stages_pet
from body import Body
import pygame
import stages_pet


class The_pet:
    def __init__(self):
        self.size = (800, 800)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        self.body = Body(self.size)


    def game_loop(self):
        clock = pygame.time.Clock()

        while True:
            # Check for pygame events
            for event in pygame.event.get():
                # If the screen is closed quit program
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Call all functions
            self.display()

            # Update the entire canvas
            pygame.display.flip()
            # Limit the frame rate
            clock.tick(60)

    def display(self):
        self.screen.fill((175, 203, 173))

        move_list = stages_pet.stage('scr')
        self.body.update(move_list)
        self.body.display_all(self.screen)
