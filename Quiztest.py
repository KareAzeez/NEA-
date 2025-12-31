import pygame
import csv
import random

# Colors
BLACK = (0, 0, 0)
GREY = (217, 217, 217)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (178, 132, 190)


# Initialize pygame 
pygame.init()

size = (700, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Quiz Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
big_font = pygame.font.Font(None, 40)

# Load CSV questions
def load_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            question_data = {
                'question': row['Question'],
                'A': row['OptionA'],
                'B': row['OptionB'],
                'C': row['OptionC'],
                'D': row['OptionD'],
                'correct': row['CorrectOption'].strip().upper()
            }
            questions.append(question_data)
            
        return questions

questions = load_questions("Quiz.csv")
random.shuffle(questions)  # Shuffle to avoid order repetition
question_index = 0
score = 0
current_index = 0
selected_option = None
show_score = False
review_mode = False
wrong_answers = []

# Game loop
running = True
while running:
    screen.fill(PURPLE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if not show_score and not review_mode:
                
                for key, rect in option_rects.items():
                    if rect.collidepoint(mouse_pos):
                            selected_option = key
                if 600 <= mouse_pos[0] <= 690 and 20 <=mouse_pos[1] <= 60 and selected_option:
                    correct_option_key = questions[current_index]['correct']
                    correct_text = questions[current_index][correct_option_key]
                    if selected_option == correct_option_key:
                        score += 1 
                    else:
                        wrong_answers.append({
                            'question': questions[current_index]['question'],
                            'correct': correct_text
                        })
                    current_index += 1
                    selected_option = None
                    if current_index >= len(questions):
                        show_score = True
            elif show_score:
                if 570 <= mouse_pos[0] <= 680 and 540 <= mouse_pos[1] <= 580:
                    review_mode = True 
                    show_score = False
    
    if not show_score and not review_mode and current_index < len(questions):
        question_data = questions[current_index]
        
        pygame.draw.rect(screen, WHITE, [100, 170, 500, 100])
        pygame.draw.rect(screen, BLACK, [100, 170, 500, 100], 2)
        lines = []
        words = question_data['question'].split()
        line = ""
        for word in words:
            test_line = line + word + " "
            if font.size(test_line)[0] < 480:
                line = test_line
            else:
                lines.append(line)
                line = word + " "
        lines.append(line)
        y_offset = 190
        for line in lines:
            rendered_line = font.render(line, True, BLACK)
            screen.blit(rendered_line, (110, y_offset))
            y_offset += 25  


# Rectangles
        option_rects = {
        'A': pygame.Rect(40, 400, 260, 40),
        'B': pygame.Rect(380, 400, 280, 40),
        'C': pygame.Rect(40, 540, 260, 40),
        'D': pygame.Rect(380, 540, 280, 40)
    }
        
        for key,rect in option_rects.items():
            colour = YELLOW if selected_option == key else WHITE
            pygame.draw.rect(screen, colour , rect)
            pygame.draw.rect(screen, colour , rect, 2)
            txt = font.render(question_data[key], True, BLACK)
            txt_rect = txt.get_rect(center = rect.center)
            screen.blit(txt, txt_rect)

        # Draw Next button
        pygame.draw.rect(screen, WHITE,(600, 20, 90, 40))
        pygame.draw.rect(screen, BLACK, (600, 20, 90, 40), 2)
        txt = font.render("Next", True, BLACK)
        screen.blit(txt, (620, 30))

    elif show_score:
        pygame.draw.rect(screen, WHITE, [150, 180, 400, 200], border_radius=15) # Draws score box 
        pygame.draw.rect(screen, BLACK, [150, 180, 400, 200], 2, border_radius=15)
        result_text = big_font.render(f"Your Score: {score} / {len(questions)}", True, BLACK)
        screen.blit(result_text, result_text.get_rect(center=(350, 280)))

        # Draws review button
        pygame.draw.rect(screen,WHITE,[580,540,100,40], border_radius = 10)
        pygame.draw.rect(screen, BLACK,[580,540,100,40], 2, border_radius = 10)
        screen.blit(font.render("Review", True, BLACK), (590, 550))

    elif review_mode:
        y = 60
        for item in wrong_answers:
            pygame.draw.rect(screen,WHITE,[50, y,600,60])
            pygame.draw.rect(screen, BLACK,[50,y,600,60], 2)
            q_text = font.render(f"Q: {item['question']}", True, BLACK)
            screen.blit(q_text,(60,y + 5))
            pygame.draw.rect(screen, GREEN, (60, y+30, 580, 25))
            correct_text = font.render(f"Correct: {item['correct']}", True, BLACK)
            screen.blit(correct_text, (70, y+32))
            y += 90
            
            

    pygame.display.flip()
    clock.tick(60)

pygame.quit()