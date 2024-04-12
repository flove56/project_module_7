import pygame


class Eyes_ears:
    def __init__(self, x_, y_, drawing_x_, drawing_y_):
        self.x = x_
        self.y = y_
        self.drawing_x = drawing_x_
        self.drawing_y = drawing_y_

        self.angle_ears = 15
        self.ears_pos_indication = None
        self.ears_wanted_scalers = [0.8, 2.1, 0.1, 2.11]
        self.ears_scalers_now = [0.8, 2.1, 0.1, 2.11]
        self.change_state = False

        # define colors
        self.eye_color = (237, 237, 0)  # (212, 235, 242)  # Light blue # dark yellow (237, 237, 0)
        # light yellow (255, 255, 161)
        self.iris_color = (255, 255, 255)  # White
        self.pupil_color = (0, 0, 0)  # Black
        self.eyes_lashes_color = (0, 0, 0)  # Black

        # ears import pictures
        left_ear_img = pygame.image.load("pictures/left ear.png")
        right_ear_img = pygame.image.load("pictures/right ear.png")
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
        if self.eyes_open_bool is True:
            # Sclera
            left_eye_surf = pygame.Surface(self.left_scrala.size, pygame.SRCALPHA)
            pygame.draw.ellipse(left_eye_surf, self.eye_color, (0, 0, *self.left_scrala.size))
            rotated_left_eye = pygame.transform.rotate(left_eye_surf, 350)
            self.screen.blit(rotated_left_eye, rotated_left_eye.get_rect(center=self.left_scrala.center))

            right_eye_surf = pygame.Surface(self.right_scrala.size, pygame.SRCALPHA)
            pygame.draw.ellipse(right_eye_surf, self.eye_color, (0, 0, *self.right_scrala.size))
            rotated_right_eye = pygame.transform.rotate(right_eye_surf, 10)
            self.screen.blit(rotated_right_eye, rotated_right_eye.get_rect(center=self.right_scrala.center))

            # Iris
            pygame.draw.ellipse(self.screen, self.iris_color, self.left_iris)
            pygame.draw.ellipse(self.screen, self.iris_color, self.right_iris)

            # Pupil
            pygame.draw.ellipse(self.screen, self.pupil_color, self.left_pupil)
            pygame.draw.ellipse(self.screen, self.pupil_color, self.right_pupil)

        if self.eyes_open_bool is False:
            if self.eyes_closed_awake is True:
                # curved closed eyes
                left_eye_closed = (self.x / 2 - self.drawing_x * 0.5,
                                   self.y / 2 - self.drawing_y * 1.32,
                                   self.drawing_x * 0.35,
                                   self.drawing_y * 0.3)
                pygame.draw.arc(self.screen, self.eyes_lashes_color, left_eye_closed,
                                0, 1.57, 2)

                right_eye_closed = (self.x / 2 + self.drawing_x * 0.17,
                                    self.y / 2 - self.drawing_y * 1.32,
                                    self.drawing_x * 0.35,
                                    self.drawing_y * 0.3)
                pygame.draw.arc(self.screen, self.eyes_lashes_color, right_eye_closed,
                                1.57, 3.14, 2)
            else:
                # straight closed eyes
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
        # the self.eyes_scale changes how big the eyes are, is smaller, then eyes bigger
        self.eyes_scale = eyes_stages['scale']
        self.eyes_big_bool = eyes_stages['big_bool']
        self.eyes_open_bool = eyes_stages['open_bool']
        self.eyes_closed_awake = eyes_stages['closed_bool_awake']

        if self.eyes_big_bool is True:
            self.left_scrala = pygame.Rect(self.x / 2 - self.drawing_x * 0.45,
                                           self.y / 2 - self.drawing_y * 1.35,
                                           self.drawing_x / 3,
                                           self.drawing_y / self.eyes_scale)

            self.right_scrala = pygame.Rect(self.x / 2 + self.drawing_x * 0.15,
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
            self.left_scrala = pygame.Rect(self.x / 2 - self.drawing_x * 0.45,
                                           self.y / 2 - self.drawing_y * 1.3,
                                           self.drawing_x / 3,
                                           self.drawing_y / self.eyes_scale)

            self.right_scrala = pygame.Rect(self.x / 2 + self.drawing_x * 0.15,
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
        position_left = (self.x / 2 - self.drawing_x * self.ears_scalers_now[0],
                         self.y / 2 - self.drawing_y * self.ears_scalers_now[1])
        position_right = (self.x / 2 + self.drawing_x * self.ears_scalers_now[2],
                          self.y / 2 - self.drawing_y * self.ears_scalers_now[3])

        left_ear_rot = pygame.transform.rotate(self.left_ear, self.angle_ears)
        self.screen.blit(left_ear_rot, position_left)

        right_ear_rot = pygame.transform.rotate(self.right_ear, int(360 - self.angle_ears - 1))
        self.screen.blit(right_ear_rot, position_right)

    def update_ears(self, ears_stages, change_state_):
        if change_state_:
            self.change_state = change_state_
            if self.ears_pos_indication is not ears_stages['position']:
                self.ears_pos_indication = ears_stages['position']
                if self.ears_pos_indication == 'reg':
                    self.ears_wanted_scalers = [0.8, 2.1, 0.1, 2.11]
                if self.ears_pos_indication == 'low':
                    self.ears_wanted_scalers = [1.1, 2, 0.28, 2]
                if self.ears_pos_indication == 'high':
                    self.ears_wanted_scalers = [0.7, 2.12, 0.05, 2.13]

        if self.change_state is True:
            print(self.angle_ears, ears_stages['angle'])
            for scaler in range(len(self.ears_wanted_scalers)):
                if self.ears_scalers_now[scaler] > self.ears_wanted_scalers[scaler]:
                    self.ears_scalers_now[scaler] -= 0.01
                if self.ears_scalers_now[scaler] < self.ears_wanted_scalers[scaler]:
                    self.ears_scalers_now[scaler] += 0.01
            if self.angle_ears > ears_stages['angle']:
                self.angle_ears -= 0.5
            if self.angle_ears < ears_stages['angle']:
                self.angle_ears += 0.5
            if (self.ears_wanted_scalers[2] - 0.005 >= self.ears_scalers_now[2] >=
                    self.ears_wanted_scalers[2] + 0.005 and
                    ears_stages['angle'] - 0.05 >= self.angle_ears >=
                    ears_stages['angle'] + 0.05):
                self.change_state = False

