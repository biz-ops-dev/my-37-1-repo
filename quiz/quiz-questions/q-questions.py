
# take-aways
## make not case sensitive
# enumerate
# random.sample(), random.shuffle()
# zip, 

git_questions = [ # These have been moved to yml file
    ('Commit the current directiory with notes "notes"', 'git commit -m "notes"'),
    ('Find the hash for a commit"', 'git log'),
    ('Create a branch called "new-feature"', 'git branch new-feature'),
    ('switch to a branch called "other-branch"', 'git checkout other-branch'),
    ('delete a branch called "old-branch', 'git branch -d old-branch'),
    ('obtain the status of the current repository', 'git status'),
    ('add a file called "new.py" to the index', 'git add new.py'),
    ('add all files in current directory to the index', 'git add --all')
    ('create a new git repository in the current directory', 'git init'),
    # Note git init basic_scripts_repo created a new directory with git in that diectory not parent folder
    #More git init : https://git-scm.com/docs/git-init
]

math_questions = [
    ('0 is a natural numner', 'False'),
    ('0 is a whole numner', 'True'),
    ('All whole numbers are integers', 'True'),
    ('All integers numbers whole numbers', 'False'),
]

python_functions = [
    ('return a list of seasons "seasons" as a numbered list of tuples starting at 1', 'list(enumerate(seasons, 1))')
]

keyboard_shortcuts = [
    ('Preview a file(s) from finder', 'space'),
    ('Open app settings: ⌘', ','),
    ('Switch to another window, same app: ⌘', '~')
]

list(enumerate(git_questions, 1))
for question, correct_answer in git_questions:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")


NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "What's the official name of the := operator": [
        "Assignment expression",
        "Named expression",
        "Walrus operator",
        "Colon equals operator",
    ],
    "What's one effect of calling random.seed(42)": [
        "The random numbers are reproducible.",
        "The random numbers are more random.",
        "The computer clock is reset.",
        "The first random number is always 42.",
    ]
}

'''
num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)
print('The Questions:', sep='\n')
print(*questions, sep='\n')



num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")
'''
