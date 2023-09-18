from string import ascii_lowercase
import random
import pathlib #<--You’re using pathlib to handle the path to questions.toml. Instead of hard-coding the path to questions.toml you rely on the special __file__ variable. In practice, you’re stating that it’s located in the same directory as your quiz.py file.
try:
    import tomllib
except ModuleNotFoundError: #<-- like it error exception
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "quiz questions/new-questions.toml"

def run_quiz():

    #Preprocess: prepare question data structure, limit number of questions, ensure listed in random order
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ)

    #Process (main loop)
    num_correct = 0
    for num, question in enumerate(questions, start=1):#<--enumerate() to keep a counter that numbers the questions you ask
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)
    
    #Postprocess
    print(f"\nYou got {num_correct} correct out of {num} questions")

def prepare_questions(path, num_questions):
    questions = tomllib.loads(path.read_text())['questions']
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

def ask_question(question):
    correct_answer = question['answer']
    possible_answers = [question['answer']] + question['alternatives']

    ordered_alternatives = random.sample(possible_answers, k=len(possible_answers))

    answer = get_answer(question['question'], ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

def get_answer(question, possible_answers):

    '''
    This function accepts a question text and a list of alternatives.
    You then use the same techniques as earlier to label the alternatives and
    ask the user to enter a valid label. 
    '''
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, possible_answers))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

if __name__ == "__main__": #<--special incantation
    run_quiz()

