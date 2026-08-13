from agents.conference_agent import ConferenceAgent
from rag.document_loader import ConferenceDocumentLoader
from rag.chunking import TextChunker
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import ConferenceRetriever
from agents.faq_agent import FAQAgent


def separator(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def main():

    # -------------------------------------------------------------
    separator("STEP 1 : Conference Data Collection")

    try:
        agent = ConferenceAgent()
        agent.load_conference()
    except Exception as e:
        print("Conference download skipped:", e)

    print("Conference Agent Executed")

    # -------------------------------------------------------------
    separator("STEP 2 : Document Loading")

    loader = ConferenceDocumentLoader()

    documents = loader.load_documents()

    print(f"Documents Loaded : {len(documents)}")

    # -------------------------------------------------------------
    separator("STEP 3 : Chunking")

    chunker = TextChunker()

    chunks = chunker.create_chunks(documents)

    print(f"Chunks Created : {len(chunks)}")

    # -------------------------------------------------------------
    separator("STEP 4 : Embedding Model")

    embedding = EmbeddingModel().get_embeddings()

    print("Embedding Model Loaded Successfully")

    # -------------------------------------------------------------
    separator("STEP 5 : Vector Database")

    vector_db = VectorStore(embedding)

    vector_db.create_vector_db(chunks)

    # -------------------------------------------------------------
    separator("STEP 6 : Retriever")

    retriever = ConferenceRetriever()

    query = "What is the email address of the congress secretariat?"

    docs = retriever.retrieve(query)

    print(f"\nRetrieved {len(docs)} document(s)\n")

    for i, doc in enumerate(docs):

        print(f"Document {i+1}")
        print("-" * 60)
        print(doc.page_content[:400])
        print()

    # -------------------------------------------------------------
    separator("STEP 7 : FAQ Agent")

    faq = FAQAgent()

    questions = [

        "What is IEEE WCCI 2026?",

        "Who organizes IEEE WCCI 2026?",

        "What is the email address of the congress secretariat?",

        "Does the conference have tutorials?",

        "Does the conference have workshops?",

        "Does the conference have competitions?"

    ]

    for question in questions:

        print("\nQuestion:")
        print(question)

        print("\nAnswer:")

        answer = faq.answer_question(question)

        print(answer)

        print("-" * 80)


if __name__ == "__main__":
    main()