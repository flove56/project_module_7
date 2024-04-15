import pygame


class Eyes_ears:
    def __init__(self, x_, y_, drawing_x_, drawing_y_):
        # Initialize drawing parameters
        self.x = x_
        self.y = y_
        self.drawing_x = drawing_x_
        self.drawing_y = drawing_y_

        # Set the ears variables for the start
        self.angle_ears = 15
        self.ears_pos_indication = None

        # Set the scalers for the ears for the different positions
        self.ears_wanted_scalers_reg = [0.8, 2.1, 0.1, 2.11]
        self.ears_wanted_scalers_low = [1.1, 2, 0.28, 2]
        self.ears_wanted_scalers_high = [0.7, 2.12, 0.02, 2.13]
        # Initialize the scalers for the start
        self.ears_wanted_scalers = self.ears_wanted_scalers_reg
        self.ears_scalers_now = [0.8, 2.1, 0.1, 2.11]
        # Calculate the proportions for the animations
        self.scalers_for_the_changes = []
        for position in range(len(self.ears_wanted_scalers)):
            self.scalers_for_the_changes.append((abs(self.ears_wanted_scalers_high[position] -
                                                     self.ears_wanted_scalers_low[position]))/50)
        # Initialize the change state as false
        self.change_state = False

        # Define the colors
        self.eye_color = (237, 237, 0)  # (212, 235, 242)  # Light blue # dark yellow (237, 237, 0)
        # light yellow (255, 255, 161)
        self.iris_color = (255, 255, 255)  # White
        self.pupil_color = (0, 0, 0)  # Black
        self.eyes_lashes_color = (0, 0, 0)  # Black

        # Import the pictures of the ears
        left_ear_img = pygame.image.load("pictures/left ear.png")
        right_ear_img = pygame.image.load("pictures/right ear.png")
        # Resize the ear pictures
        self.picture_size = (self.drawing_x * 0.6, self.drawing_y * 0.6)
        self.left_ear = pygame.transform.scale(left_ear_img, self.picture_size)
        self.right_ear = pygame.transform.scale(right_ear_img, self.picture_size)

    def display(self, screen_):
        self.screen = screen_
        self.display_eyes()
        self.display_ears()

    def update(self, ears_stages_, eyes_stages_, change_state):
        self.update_eyes(eyes_stages_)
        self.update_ears(ears_stages_, change_state)

    def display_eyes(self):
        # If the eyes are open create the open eyes
        if self.eyes_open_bool is True:
            # Sclera
            # Create a surface for the left eye
            left_eye_surf = pygame.Surface(self.left_sclera.size, pygame.SRCALPHA)
            # Create an ellipse on the surface
            pygame.draw.ellipse(left_eye_surf, self.eye_color, (0, 0, *self.left_sclera.size))
            # Rotate the left eye
            rotated_left_eye = pygame.transform.rotate(left_eye_surf, 350)
            # Add the Sclera to the screen
            self.screen.blit(rotated_left_eye, rotated_left_eye.get_rect(center=self.left_sclera.center))

            # Create a surface for the left eye
            right_eye_surf = pygame.Surface(self.right_sclera.size, pygame.SRCALPHA)
            # Create an ellipse on the surface
            pygame.draw.ellipse(right_eye_surf, self.eye_color, (0, 0, *self.right_sclera.size))
            # Rotate the left eye
            rotated_right_eye = pygame.transform.rotate(right_eye_surf, 10)
            # Add the Sclera to the screen
            self.screen.blit(rotated_right_eye, rotated_right_eye.get_rect(center=self.right_sclera.center))

            # Iris
            pygame.draw.ellipse(self.screen, self.iris_color, self.left_iris)
            pygame.draw.ellipse(self.screen, self.iris_color, self.right_iris)

            # Pupil
            pygame.draw.ellipse(self.screen, self.pupil_color, self.left_pupil)
            pygame.draw.ellipse(self.screen, self.pupil_color, self.right_pupil)

        # If the eyes are closed create the open eyes
        if self.eyes_open_bool is False:
            # If the pet is awake create these lines
            if self.eyes_closed_awake is True:
                # Curved closed eyes
                # Create a rectangle for the left eye
                left_eye_closed = (self.x / 2 - self.drawing_x * 0.5,
                                   self.y / 2 - self.drawing_y * 1.32,
                                   self.drawing_x * 0.35,
                                   self.drawing_y * 0.3)
                # Draw an arc in the rectangle
                pygame.draw.arc(self.screen, self.eyes_lashes_color, left_eye_closed,
                                0, 1.57, 2)

                # Create a rectangle for the right eye
                right_eye_closed = (self.x / 2 + self.drawing_x * 0.17,
                                    self.y / 2 - self.drawing_y * 1.32,
                                    self.drawing_x * 0.35,
                                    self.drawing_y * 0.3)
                # Draw an arc in the rectangle
                pygame.draw.arc(self.screen, self.eyes_lashes_color, right_eye_closed,
                                1.57, 3.14, 2)
            else:
                # If the pet is not awake create these lines
                # Straight closed eyes
                # Left eye
                pygame.draw.line(self.screen, self.eyes_lashes_color,
                                 (self.x / 2 - self.drawing_x * 0.3,
                                  self.y / 2 - self.drawing_y * 1.2),
                                 (self.x / 2 - self.drawing_x * 0.15,
                                  self.y / 2 - self.drawing_y * 1.2),
                                 2)

                # Right eye
                pygame.draw.line(self.screen, self.eyes_lashes_color,
                                 (self.x / 2 + self.drawing_x * 0.15,
                                  self.y / 2 - self.drawing_y * 1.2),
                                 (self.x / 2 + self.drawing_x * 0.3,
                                  self.y / 2 - self.drawing_y * 1.2),
                                 2)

    def update_eyes(self, eyes_stages):
        # Set the variables to the given variables
        self.eyes_scale = eyes_stages['scale']
        self.eyes_big_bool = eyes_stages['big_bool']
        self.eyes_open_bool = eyes_stages['open_bool']
        self.eyes_closed_awake = eyes_stages['closed_bool_awake']

        # If the eyes are big set these rectangles
        if self.eyes_big_bool is True:
            self.left_sclera = pygame.Rect(self.x / 2 - self.drawing_x * 0.45,
                                           self.y / 2 - self.drawing_y * 1.35,
                                           self.drawing_x / 3,
                                           self.drawing_y / self.eyes_scale)

            self.right_sclera = pygame.Rect(self.x / 2 + self.drawing_x * 0.15,
                                            self.y / 2 - self.drawing_y * 1.35,
                                            self.drawing_x / 3,
                                            self.drawing_y / self.eyes_scale)

            self.left_iris = (self.x / 2 - self.drawing_x * 0.38,
                              self.y / 2 - self.drawing_y * 1.29,
                              self.drawing_x / (self.eyes_scale * 1.5),
                              self.drawing_y / (self.eyes_scale * 1.5))

            self.right_iris = (self.x / 2 + self.drawing_x * 0.21,
                               self.y / 2 - self.drawing_y * 1.29,
                               self.drawing_x / (self.eyes_scale * 1.5),
                               self.drawing_y / (self.eyes_scale * 1.5))

            self.left_pupil = (self.x / 2 - self.drawing_x * 0.33,
                               self.y / 2 - self.drawing_y * 1.25,
                               self.drawing_x / (self.eyes_scale * 2.5),
                               self.drawing_y / (self.eyes_scale * 2.5))

            self.right_pupil = (self.x / 2 + self.drawing_x * 0.25,
                                self.y / 2 - self.drawing_y * 1.25,
                                self.drawing_x / (self.eyes_scale * 2.5),
                                self.drawing_y / (self.eyes_scale * 2.5))
        else:
            # If the eyes are small set these rectangles
            self.left_sclera = pygame.Rect(self.x / 2 - self.drawing_x * 0.45,
                                           self.y / 2 - self.drawing_y * 1.3,
                                           self.drawing_x / 3,
                                           self.drawing_y / self.eyes_scale)

            self.right_sclera = pygame.Rect(self.x / 2 + self.drawing_x * 0.15,
                                            self.y / 2 - self.drawing_y * 1.3,
                                            self.drawing_x / 3,
                                            self.drawing_y / self.eyes_scale)

            self.left_iris = (self.x / 2 - self.drawing_x * 0.36,
                              self.y / 2 - self.drawing_y * 1.26,
                              self.drawing_x / (self.eyes_scale * 1.4),
                              self.drawing_y / (self.eyes_scale * 1.4))

            self.right_iris = (self.x / 2 + self.drawing_x * 0.20,
                               self.y / 2 - self.drawing_y * 1.26,
                               self.drawing_x / (self.eyes_scale * 1.4),
                               self.drawing_y / (self.eyes_scale * 1.4))

            self.left_pupil = (self.x / 2 - self.drawing_x * 0.32,
                               self.y / 2 - self.drawing_y * 1.225,
                               self.drawing_x / (self.eyes_scale * 2.2),
                               self.drawing_y / (self.eyes_scale * 2.2))

            self.right_pupil = (self.x / 2 + self.drawing_x * 0.235,
                                self.y / 2 - self.drawing_y * 1.225,
                                self.drawing_x / (self.eyes_scale * 2.2),
                                self.drawing_y / (self.eyes_scale * 2.2))

    def display_ears(self):
        # Create the position of the ears.
        position_left = (self.x / 2 - self.drawing_x * self.ears_scalers_now[0],
                         self.y / 2 - self.drawing_y * self.ears_scalers_now[1])
        position_right = (self.x / 2 + self.drawing_x * self.ears_scalers_now[2],
                          self.y / 2 - self.drawing_y * self.ears_scalers_now[3])

        # Rotate the left ear to the correct angle
        left_ear_rot = pygame.transform.rotate(self.left_ear, self.angle_ears)
        # Add the picture to the screen
        self.screen.blit(left_ear_rot, position_left)

        # Rotate the right ear to the correct angle
        right_ear_rot = pygame.transform.rotate(self.right_ear, int(360 - self.angle_ears - 1))
        # Add the picture to the screen
        self.screen.blit(right_ear_rot, position_right)

    def update_ears(self, ears_stages, change_state_):
        # When there is a different state move the ears to the correct position
        if change_state_:  # This happens once
            # The state of the class is the state from stages_pet
            self.change_state = change_state_
            # If the position is different change the position indication
            if self.ears_pos_indication is not ears_stages['position']:
                self.ears_pos_indication = ears_stages['position']
                # Change the wanted scalers to the scalers corresponding of the position
                if self.ears_pos_indication == 'reg':
                    self.ears_wanted_scalers = self.ears_wanted_scalers_reg
                if self.ears_pos_indication == 'low':
                    self.ears_wanted_scalers = self.ears_wanted_scalers_low
                if self.ears_pos_indication == 'high':
                    self.ears_wanted_scalers = self.ears_wanted_scalers_high

        # Is the change state of the class is true
        if self.change_state is True:  # this happens multiple times
            # Adjust each scaler with its own proportions
            for scaler in range(len(self.ears_wanted_scalers)):
                if self.ears_scalers_now[scaler] > self.ears_wanted_scalers[scaler]:
                    self.ears_scalers_now[scaler] -= self.scalers_for_the_changes[scaler]
                if self.ears_scalers_now[scaler] < self.ears_wanted_scalers[scaler]:
                    self.ears_scalers_now[scaler] += self.scalers_for_the_changes[scaler]
            # Change the angle of the ears
            if self.angle_ears > ears_stages['angle']:
                self.angle_ears -= 0.5
            if self.angle_ears < ears_stages['angle']:
                self.angle_ears += 0.5
            # Change the change_state of the class when the ears are in the correct position
            if (self.ears_wanted_scalers[2] - 0.005 >= self.ears_scalers_now[2] >=
                    self.ears_wanted_scalers[2] + 0.005 and
                    ears_stages['angle'] - 0.05 >= self.angle_ears >=
                    ears_stages['angle'] + 0.05):
                self.change_state = False

