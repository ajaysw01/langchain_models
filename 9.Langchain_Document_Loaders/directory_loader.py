from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path='books',          # Folder where all your PDFs are stored
    glob='**/*.pdf',       # Recursively search for all PDF files
    loader_cls=PyPDFLoader # Use PyPDFLoader for each PDF
)

# docs = loader.load()
docs = loader.lazy_load()


for document in docs :
    print(document.metadata)

print(docs)                    # Will print the list of Document objects
print(len(docs))               # Total number of Document objects (pages, not files)
print(docs[0].page_content)    # Text content of the first page
print(docs[0].metadata)        # Metadata such as source file and page number


# It takes time to load all documents, especially if there are many PDFs or large files.
# we are laoding this files in memroy. better to use lazy_load()