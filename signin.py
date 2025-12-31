import pygame 
import os 

pygame.init()

WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sign in")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (217, 217, 217)

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True
username = "User123457890"
password = "1234567890"

while running:
    screen.fill(GREY)

    pygame.draw.rect(screen, WHITE, (200, 180, 300, 40)) #username 
    pygame.draw.rect(screen, WHITE, (200, 260, 300, 40)) # password 
    pygame.draw.rect(screen, BLACK, (200, 180, 300, 40), 2) #username 
    pygame.draw.rect(screen, BLACK, (200, 260, 300, 40), 2) #password 

    user_text = font.render(username, True, BLACK)
    pass_text = font.render("*" * len(password), True, BLACK)
    screen.blit(user_text, (210, 185)) 
    screen.blit(pass_text, (210, 265))

    label1 = font.render("Username:", True, BLACK)
    label2 = font.render("Password:", True, BLACK)
    screen.blit(label1, (200, 150))
    screen.blit(label2, (200, 230))

    pygame.draw.rect(screen, WHITE, (250, 350, 200, 50))
    pygame.draw.rect(screen, BLACK, (250, 350, 200, 50), 2)
    login_text = font.render("Log in", True, BLACK)
    screen.blit(login_text, (310, 360))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if  pygame.Rect(250, 350, 200, 50).collidepoint(event.pos):
                pygame.quit()
                os.system("python Mainmenu.py")
                exit()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

