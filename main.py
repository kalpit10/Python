def KBC(question, answer, amount):
  print(question)
  user_answer = input("Enter your answer: ")
  if user_answer == answer:
      print("Correct answer!")
      amount += 1000
      print("You won", amount)
      return True, amount
  else:
      print("Wrong answer!")
      return False, amount

# List of question-answer pairs
questions = [
  {"question": "What is the capital of INDIA?", "answer": "New Delhi"},
  {"question": "How many states are there in INDIA?", "answer": "28"},
  {"question": "Who is the prime minister of INDIA?", "answer": "Narendra Modi"}
]

# Initial amount
amount = 0

# Iterate over each question-answer pair
for qa in questions:
  #correct is a boolean
  correct, amount = KBC(qa["question"], qa["answer"], amount)
  if not correct:
      break

print("Game over! Your total winnings are:", amount)