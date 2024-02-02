import random
import time

class QuizGame:
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                "question": "What is the correct way to create a function in Python?",
                "options": ["function myFunction():", "def myFunction():", "create myFunction():", "func myFunction():"],
                "answer": 1
            },
            {
                "question": "Which of these is NOT a Python data type?",
                "options": ["list", "dictionary", "tuple", "array"],
                "answer": 3
            },
            {
                "question": "What is the output of print(2 ** 3)?",
                "options": ["6", "8", "5", "9"],
                "answer": 1
            },
            {
                "question": "Which method is used to add an element to a list?",
                "options": [".add()", ".append()", ".insert()", ".extend()"],
                "answer": 1
            },
            {
                "question": "What does the 'len()' function do?",
                "options": ["Returns the length of an object", "Rounds a number down", "Converts to lowercase", "Creates a new list"],
                "answer": 0
            },
            {
                "question": "How do you start a comment in Python?",
                "options": ["//", "/* */", "#", "<!-- -->"],
                "answer": 2
            },
            {
                "question": "What is the correct way to create a variable in Python?",
                "options": ["var x = 5", "x = 5", "int x = 5", "let x = 5"],
                "answer": 1
            },
            {
                "question": "Which of these is a valid way to create a tuple in Python?",
                "options": ["(1, 2, 3)", "{1, 2, 3}", "[1, 2, 3]", "<1, 2, 3>"],
                "answer": 0
            },
            {
                "question": "What does the 'import' keyword do?",
                "options": ["Exports a module", "Creates a new module", "Deletes a module", "Imports a module"],
                "answer": 3
            },
            {
                "question": "Which of these is NOT a valid loop in Python?",
                "options": ["for loop", "while loop", "do-while loop", "nested loop"],
                "answer": 2
            }
        ]
    
    def display_welcome(self):
        print("\n" + "=" * 50)
        print("🐍 WELCOME TO THE PYTHON QUIZ GAME! 🐍")
        print("=" * 50)
        print("Test your Python knowledge with these 5 questions!")
        print("=" * 50)
    
    def display_question(self, question_data):
        print("\n" + "-" * 50)
        print(f"Question: {question_data['question']}")
        print("-" * 50)
        
        for i, option in enumerate(question_data['options']):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                choice = int(input("\nEnter your answer (1-4): "))
                if 1 <= choice <= 4:
                    return choice - 1  # Adjust to 0-based indexing
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def run_quiz(self):
        self.display_welcome()
        
        # Shuffle questions and select 5
        quiz_questions = random.sample(self.questions, 5)
        
        for i, question_data in enumerate(quiz_questions):
            print(f"\nQuestion {i+1} of 5:")
            user_answer = self.display_question(question_data)
            correct_answer = question_data['answer']
            
            if user_answer == correct_answer:
                print("\n✅ Correct! Well done!")
                self.score += 1
            else:
                correct_option = question_data['options'][correct_answer]
                print(f"\n❌ Wrong! The correct answer is: {correct_option}")
            
            # Small pause between questions
            time.sleep(1)
        
        self.display_results()
    
    def display_results(self):
        print("\n" + "=" * 50)
        print("🏆 QUIZ COMPLETED! 🏆")
        print("=" * 50)
        print(f"Your final score: {self.score}/5")
        
        if self.score == 5:
            print("🌟 Perfect score! You're a Python expert! 🌟")
        elif self.score >= 3:
            print("👍 Great job! You know your Python well!")
        else:
            print("📚 Keep practicing! You'll get better at Python!")
        
        print("=" * 50)
    
    def play_again(self):
        while True:
            choice = input("\nDo you want to play again? (yes/no): ").lower()
            if choice in ['yes', 'y']:
                self.score = 0
                return True
            elif choice in ['no', 'n']:
                print("\nThank you for playing! Goodbye! 👋")
                return False
            else:
                print("Please enter 'yes' or 'no'.")


def main():
    quiz = QuizGame()
    playing = True
    
    while playing:
        quiz.run_quiz()
        playing = quiz.play_again()


if __name__ == "__main__":
    main()