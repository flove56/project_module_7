import pygame
from tail import Tail
from eyes_ears import Eyes_ears


class Body:
    def __init__(self, _size):
        self.screen = None

        # Initialize the width and height
        self.size = _size
        self.x = self.size[0]
        self.y = self.size[1]
        # Map the sizes to make simpler calculations
        self.drawing_x = self.x / 8
        self.drawing_y = self.y / 8

        # Define the colors
        self.fur_color = (248, 200, 135)  # Light brown
        self.nose_color = (255, 167, 182)  # Pink
        self.mouth_color = (0, 0, 0)  # Black
        self.leg_color = (50, 10, 0)  # Dark Brown
        self.feet_color = (100, 50, 10)  # between dark and light brown

        # Import the picture used for the legs
        leg = pygame.image.load("pictures/leg.png")
        # Set the image to the correct size
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

    def update_all(self, move_list):
        self.eyes_ears.update(move_list[0], move_list[1], move_list[3])
        self.tail.update_tail(move_list[2], move_list[3])

    def display_body(self):
        # Create a rectangle to put the torso into
        rect_main_body = [self.x / 2 - (self.drawing_x * 1.5) / 2,
                          self.y / 2 - (self.drawing_y * 1.95) / 2,
                          self.drawing_x * 1.5,
                          self.drawing_y * 1.95]
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.fur_color, rect_main_body)
        # Create a rectangle to put the lower body into
        rect_lower_body = [self.x / 2 - (self.drawing_x * 1.61) / 2,
                           self.y / 2 - (self.drawing_y * 0.91) / 2 + self.drawing_y * 0.7,
                           self.drawing_x * 1.61,
                           self.drawing_y * 0.91]
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.fur_color, rect_lower_body)
        # Create a rectangle to put the head into
        rect_head = [self.x / 2 - (self.drawing_x * 1.5) / 2,
                     self.y / 2 - (self.drawing_y * 1.03) / 2 - self.drawing_y * 1.1,
                     self.drawing_x * 1.5,
                     self.drawing_y * 1.03]
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.fur_color, rect_head)

    def display_mouth(self):
        # Create a rectangle to put the left side of the mouth into
        mouth_left = (self.x / 2 - self.drawing_x / 11,
                      self.y / 2 - self.drawing_y * 1.1,
                      self.drawing_x / 8,
                      self.drawing_y / 4)
        # Draw an arc into the rectangle
        pygame.draw.arc(self.screen, self.mouth_color, mouth_left, 4.51, 0)

        # Create a rectangle to put the right side of the mouth into
        mouth_right = (self.x / 2,
                       self.y / 2 - self.drawing_y * 1.1,
                       self.drawing_x / 8,
                       self.drawing_y / 4)
        # Draw an arc into the rectangle
        pygame.draw.arc(self.screen, self.mouth_color, mouth_right, 3.14, 4.91)

    def display_nose(self):
        # Create a rectangle to put the top of the nose into
        top_nose = (self.x / 2 - (self.drawing_x / 12),
                    self.y / 2 - self.drawing_y * 1.1,
                    self.drawing_x / 5,
                    self.drawing_y / 8)
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.nose_color, top_nose)
        # Create a rectangle to put the bottom of the nose into
        bottom_nose = (self.x / 2 - (self.drawing_x / 30),
                       self.y / 2 - self.drawing_y * 1.1,
                       self.drawing_x / 9,
                       self.drawing_y / 6)
        # Draw a rectangle with rounded corners in the rectangle
        pygame.draw.rect(self.screen, self.nose_color, bottom_nose, border_radius=8)

    def display_legs(self):
        # Create the feet in the back
        # Create a rectangle to put the left back leg into
        left_back_leg = (self.x / 2 - self.drawing_x * 0.8,
                         self.y / 2 + self.drawing_y * 0.55,
                         self.drawing_x * 0.6,
                         self.drawing_y * 0.5)
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.feet_color, left_back_leg)

        # Create a rectangle to put the right back leg into
        right_back_leg = (self.x / 2 + self.drawing_x * 0.2,
                          self.y / 2 + self.drawing_y * 0.55,
                          self.drawing_x * 0.6,
                          self.drawing_y * 0.5)
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.feet_color, right_back_leg)

        # Create a rectangle to put the left back foot into
        left_back_foot = (self.x / 2 - self.drawing_x * 0.68,
                          self.y / 2 + self.drawing_y * 0.7,
                          self.drawing_x * 0.3,
                          self.drawing_y * 0.4)
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.leg_color, left_back_foot)

        # Create a rectangle to put the right back foot into
        right_back_foot = (self.x / 2 + self.drawing_x * 0.38,
                           self.y / 2 + self.drawing_y * 0.7,
                           self.drawing_x * 0.3,
                           self.drawing_y * 0.4)
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.leg_color, right_back_foot)

        # Create the legs in the front
        # Set the position of the legs
        position_right = (self.x / 2 + self.drawing_x * 0.2,
                          self.y / 2 - self.drawing_y * 0.5)
        position_left = (self.x / 2 - self.drawing_x * 0.5,
                         self.y / 2 - self.drawing_y * 0.5)
        # Display the pictures of the legs
        self.screen.blit(self.resized_leg, position_right)
        self.screen.blit(self.resized_leg, position_left)

        # Create the feet in the front
        # Create a rectangle to put the left front foot into
        left_front_foot = (self.x / 2 - self.drawing_x * 0.56,
                           self.y / 2 + self.drawing_y * 0.98,
                           self.drawing_x * 0.4,
                           self.drawing_y * 0.3)
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.leg_color, left_front_foot)

        # Create a rectangle to put the right front foot into
        right_front_foot = (self.x / 2 + self.drawing_x * 0.15,
                            self.y / 2 + self.drawing_y * 0.98,
                            self.drawing_x * 0.4,
                            self.drawing_y * 0.3)
        # Draw an ellipse in the rectangle
        pygame.draw.ellipse(self.screen, self.leg_color, right_front_foot)
