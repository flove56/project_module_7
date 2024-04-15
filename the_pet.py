from body import Body
import pygame
import stages_pet
from a_four_read_real_time import real_time_reading
from sounds import Sounds
from background import Background


class The_pet:
    def __init__(self):
        self.state = 'reg'
        self.size = (800, 800)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.background = Background(self.size)
        self.body = Body(self.size)
        self.sound = Sounds()

        self.read_state = real_time_reading()
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
            #self.test_key()

            self.read_state.do_one_reading()
            self.state = self.read_state.get_the_smooth_state(self.state)
            self.render()

            # Update the entire canvas
            pygame.display.flip()
            # Limit the frame rate
            clock.tick(60)

    def render(self):
        self.background.display(self.screen)
        move_list = stages_pet.stage(self.state, self.last_state)
        self.body.update(move_list)
        self.last_state = self.state
        self.body.display_all(self.screen)
        self.sound.play_sound(move_list[4], self.state)

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
