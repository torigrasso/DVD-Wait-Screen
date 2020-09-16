from pygame import mixer
import pygame


class Image():
    def __init__(self, filename):
        self.file = filename
        self.x1 = self.y1 = 300
        self.change_x1 = 2
        self.change_y1 = 3

    def move(self):
        # x coordinate check
        if self.x1 < 0 or self.x1 > 500 - 80:
            self.change_x1 = -self.change_x1
        # y coordinate check
        if self.y1 < 180 or self.y1 > 500 - 80:
            self.change_y1 = -self.change_y1

        self.x1 += self.change_x1
        self.y1 += self.change_y1

    def draw(self, screen):
        img = pygame.image.load(self.file)
        img = pygame.transform.scale(img, (100, 100))
        screen.blit(img, (self.x1, self.y1))


def create_window():
    screen = pygame.display.set_mode((500, 500))
    screen.fill(BLACK)
    pygame.display.set_caption('Simulation')
    return screen


def main():

    pygame.init()
    clock = pygame.time.Clock()

    # define global color
    global BLACK
    BLACK = (0, 0, 0)

    img = Image("dvdBlue.png")  # create the image
    screen = create_window()  # create window
    done = False
    while not done:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_ESCAPE]:
                    done = True

        img.draw(screen)
        img.move()

        pygame.display.update()
        clock.tick(30)

    pygame.quit()


main()
