from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path='books',          # Folder where all your PDFs are stored
    glob='**/*.pdf',       # Recursively search for all PDF files
    loader_cls=PyPDFLoader # Use PyPDFLoader for each PDF
)

docs = loader.load()

print(docs)                    # Will print the list of Document objects
print(len(docs))               # Total number of Document objects (pages, not files)
print(docs[0].page_content)    # Text content of the first page
print(docs[0].metadata)        # Metadata such as source file and page number
