from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Feedback.pdf')
docs = loader.load()
print(docs)
print(len(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)