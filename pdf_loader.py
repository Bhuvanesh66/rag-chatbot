from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    # ✅ ensure page metadata exists
    for i, chunk in enumerate(chunks):
        if "page" not in chunk.metadata:
            chunk.metadata["page"] = chunk.metadata.get("page_number", "Unknown")

    return chunks