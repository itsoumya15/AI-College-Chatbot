# AI College Chatbot

An interactive AI chatbot that answers college-related queries using a dataset and semantic search.
This project demonstrates how AI, data, and web development can be combined to build a simple and effective assistant.

---

## About the Project

This chatbot is designed to help users ask basic college-related questions such as GPA insights, admission decisions, and statistics.
It uses a vector database (FAISS) to search through data and generate relevant responses.

The goal of this project is to showcase:

* How chatbot systems work
* How datasets can be used for analysis
* How AI can improve user interaction

---

## Features

* Simple and user-friendly chatbot interface
* Semantic search using FAISS
* HuggingFace embeddings for query understanding
* Data insights such as highest GPA and acceptance rate
* Fast backend using Flask

---

## What You Can Ask

You can try questions like:

**Basic conversation**

* hi
* hello
* bye

**GPA related**

* highest gpa
* top gpa

**Admission related**

* admission decision
* will I get admission

**Data insights**

* how many students accepted
* acceptance rate

**Fees**

* fee structure

---

## Tech Stack

* Frontend: HTML, CSS, JavaScript
* Backend: Flask (Python)
* AI/NLP: LangChain and HuggingFace
* Vector Database: FAISS
* Dataset: CSV file

---

## Project Structure

```
AI_Chatbot/
│
├── backend/
│   ├── app.py
│   ├── build_vector.py
│
├── frontend/
│   ├── index.html
│   └── script.js
│
├── data/
│   └── college-admission-dataset.csv
│
├── README.md
└── .gitignore
```

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/AI_Chatbot.git
cd AI_Chatbot
```

---

### 2. Install dependencies

```
pip install flask flask-cors pandas langchain langchain-community langchain-huggingface faiss-cpu sentence-transformers
```

---

### 3. Build the vector database

```
cd backend
python build_vector.py
```

---

### 4. Run the backend

```
python app.py
```

The server will run at:

```
http://127.0.0.1:5000
```

---

### 5. Run the frontend

Open the frontend using Live Server in VS Code:

```
frontend/index.html
```

---

## Output

<img width="731" height="429" alt="image" src="https://github.com/user-attachments/assets/8994b352-7b1c-43f9-9981-08f18744d543" />

Example:

```
You: hi  
Bot: Hello. How can I help you?

You: highest gpa  
Bot: The highest GPA is 4.0  

You: how many students accepted  
Bot: Total accepted students: ___  

You: acceptance rate  
Bot: Acceptance rate is ___%  
```

---

## Limitations

* The chatbot relies on a dataset and cannot answer unrelated questions
* It does not include real college information such as syllabus or exam dates
* Some responses (like fees) are predefined

---

## Future Improvements

* Add real-time college data
* Improve responses using advanced language models
* Enable PDF-based query system
* Enhance user interface

---

## Author

Soumya Singh

---

## Support

If you found this project useful, consider giving it a star on GitHub.
