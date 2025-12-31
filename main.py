# main.py
import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMG, MUSIC_FILE, OPTION_BOXES, QUESTION_DELAY, BLACK, WHITE
from player import Player
from questions import load_questions, display_question_and_options
from maze import create_maze

# Creates score screen 
def show_score_screen (screen, font, score, total):
    screen.fill(BLACK)
    score_text = font.render(f"Final Score: {score} / {total}", True, WHITE)
    instructions_text = font.render("Press any key to exit", True, WHITE)
    screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_width()) // 2, SCREEN_HEIGHT //2 - 50))
    screen.blit(instructions_text, ((SCREEN_WIDTH - instructions_text.get_width()) // 2, SCREEN_HEIGHT //2 + 10))
    pygame.display.flip()

    waiting = True 
    while waiting :
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False

def main():
    # Initialize Pygame and create window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Game with Questions")

    # Load and scale background
    background = pygame.image.load(BACKGROUND_IMG)
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize music
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_FILE)
    pygame.mixer.music.play(-1)

    # Generate a random color for the maze walls
    wall_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    wall_list, all_sprite_list = create_maze(wall_color)

    # Load questions from CSV and choose one at random
    questions = load_questions("questions.csv")
    total_questions = len(questions) # Change from random question to length of questions 
    current_question_index = 0
    current_question = questions[current_question_index]
    correct_answer_index = ord(current_question['correct_option'].strip()) - ord('A')

    # Score counter 
    score = 0

    # Create the player and add to the sprite group
    player = Player(50, 50, wall_list)
    all_sprite_list.add(player)

    # Set up fonts and clock
    font = pygame.font.SysFont('Calibri', 25, True, False)
    clock = pygame.time.Clock()

    # Game state variables
    done = False
    selected_option_index = None
    feedback_message = ""
    show_feedback = False
    feedback_start_time = 0

    while not done:
        current_time = pygame.time.get_ticks()

        # Event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)

        # Update sprites
        all_sprite_list.update()

        # Check if player is on an option box and ENTER is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and selected_option_index is None and not show_feedback:
            for idx, option in enumerate(OPTION_BOXES):
                if option.collidepoint(player.rect.center):
                    selected_option_index = idx  # Record the selected option

                    if selected_option_index == correct_answer_index:
                        feedback_message = "CORRECT KEEP IT UP!"
                        score += 1 # Increase score by 1 
                    else:
                        correct_option = current_question[f'option{chr(ord("A") + correct_answer_index)}']
                        feedback_message = f"Incorrect! The correct answer is {correct_option}"
                    show_feedback = True
                    feedback_start_time = pygame.time.get_ticks()


        # After delay, reset for a new question
        if show_feedback and (current_time - feedback_start_time > QUESTION_DELAY):
            show_feedback = False
            selected_option_index = None
            feedback_message = ""
            current_question_index += 1 # This helps the program to move to the next question

            if current_question_index >= total_questions:
                done = True 
            else:
                current_question = questions[current_question_index]
                correct_answer_index = ord(current_question['correct_option'].strip()) - ord('A')

                wall_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                wall_list, all_sprite_list = create_maze(wall_color)
                
                player = Player(50, 50, wall_list)
                all_sprite_list.add(player)

                
        # Draw background and sprites
        screen.blit(background, (0, 0))
        all_sprite_list.draw(screen)

        # Draw option boxes with feedback color if selected
        for idx, option in enumerate(OPTION_BOXES):
            if selected_option_index is not None:
                if idx == selected_option_index:
                    color = (0, 128, 0) if idx == correct_answer_index else (255, 0, 0)
                else:
                    color = WHITE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, option)

        # Draw letters on the option boxes
        screen.blit(font.render("A", True, BLACK), (OPTION_BOXES[0].x + 5, OPTION_BOXES[0].y + 3))
        screen.blit(font.render("B", True, BLACK), (OPTION_BOXES[1].x + 5, OPTION_BOXES[1].y + 3))
        screen.blit(font.render("C", True, BLACK), (OPTION_BOXES[2].x + 5, OPTION_BOXES[2].y + 3))
        screen.blit(font.render("D", True, BLACK), (OPTION_BOXES[3].x + 5, OPTION_BOXES[3].y + 3))

        # Display question and answer options text
        display_question_and_options(screen, font, current_question)

        # Display feedback message 
        if feedback_message:
            feedback_text = font.render(feedback_message, True, WHITE)
            screen.blit(feedback_text, (380, 120))

        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.stop()
    show_score_screen(screen, font, score, total_questions)
    pygame.quit()

if __name__ == '__main__':
    main()