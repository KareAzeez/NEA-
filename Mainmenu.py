import pygame 
import os 

# Initialize Pygame
pygame.init()

# Define colors
GREY = (217, 217, 217)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Main menu")

# Define font 
font = pygame.font.Font(None, 40)  
small_font = pygame.font.Font(None, 30)
show_dropdown = False

# Initialize clock
clock = pygame.time.Clock()

# done variable to control the loop
running = True 

while running:
     # Fill background inside the loop
    screen.fill(GREY)

    title = font.render("Main Menu", True, BLACK)
    screen.blit(title, (300,40))
    
    # Draw a long black line underneath the rectangles
    pygame.draw.line(screen, BLACK, (0, 85), (800, 85), 2) # (start_pos, end_pos, thickness)

    # Rectangle for User profile 
    pygame.draw.rect(screen, WHITE, [290, 230, 210, 50], border_radius = 10)  # Backround 
    pygame.draw.rect(screen, WHITE, [290, 230, 210, 50], 2, border_radius = 10)  # Challenges icon 

    
    pygame.draw.rect(screen, WHITE, [290, 370, 210, 50], border_radius = 10)  # Backround 
    pygame.draw.rect(screen, WHITE, [290, 370, 210, 50], 2, border_radius = 10)  # Log out  icon 

    
     # Render text "About Business Minds" 
    text_icon = font.render("Challenges  V", True, BLACK) 
    text1_icon = font.render("Log out", True, BLACK)

      # Position of text  
    screen.blit(text_icon, (300, 240))
    screen.blit(text1_icon, (340,380))

    if show_dropdown:
        pygame.draw.rect(screen, WHITE, (290, 270, 210, 50))
        pygame.draw.rect(screen, BLACK, (290, 270, 210, 50), 2)
        maze_text = small_font.render("MAZE GAME", True, BLACK)
        screen.blit(maze_text, (310, 290)) 

        pygame.draw.rect(screen, WHITE, (290, 320, 210, 40))
        pygame.draw.rect(screen, BLACK, (290, 320, 210, 40), 2)
        quiz_text = small_font.render("QUIZ GAME", True, BLACK)
        screen.blit(quiz_text, (310, 330))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if pygame.Rect(290, 230, 210, 50).collidepoint(mouse_pos):
                show_dropdown = not show_dropdown
            elif show_dropdown and pygame.Rect(290, 270, 210, 40).collidepoint(mouse_pos):
                pygame.quit()
                os.system('python main.py')
                exit()
            elif show_dropdown and pygame.Rect(290, 320, 210, 40).collidepoint(mouse_pos):
                pygame.quit()
                os.system('python Quiztest.py')
                exit()
            elif pygame.Rect(290, 370, 210, 50).collidepoint(mouse_pos) and not show_dropdown:
                pygame.quit()
                os.system('python Welcomepage.py')
                exit()




# Update the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()