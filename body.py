import pygame
from tail import Tail
from eyes_ears import Eyes_ears


class Body:
    def __init__(self, _size):
        self.screen = None

        # set sizes
        self.size = _size
        self.x = self.size[0]
        self.drawing_x = self.x / 8
        self.y = self.size[1]
        self.drawing_y = self.y / 8

        # define colors
        self.fur_color = (248, 200, 135)  # Light brown
        self.nose_color = (255, 167, 182)  # Pink
        self.mouth_color = (0, 0, 0)  # Black
        self.leg_color = (50, 10, 0)  # Dark Brown
        self.feet_color = (100, 50, 10)

        # import leg picture
        leg = pygame.image.load("pictures/leg.png")
        self.resized_leg = pygame.transform.scale(leg, (self.drawing_x * 0.3, self.drawing_y * 1.7))

        # Initialize classes
        self.tail = Tail((self.x / 2, self.y / 2 + self.drawing_y * 0.55),
                         self.x, self.y,
                         self.drawing_x, self.drawing_y)
        self.eyes_ears = Eyes_ears(self.x, self.y, self.drawing_x, self.drawing_y)

    def display_all(self, _screen):
        self.screen = _screen

        self.tail.display_tail(self.screen)
        self.display_body()
        self.eyes_ears.display(self.screen)
        self.display_mouth()
        self.display_nose()
        self.display_legs()

    def update(self, move_list):
        self.eyes_ears.update(move_list[0], move_list[1])
        self.tail.update_tail(move_list[2], move_list[4])
        self.update_mouth(move_list[3])

    def display_body(self):
        rect_main_body = [self.x / 2 - (self.drawing_x * 1.5) / 2,
                          self.y / 2 - (self.drawing_y * 1.95) / 2,
                          self.drawing_x * 1.5,
                          self.drawing_y * 1.95]
        pygame.draw.ellipse(self.screen, self.fur_color, rect_main_body)
        rect_lower_body = [self.x / 2 - (self.drawing_x * 1.61) / 2,
                           self.y / 2 - (self.drawing_y * 0.91) / 2 + self.drawing_y * 0.7,
                           self.drawing_x * 1.61,
                           self.drawing_y * 0.91]
        pygame.draw.ellipse(self.screen, self.fur_color, rect_lower_body)
        rect_head = [self.x / 2 - (self.drawing_x * 1.5) / 2,
                     self.y / 2 - (self.drawing_y * 1.03) / 2 - self.drawing_y * 1.1,
                     self.drawing_x * 1.5,
                     self.drawing_y * 1.03]
        pygame.draw.ellipse(self.screen, self.fur_color, rect_head)

    def display_mouth(self):
        mouth_left = (self.x / 2 - self.drawing_x / 11,
                      self.y / 2 - self.drawing_y * 1.1,
                      self.drawing_x / 8,
                      self.drawing_y / 4)
        pygame.draw.arc(self.screen, self.mouth_color, mouth_left, 4.51, 0)

        mouth_right = (self.x / 2,
                       self.y / 2 - self.drawing_y * 1.1,
                       self.drawing_x / 8,
                       self.drawing_y / 4)
        pygame.draw.arc(self.screen, self.mouth_color, mouth_right, 3.14, 4.91)

    def update_mouth(self, mouth_pos_):
        self.mouth_pos = mouth_pos_

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

    def display_legs(self):
        # Feet in the back
        left_back_leg = (self.x / 2 - self.drawing_x * 0.8,
                         self.y / 2 + self.drawing_y * 0.55,
                         self.drawing_x * 0.6,
                         self.drawing_y * 0.5)
        pygame.draw.ellipse(self.screen, self.feet_color, left_back_leg)

        right_back_leg = (self.x / 2 + self.drawing_x * 0.2,
                          self.y / 2 + self.drawing_y * 0.55,
                          self.drawing_x * 0.6,
                          self.drawing_y * 0.5)
        pygame.draw.ellipse(self.screen, self.feet_color, right_back_leg)

        left_back_foot = (self.x / 2 - self.drawing_x * 0.68,
                          self.y / 2 + self.drawing_y * 0.7,
                          self.drawing_x * 0.3,
                          self.drawing_y * 0.4)
        pygame.draw.ellipse(self.screen, self.leg_color, left_back_foot)

        right_back_foot = (self.x / 2 + self.drawing_x * 0.38,
                           self.y / 2 + self.drawing_y * 0.7,
                           self.drawing_x * 0.3,
                           self.drawing_y * 0.4)
        pygame.draw.ellipse(self.screen, self.leg_color, right_back_foot)

        # Front legs
        position_right = (self.x / 2 + self.drawing_x * 0.2,
                          self.y / 2 - self.drawing_y * 0.5)
        position_left = (self.x / 2 - self.drawing_x * 0.5,
                         self.y / 2 - self.drawing_y * 0.5)
        self.screen.blit(self.resized_leg, position_right)
        self.screen.blit(self.resized_leg, position_left)

        # Feet in the front
        left_front_foot = (self.x / 2 - self.drawing_x * 0.56,
                           self.y / 2 + self.drawing_y * 0.98,
                           self.drawing_x * 0.4,
                           self.drawing_y * 0.3)
        pygame.draw.ellipse(self.screen, self.leg_color, left_front_foot)

        right_front_foot = (self.x / 2 + self.drawing_x * 0.15,
                            self.y / 2 + self.drawing_y * 0.98,
                            self.drawing_x * 0.4,
                            self.drawing_y * 0.3)
        pygame.draw.ellipse(self.screen, self.leg_color, right_front_foot)
