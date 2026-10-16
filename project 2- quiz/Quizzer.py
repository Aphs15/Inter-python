import random
import json
import os

class Question:
    def __init__(self, text, choices, correct_index):
        self.text = text
        self.choices = choices        #list of 4 strings
        self.correct_index = correct_index

    def check(self, answer_index):
        return answer_index == self.correct_index

    def display(self):
        print(f"\n{self.text}")
        for i, choice in enumerate(self.choices, start=1):
            print(f" {i}. {choice}")

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.display()
            try:
                answer = int(input("Your answer (1-4): ")) - 1
            except ValueError:
                print("Skipping - invalid input.")
                continue

            if question.check(answer):
                print("correct!")
                self.score += 1
            else:
                correct = question.choices[question.correct_index]
                print(f"Wrong. Correct answer: {correct}")

        self.show_result()

    def show_result(self):
        total = len(self.questions)
        pct = (self.score / total) * 100
        print(f"\nFinal Score: {self.score}/{total} ({pct:.1f}%)")

def load_questions(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, filename)
    with open(path, "r") as f:
        data = json.load(f)
    return [Question(q["text"], q["choices"], q["correct"]) for q in data]

if __name__ == "__main__":
    questions = load_questions("questions.json")
    quiz = Quiz(questions)
    quiz.run()

