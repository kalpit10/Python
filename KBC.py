def KBC(questions):
    amount = 0
    for qa in questions:
        print(qa["question"])
        user_answer = input("Enter your answer: ")
        if user_answer == qa["answer"]:
            print("Correct answer!")
            amount += 1000
            print("You won", amount)
        else:
            print("Wrong answer!")
            break
    print("Game over! Your total winnings are:", amount)


# List of question-answer pairs
questions = [{
    "question": "What is the capital of INDIA?",
    "answer": "New Delhi"
}, {
    "question": "How many states are there in INDIA?",
    "answer": "28"
}, {
    "question": "Who is the prime minister of INDIA?",
    "answer": "Narendra Modi"
}]

# Run the game
KBC(questions)
