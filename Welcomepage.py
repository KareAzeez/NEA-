import pygame
import os  # For handling file paths

# Define colors
GREY = (217, 217, 217)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set the width and height of the window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Home Page")

# Initialize clock
clock = pygame.time.Clock()

# you ensure the image is in the same directory as the script
image_path = os.path.join("BS_image.png")  # Image name is BS_image.png
try:
    image = pygame.image.load(image_path)  # Load the image
    image = pygame.transform.scale(image, (400, 200))  # Resize the image to fit the space
except pygame.error as e:
    print(f"Error loading image: {e}")
    image = None  # Set image to None if loading fails

# Function to draw a button with text
def draw_button(screen, x, y, width, height, text, font, border_radius=0):
    # Draw button background
    pygame.draw.rect(screen, WHITE, [x, y, width, height], border_radius=border_radius)
    # Draw button border
    pygame.draw.rect(screen, WHITE, [x, y, width, height], 2, border_radius=border_radius)
    # Render text
    text_surface = font.render(text, True, BLACK)
    # Center text on the button
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(630, 30, 150, 40).collidepoint(event.pos):
                pygame.quit()
                os.system("python signin.py")
                exit()


    # Fill background inside the loop
    screen.fill(GREY)

    # Draw buttons for the home screen icons
    font = pygame.font.Font(None, 30)
    draw_button(screen, 630, 30, 150, 40, "Sign in", font,  border_radius = 10)

    # Draw a long black line underneath the buttons
    pygame.draw.line(screen, BLACK, (5, 100), (800, 100), 2)

    # Render and display the main text
    font = pygame.font.Font(None, 36)
    text_lines = [
        "Welcome!!",
        "To Business Minds, a fun and",
        "interactive study gaming app",
        "designed to guide and support",
        "in learning business studies",
        "concepts through fun and",
        "interactive games."
    ]
    for i, line in enumerate(text_lines):
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (10, 200 + i * 30))

        # display text on the screen 
        text = font.render("Business Minds", True, BLACK) 
    screen.blit(text, (300, 110))

    if image:
        screen.blit(image, (450, 190))  # Position the image at (450, 150)
    else:
        # Display an error message if the image fails to load
        error_font = pygame.font.Font(None, 24)
        error_text = error_font.render("Image not found!", True, BLACK)
        screen.blit(error_text, (450, 190))


    # Update the screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()