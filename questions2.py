import csv

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

def main():
    questions = load_questions("Quiz.csv")
    print(questions)

if __name__ =="__main__":
    main()
