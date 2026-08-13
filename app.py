import argparse
from agents.coordinator_agent import CoordinatorAgent
import argparse


def main():
    coordinator = CoordinatorAgent()
    while True:
        print("\n" + "=" * 60)
        print("      AI CONFERENCE MANAGEMENT AGENT")
        print("=" * 60)
        print("1. Analyze Research Paper")
        print("2. Conference FAQ")
        print("3. Generate Acceptance Email")
        print("4. Exit")
        print("=" * 60)
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            pdf_path = input("\nEnter PDF path: ")
            result = coordinator.process(
                "Analyze my paper",
                pdf_path
            )
            print("\n========== ANALYSIS ==========\n")
            print(result)
        elif choice == "2":
            question = input("\nAsk your conference question: ")
            result = coordinator.process(question)
            print("\n========== ANSWER ==========\n")
            print(result)
        elif choice == "3":
            paper_title = input("\nEnter paper title: ")
            email_type = input("\nEnter email type (Acceptance/Rejection): ")
            result = coordinator.process(
                user_request="Generate email",
                paper_title=paper_title,
                email_type=email_type
            )
            print("\n========== GENERATED EMAIL ==========\n")
            print(result)
        elif choice == "4":
            print("\nThank you for using Conference Management Agent.")
            break
        else:
            print("\nInvalid Choice. Please try again.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conference Management Agent")
    parser.add_argument("--ui", action="store_true", help="Run the Flask web UI")
    args = parser.parse_args()
    if args.ui:
        from ui.server import run_app
        run_app()
    else:
        main()