import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512)) #This line defines the size of the window, (screen resolution)
        clock = pygame.time.Clock() #This line is a for loop that will get all the events happening to your window
        running = True
        game = 0
        while running:
            #grid is 32x32 increment by 32 so just use loop
            for event in pygame.event.get(): #pygame.event.get() is when something happens to pygame
                if event.type == pygame.QUIT: #this is when the corner x gets clicked
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if rect.collidepoint(mouse_pos):
                        game = 1
                        mole_pos = (random.randrange(0, 19)*32, random.randrange(0, 15)*32)

            screen.fill("light blue") #fills with color that you want

            if game == 0:
                mole_pos = (0,0)
            #creating collision rectangle
            rect = pygame.Rect(mole_pos, (36, 36))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pos)))


            y = 0
            while y < 512:
                y += 32
                pygame.draw.line(screen, 'black', (0, y), (640, y))
            x = 0
            while x < 640:
                x += 32
                pygame.draw.line(screen, 'black', (x,0), (x, 512))
            pygame.display.flip() #updates the screen
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

