from agents.faq_agent import FAQAgent


def main():

    agent = FAQAgent()

    print("=" * 60)
    print("Conference FAQ Assistant")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        question = input("\nAsk your question: ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        answer = agent.answer_question(question)

        print("\nAnswer:\n")
        print(answer)
        print("-" * 60)


if __name__ == "__main__":
    main()