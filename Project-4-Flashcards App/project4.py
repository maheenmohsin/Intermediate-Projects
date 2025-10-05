import json
import random
import os

FILE_NAME = "flashcards.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)


def load_flashcards():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_flashcards(flashcards):
    with open(FILE_NAME, "w") as file:
        json.dump(flashcards, file, indent=4)


def add_flashcard():
    question = input("\nEnter the question: ").strip()
    answer = input("Enter the answer: ").strip()

    flashcards = load_flashcards()
    flashcards.append({"question": question, "answer": answer})
    save_flashcards(flashcards)
    print("Flashcard added successfully!\n")


def view_flashcards():
    flashcards = load_flashcards()
    if not flashcards:
        print("No flashcards found!\n")
        return

    print("\n=== All Flashcards ===")
    for i, card in enumerate(flashcards, start=1):
        print(f"{i}. Q: {card['question']} | A: {card['answer']}")
    print()


def quiz_mode():
    flashcards = load_flashcards()
    if not flashcards:
        print("No flashcards available for quiz!\n")
        return

    card = random.choice(flashcards)
    print(f"\nQuestion: {card['question']}")
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == card["answer"].lower():
        print("Correct! Great job!\n")
    else:
        print(f"Wrong! The correct answer is: {card['answer']}\n")


def main():
    print("=== Flashcard App ===")

    while True:
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Quiz Mode")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            add_flashcard()
        elif choice == "2":
            view_flashcards()
        elif choice == "3":
            quiz_mode()
        elif choice == "4":
            print("Exiting Flashcard App. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
