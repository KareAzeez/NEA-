# questions.py
import csv
from settings import WHITE, QUESTION_AREA_Y

def load_questions(file_path):
    questions = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            question_data = {
                'question': row['Question'],
                'optionA': row['OptionA'],
                'optionB': row['OptionB'],
                'optionC': row['OptionC'],
                'optionD': row['OptionD'],
                'correct_option': row['CorrectOption']
            }
            questions.append(question_data)
    return questions

def display_question_and_options(screen, font, question_data):
    # Render question and options texts
    question_text = font.render(question_data['question'], True, WHITE)
    optionA_text = font.render(question_data['optionA'], True, WHITE)
    optionB_text = font.render(question_data['optionB'], True, WHITE)
    optionC_text = font.render(question_data['optionC'], True, WHITE)
    optionD_text = font.render(question_data['optionD'], True, WHITE)

    # Display the question and options in the dedicated area
    screen.blit(question_text, (60, QUESTION_AREA_Y))
    screen.blit(optionA_text, (100, QUESTION_AREA_Y + 50))
    screen.blit(optionB_text, (450, QUESTION_AREA_Y + 50))
    screen.blit(optionC_text, (100, QUESTION_AREA_Y + 100))
    screen.blit(optionD_text, (450, QUESTION_AREA_Y + 100))