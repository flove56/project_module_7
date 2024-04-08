import pygame

class Body:
    def __init__(self, _size):
        self.size = _size
        self.x = self.size[0]
        self.drawing_x = self.x/8
        self.y = self.size[1]
        self.drawing_y = self.y/8

    def display(self, _screen):
        self.screen = _screen

        self.display_body()
        self.display_ears()

    def display_body(self):
        fur_color = (255, 195, 20)
        rect_main_body = [self.x/2 - self.drawing_x*1.5/2,
                          self.y/2 - self.drawing_y*1.95/2,
                          self.drawing_x*1.5,
                          self.drawing_y*1.95]
        pygame.draw.ellipse(self.screen, fur_color , rect_main_body)
        rect_lower_body = [self.x/2 - self.drawing_x*1.81/2,
                          self.y/2 - self.drawing_y*0.91/2+ self.drawing_y*0.7,
                          self.drawing_x*1.81,
                          self.drawing_y*0.91]
        pygame.draw.ellipse(self.screen, fur_color, rect_lower_body)
        rect_head = [self.x / 2 - self.drawing_x * 1.5 / 2,
                     self.y / 2 - self.drawing_y * 1.03 / 2 - self.drawing_y * 1.1,
                     self.drawing_x * 1.5,
                     self.drawing_y * 1.03]
        pygame.draw.ellipse(self.screen, fur_color, rect_head)

    def display_ears(self):
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