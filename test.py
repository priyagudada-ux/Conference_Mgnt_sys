from rag.retriever import ConferenceRetriever


def main():

    retriever = ConferenceRetriever()

    print("=" * 60)
    print("Conference Retriever Test")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        query = input("\nEnter your question: ")

        if query.lower() == "exit":
            print("\nExiting...")
            break

        results = retriever.retrieve(query)

        print("\nRetrieved Documents:\n")

        if not results:
            print("No relevant documents found.")
            continue

        for i, doc in enumerate(results, start=1):

            print("=" * 70)
            print(f"Document {i}")
            print("=" * 70)
            print(f"Source : {doc.metadata.get('source', 'Unknown')}")
            print()
            print(doc.page_content[:800])
            print()


if __name__ == "__main__":
    main()