import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="db_quiz"
)

# Create cursor
mycursor = mydb.cursor()

# Create Tkinter window
root = tk.Tk()
root.title("Quiz")

# Add widgets
question_label = tk.Label(root, text="Question:")
question_label.pack()

question_text = tk.Label(root, text="")
question_text.pack()

option_a = tk.Button(root, text="")
option_a.pack()

option_b = tk.Button(root, text="")
option_b.pack()

option_c = tk.Button(root, text="")
option_c.pack()

option_d = tk.Button(root, text="")
option_d.pack()

submit_button = tk.Button(root, text="Submit")
submit_button.pack()

# Function to load question from database
def load_question():
    # Get random question
    mycursor.execute("SELECT * FROM create_quiz_tb ORDER BY RAND() LIMIT 1")
    question = mycursor.fetchone()

    # Set question text
    question_text.config(text=question[1])

    # Set option buttons
    option_a.config(text=question[2], command=lambda: check_answer(question[0], "A"))
    option_b.config(text=question[3], command=lambda: check_answer(question[0], "B"))
    option_c.config(text=question[4], command=lambda: check_answer(question[0], "C"))
    option_d.config(text=question[5], command=lambda: check_answer(question[0], "D"))

# Function to check answer
def check_answer(question_id, selected_option):
    # Get correct answer
    mycursor.execute("SELECT Answer FROM create_quiz_tb WHERE id=%s", (question_id,))
    correct_answer = mycursor.fetchone()[0]

    # Check if answer is correct
    if selected_option == correct_answer:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showerror("Result", "Incorrect!")

    # Load next question
    load_question()

# Load first question
load_question()

# Run Tkinter main loop
root.mainloop()
