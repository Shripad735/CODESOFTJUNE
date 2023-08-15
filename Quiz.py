import random

class Question:
    def __init__(self, question, choices, correct_choice):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, choices, correct_choice):
        self.questions.append(Question(question, choices, correct_choice))

    def play(self):
        print("Welcome to the Quiz Game!")
        print("Rules: Answer multiple-choice questions. Enter the letter corresponding to your choice.")
        
        play_again = "yes"
        while play_again.lower() == "yes":
            self.score = 0
            random.shuffle(self.questions)
            
            for question_obj in self.questions:
                print("\n" + question_obj.question)
                for i, choice in enumerate(question_obj.choices, start=1):
                    print(f"{chr(65 + i - 1)}. {choice}")
                
                user_choice = input("Your answer: ").upper()
                correct_choice = question_obj.correct_choice
                
                if user_choice == correct_choice:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Incorrect. The correct answer is {correct_choice}.")
            
            print("\nQuiz completed!")
            print(f"Your score: {self.score}/{len(self.questions)}")
            
            play_again = input("Do you want to play again? (yes/no): ")

def main():
    quiz = Quiz()
    
    # Add your questions here
    quiz.add_question("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "A")
    quiz.add_question("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Venus", "Mercury"], "A")
    quiz.add_question("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], "C")
    quiz.add_question("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "C")
    quiz.add_question("Which planet is known as the 'Morning Star' or 'Evening Star'?", ["Mars", "Venus", "Jupiter", "Saturn"], "B")
    quiz.add_question("Which famous scientist developed the theory of general relativity?", ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Niels Bohr"], "B")
    quiz.add_question("Which river is the longest in the world?", ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "B")
    quiz.add_question("Which country is known as the 'Land of the Rising Sun'?", ["Japan", "China", "South Korea", "Thailand"], "A")
    quiz.add_question("What is the largest mammal in the world?", ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "B")
    quiz.add_question("Who wrote the play 'Romeo and Juliet'?", ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "A")

    # Add more questions
    
    quiz.play()

if __name__ == "__main__":
    main()
