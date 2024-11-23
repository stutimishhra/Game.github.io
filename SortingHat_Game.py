import tkinter as tk
from tkinter import messagebox

class HogwartsSortingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hogwarts Sorting Hat Quiz!")
        self.root.config(bg="#6a4e23")
        # Initialize house scores
        self.house_scores = {'Gryffindor': 0,'Slytherin': 0,'Ravenclaw': 0,'Hufflepuff': 0}
        
        self.questions = [
            {
                "question": "You find a wallet on the street. What do you do?",
                "answers": {
                    "A": ("Keep it and buy something nice for yourself.", "Slytherin"),
                    "B": ("Return it to the lost and found.", "Hufflepuff"),
                    "C": ("Take it to the police station.", "Ravenclaw"),
                    "D": ("Look for the owner and give it back directly.", "Gryffindor")
                }
            },
            {
                "question": "If you were in a difficult situation, what would you do?",
                "answers": {
                    "A": ("Think of a clever plan to get out of it.", "Ravenclaw"),
                    "B": ("Fight through it with all your might.", "Gryffindor"),
                    "C": ("Look for a way to manipulate the situation for personal gain.", "Slytherin"),
                    "D": ("Stay calm, and do your best to help everyone.", "Hufflepuff")
                }
            },
            {
                "question": "Which of these qualities do you value most?",
                "answers": {
                    "A": ("Courage and bravery.", "Gryffindor"),
                    "B": ("Cunning and resourcefulness.", "Slytherin"),
                    "C": ("Intelligence and wisdom.", "Ravenclaw"),
                    "D": ("Loyalty and fairness.", "Hufflepuff")
                }
            },
            {
                "question": "What is your idea of fun?",
                "answers": {
                    "A": ("A daring adventure and a chance to prove yourself.", "Gryffindor"),
                    "B": ("Planning a successful scheme and winning over others.", "Slytherin"),
                    "C": ("Solving puzzles, reading, or learning new things.", "Ravenclaw"),
                    "D": ("Spending time with friends, working together on a project.", "Hufflepuff")
                }
            },
            {
                "question": "How do you make decisions?",
                "answers": {
                    "A": ("By trusting your instincts and acting quickly.", "Gryffindor"),
                    "B": ("By calculating every option and choosing the smartest move.", "Ravenclaw"),
                    "C": ("By considering what's best for yourself and your future.", "Slytherin"),
                    "D": ("By thinking of how it will affect everyone and trying to do the right thing.", "Hufflepuff")
                }
            },
            {
                "question": "What is your greatest fear?",
                "answers": {
                    "A": ("Not living up to my potential.", "Ravenclaw"),
                    "B": ("Not being brave enough when needed.", "Gryffindor"),
                    "C": ("Not getting ahead in life and falling behind.", "Slytherin"),
                    "D": ("Letting down those who rely on me.", "Hufflepuff")
                }
            }
        ]
        
        self.current_question = 0
        self.score = { 'Gryffindor': 0, 'Slytherin': 0, 'Ravenclaw': 0, 'Hufflepuff': 0 }
        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question]
        question_text = question_data["question"]
        answers = question_data["answers"]
        
        # Clear the window for the new question
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display the question
        question_label = tk.Label(self.root, text=question_text, font=("Tempus Sans ITC", 16), wraplength=400)
        question_label.pack(pady=20)

        # Display answer buttons
        for option, (answer, house) in answers.items():
            button = tk.Button(self.root, text=f"{option}: {answer}", font=("Poor Richard", 12), width=50, 
                               command=lambda house=house: self.handle_answer(house))
            button.pack(pady=5)

    def handle_answer(self, house):
        # Increment the score for the chosen house
        self.score[house] += 1
        
        # Move to the next question or display results
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_results()

    def show_results(self):
        # Determine the highest score
        sorted_houses = sorted(self.score.items(), key=lambda x: x[1], reverse=True)
        top_house, score = sorted_houses[0]
        
        # Show the results in a message box
        house_descriptions = {
            "Gryffindor": "Bravery, courage, and daring characterize Gryffindors.",
            "Slytherin": "Ambition, cunning, and resourcefulness define Slytherins.",
            "Ravenclaw": "Wisdom, creativity, and intelligence define Ravenclaws.",
            "Hufflepuff": "Hard work, loyalty, and patience are the core traits of Hufflepuffs."
        }
        
        result_text = f"\nYou belong to the House of {top_house}!\n\n{house_descriptions[top_house]}"
        
        # Replace the messagebox with a custom window for better font control
        result_window = tk.Toplevel(self.root)
        result_window.title("Your Hogwarts House")
        result_label = tk.Label(result_window, text=result_text, font=("Tempus Sans ITC", 16), wraplength=400, padx=20, pady=20)
        result_label.pack()

        # Button to close the result window
        close_button = tk.Button(result_window, text="Close", font=("Tempus Sans ITC", 14), command=result_window.destroy)
        close_button.pack(pady=10)
        
        messagebox.showinfo("Your Hogwarts House", result_text)
        
        # Reset game and close
        self.root.quit()

if __name__ == "__main__":
    # Create the Tkinter window
    root = tk.Tk()
    game = HogwartsSortingGame(root)
    root.mainloop()
