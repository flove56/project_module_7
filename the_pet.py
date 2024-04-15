from body import Body
import pygame
import stages_pet
from file_d_read_real_time import real_time_reading
from sounds import Sounds
from background import Background


class The_pet:
    def __init__(self):
        # Set the screen size
        self.size = (800, 800)

        # Set up pygame and a screen
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        # Initialize classes
        self.background = Background(self.size)
        self.body = Body(self.size)
        self.sound = Sounds()
        self.read_state = real_time_reading()

        # Set the initial state to regular
        self.state = 'reg'
        self.last_state = 'reg'


    def game_loop(self):
        clock = pygame.time.Clock()

        while True:
            # Check for pygame events
            for event in pygame.event.get():
                # If the screen is closed quit program
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Read the state and gather gestures
            #self.test_key()  # Use keys as input for states
            # Use the touch patch as input for the states:
            self.read_state.do_one_reading()
            self.state = self.read_state.get_the_smooth_state(self.state)

            self.render()

            # Update the entire canvas
            pygame.display.flip()
            # Limit the frame rate
            clock.tick(60)

    def render(self):
        # Set the background
        self.background.display(self.screen)
        # Set the variables of the pet according to the correct state
        move_list = stages_pet.stage(self.state, self.last_state)
        # Update the body to the correct state
        self.body.update_all(move_list)
        # Set the last state to the current state
        self.last_state = self.state
        # Display the animal
        self.body.display_all(self.screen)
        # Play the correct sound for the state
        self.sound.play_sound(move_list[3], self.state)

    def test_key(self):
        # Use keys as input for the different state
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
