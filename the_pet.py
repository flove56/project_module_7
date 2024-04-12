from body import Body
import pygame
import stages_pet
# from a_four_read_real_time import real_time_reading


class The_pet:
    def __init__(self):
        self.state = 'reg'
        self.size = (800, 800)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        self.body = Body(self.size)
        #self.read_state = real_time_reading()
        self.last_state = 'reg'


    def game_loop(self):
        clock = pygame.time.Clock()

        while True:
            # Check for pygame events
            for event in pygame.event.get():
                # If the screen is closed quit program
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Call all functions
            self.test_key()
            # per 10 of 20 frames pas kijken misschien? of twee python dingen
            #self.state = self.read_state.get_the_smooth_state()
            self.display()

            # Update the entire canvas
            pygame.display.flip()
            # Limit the frame rate
            clock.tick(60)

    def display(self):
        self.screen.fill((175, 203, 173))

        self.body.update(stages_pet.stage(self.state, self.last_state))
        self.last_state = self.state
        self.body.display_all(self.screen)

    def test_key(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_0]:
            self.state = 'reg'
        if key[pygame.K_1]:
            self.state = 'pet'
        if key[pygame.K_2]:
            self.state = 'pok'
        if key[pygame.K_3]:
            self.state = 'com'
        if key[pygame.K_4]:
            self.state = 'scr'
