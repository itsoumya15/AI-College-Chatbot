import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

# ✅ correct path (because we are inside backend/)
df = pd.read_csv("../data/college-admission-dataset.csv")

df = df.fillna("Not Available")

docs = []

for _, row in df.iterrows():
    text = " | ".join(
        f"{col}: {str(row[col]).strip()}"
        for col in df.columns
    )
    docs.append(Document(page_content=text))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_documents(docs, embeddings)

db.save_local("vectorstore")

print("✅ Vector DB created successfully!")