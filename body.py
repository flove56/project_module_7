import pygame


class Body:
    def __init__(self, _size):
        self.size = _size
        self.x = self.size[0]
        self.drawing_x = self.x / 8
        self.y = self.size[1]
        self.drawing_y = self.y / 8
        self.eye_color = (237, 237, 0)  # (212, 235, 242)  # Light blue # dark yellow (237, 237, 0) # light yellow (255, 255, 161)
        self.iris_color = (255, 255, 255)  # White
        self.pupil_color = (0, 0, 0)  # Black
        self.nose_color = (255, 167, 182)  # Pink
        self.mouth_color = (0, 0, 0)  # Black

    def display(self, _screen):
        self.screen = _screen

        self.display_body()
        self.display_ears()
        self.display_eyes()
        self.display_mouth()
        self.display_nose()


    def display_body(self):
        fur_color = (248, 200, 135)
        rect_main_body = [self.x / 2 - (self.drawing_x * 1.5) / 2,
                          self.y / 2 - (self.drawing_y * 1.95) / 2,
                          self.drawing_x * 1.5,
                          self.drawing_y * 1.95]
        pygame.draw.ellipse(self.screen, fur_color, rect_main_body)
        rect_lower_body = [self.x / 2 - (self.drawing_x * 1.81) / 2,
                           self.y / 2 - (self.drawing_y * 0.91) / 2 + self.drawing_y * 0.7,
                           self.drawing_x * 1.81,
                           self.drawing_y * 0.91]
        pygame.draw.ellipse(self.screen, fur_color, rect_lower_body)
        rect_head = [self.x / 2 - (self.drawing_x * 1.5) / 2,
                     self.y / 2 - (self.drawing_y * 1.03) / 2 - self.drawing_y * 1.1,
                     self.drawing_x * 1.5,
                     self.drawing_y * 1.03]
        pygame.draw.ellipse(self.screen, fur_color, rect_head)

    def display_ears(self):
        """
        first have the rotation of left ears
        happy/normal = 18
        then the right ears
        happy/normal = 341
        :return: displays ears
        """
        left_ear = pygame.image.load("pictures/left ear.png")
        left_ear_rot = pygame.transform.rotate(left_ear, 18)
        position_left = (self.x / 2 - self.drawing_x * 0.9,
                         self.y / 2 - self.drawing_y * 2.15)
        self.screen.blit(left_ear_rot, position_left)

        right_ear = pygame.image.load("pictures/right ear.png")
        right_ear_rot = pygame.transform.rotate(right_ear, 341)
        position_left = (self.x / 2 + self.drawing_x * 0.12,
                         self.y / 2 - self.drawing_y * 2.15)
        self.screen.blit(right_ear_rot, position_left)

    def display_eyes(self):
        # this changes how big the eyes are, is smaller, then eyes bigger
        big = 4

        # Sclera
        left_eye = pygame.Rect(self.x / 2 - self.drawing_x * 0.45,
                               self.y / 2 - self.drawing_y * 1.3,
                               self.drawing_x / 3,
                               self.drawing_y / big)
        # left_eye_rot = pygame.transform.rotate(left_eye, 20)
        # pygame.draw.arc(self.screen, self.eye_color, left_eye, 0, 3.14, 80)
        # pygame.draw.arc(self.screen, self.eye_color, left_eye, 3.14, 0, 80)
        # pygame.draw.ellipse(self.screen, self.eye_color, left_eye_rot)
        left_eye_surf = pygame.Surface(left_eye.size, pygame.SRCALPHA)
        pygame.draw.ellipse(left_eye_surf, self.eye_color, (0, 0, *left_eye.size))
        rotated_left_eye = pygame.transform.rotate(left_eye_surf, 350)
        self.screen.blit(rotated_left_eye, rotated_left_eye.get_rect(center=left_eye.center))

        right_eye = pygame.Rect(self.x / 2 + self.drawing_x * 0.15,
                                self.y / 2 - self.drawing_y * 1.3,
                                self.drawing_x / 3,
                                self.drawing_y / big)
        right_eye_surf = pygame.Surface(right_eye.size, pygame.SRCALPHA)
        pygame.draw.ellipse(right_eye_surf, self.eye_color, (0, 0, *right_eye.size))
        rotated_right_eye = pygame.transform.rotate(right_eye_surf, 10)
        self.screen.blit(rotated_right_eye, rotated_right_eye.get_rect(center=right_eye.center))

        # Iris
        left_iris = (self.x / 2 - self.drawing_x * 0.35,
                     self.y / 2 - self.drawing_y * 1.26,
                     self.drawing_x / (big * 1.5),
                     self.drawing_y / (big * 1.5))
        pygame.draw.ellipse(self.screen, self.iris_color, left_iris)

        right_iris = (self.x / 2 + self.drawing_x * 0.23,
                      self.y / 2 - self.drawing_y * 1.26,
                      self.drawing_x / (big * 1.5),
                      self.drawing_y / (big * 1.5))
        pygame.draw.ellipse(self.screen, self.iris_color, right_iris)

        # Pupil
        left_pupil = (self.x / 2 - self.drawing_x * 0.31,
                      self.y / 2 - self.drawing_y * 1.23,
                      self.drawing_x / (big * 2.5),
                      self.drawing_y / (big * 2.5))
        pygame.draw.ellipse(self.screen, self.pupil_color, left_pupil)

        right_pupil = (self.x / 2 + self.drawing_x * 0.25,
                       self.y / 2 - self.drawing_y * 1.23,
                       self.drawing_x / (big * 2.5),
                       self.drawing_y / (big * 2.5))
        pygame.draw.ellipse(self.screen, self.pupil_color, right_pupil)

    def display_mouth(self):
        mouth_left = (self.x / 2 - self.drawing_x / 11,
                      self.y / 2 - self.drawing_y * 1.1,
                      self.drawing_x / 8,
                      self.drawing_y / 4)
        pygame.draw.arc(self.screen, self.mouth_color, mouth_left, 4.71, 0)

        mouth_right = (self.x / 2,
                       self.y / 2 - self.drawing_y * 1.1,
                       self.drawing_x / 8,
                       self.drawing_y / 4)
        pygame.draw.arc(self.screen, self.mouth_color, mouth_right, 3.14, 4.71)

    def display_nose(self):
        top_nose = (self.x / 2 - (self.drawing_x / 12),
                    self.y / 2 - self.drawing_y * 1.1,
                    self.drawing_x / 5,
                    self.drawing_y / 8)
        pygame.draw.ellipse(self.screen, self.nose_color, top_nose)
        bottom_nose = (self.x / 2 - (self.drawing_x / 20),
                       self.y / 2 - self.drawing_y * 1.1,
                       self.drawing_x / 9,
                       self.drawing_y / 6)
        pygame.draw.rect(self.screen, self.nose_color, bottom_nose, border_radius=8)
