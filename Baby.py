from random import choice
questions = ["Why you like Sukan","Why you like Kasi","Why you like Shiv"]
question = choice(questions)
answer = input(question).strip().lower()
while answer != "just because":
    answer = input("why?").strip().lower()
print("Okay...")
