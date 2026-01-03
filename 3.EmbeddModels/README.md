# 🧩 LangChain Embedding Models

This folder contains **hands-on examples of text embeddings** using **LangChain** with multiple providers including  
**OpenAI, Google Gemini, and Hugging Face**, along with a practical **document similarity use case**.

The examples demonstrate how raw text is converted into **numerical vectors** and how those vectors are used in
real-world GenAI workflows like **semantic search, similarity matching, and retrieval systems**.

---

## 🚀 About Embeddings

**Embeddings** transform text into high-dimensional numerical vectors that capture semantic meaning.

They are the backbone of:
- 🔍 Semantic Search  
- 📄 Document Similarity  
- 🧠 Retrieval-Augmented Generation (RAG)  
- 🤖 Recommendation Systems  
- 📚 Knowledge Bases  

This folder focuses on **query embeddings**, **document embeddings**, and **similarity scoring**.

---

## 📂 Folder Structure

```bash
📁 EmbeddingModels
│
├── 1_embedding_openai_query.py      # OpenAI query embedding
├── 2_embedding_openai_docs.py       # OpenAI document embeddings
├── 3_embedding_gemini.py            # Google Gemini embeddings
├── 4_embedding_hf_query.py          # Hugging Face query embedding
├── 5_embedding_hf_docs.py           # Hugging Face document embeddings
├── 6_document_similarity.py         # Document similarity using cosine similarity
└── README.md
```

---

## 📄 File-wise Explanation
🔹 1_embedding_openai_query.py
- Uses OpenAIEmbeddings
- Generates embedding for a single query
- Uses text-embedding-3-large
- Demonstrates reduced embedding dimensions

Use case:
- Query encoding for semantic search
- RAG query vector creation

🔹 2_embedding_openai_docs.py
- Uses OpenAIEmbeddings
- Generates embeddings for multiple documents
- Demonstrates batch document embedding

Use case:
- Vector database ingestion
- Knowledge base indexing

🔹 3_embedding_gemini.py

- Uses GoogleGenerativeAIEmbeddings
- Integrates Google Gemini embedding model
- Converts text into dense semantic vectors

Use case:
- Google ecosystem-based GenAI pipelines
- Lightweight embedding generation

🔹 4_embedding_hf_query.py

- Uses HuggingFaceEmbeddings
- Model: sentence-transformers/all-MiniLM-L6-v2
- Generates embedding for a single query
- Fully open-source

Use case:
- Cost-free embedding experiments
- Offline / open-source workflows

🔹 5_embedding_hf_docs.py

- Uses HuggingFaceEmbeddings
- Generates embeddings for multiple documents
- Uses sentence-transformers

Use case:
- Local semantic search
- Vector store preparation without APIs

🔹 6_document_similarity.py

- Uses Hugging Face embeddings
- Computes cosine similarity
- Finds the most relevant document for a query
- Uses real-world text examples

Use case:
- Document matching
- FAQ retrieval
- Resume / profile similarity
- Search ranking logic

---

## 🧠 Key Concepts Covered
- Query vs Document embeddings
- Vector representations of text
- Cosine similarity scoring
- API-based vs Local embeddings
- Provider comparison (OpenAI vs Gemini vs Hugging Face)
- Core foundation for RAG systems

---

## 🧠 When to Use Which Provider?
| Provider     | Best For                               |
| ------------ | -------------------------------------- |
| OpenAI       | High-quality production embeddings     |
| Gemini       | Google-centric GenAI pipelines         |
| Hugging Face | Open-source, local, cost-free learning |

---

## 👨‍💻 Author

Manthan Jadav
AI / ML & GenAI Enthusiast

🔗 GitHub: https://github.com/Manthan2110

🔗 LinkedIn: https://www.linkedin.com/in/manthanjadav/
