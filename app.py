from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# ----------------------------
# Flask setup
# ----------------------------
app = Flask(__name__)
CORS(app)

# ----------------------------
# Load embeddings
# ----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ----------------------------
# Load FAISS DB
# ----------------------------
db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

# ----------------------------
# Home route
# ----------------------------
@app.route("/")
def home():
    return "🎓 AI College Chatbot is Running!"

# ----------------------------
# Chat route
# ----------------------------
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        query = data.get("message").lower()

        # ----------------------------
        # 1. Greetings
        # ----------------------------
        if query in ["hi", "hello", "hey"]:
            return jsonify({
                "response": "Hello 👋! How can I help you with college queries today?"
            })

        # ----------------------------
        # 2. Bye
        # ----------------------------
        if "bye" in query:
            return jsonify({
                "response": "Goodbye 👋! Have a great day."
            })

        # ----------------------------
        # 3. Fee Structure
        # ----------------------------
        if "fee" in query:
            return jsonify({
                "response": """💰 Fee Structure (Approx):

Tuition Fees: ₹80,000 per year
Hostel Fees: ₹60,000 per year
Mess Fees: ₹40,000 per year

👉 Total: ~₹1.8 Lakhs/year"""
            })

        # ----------------------------
        # 4. Load multiple docs for analysis
        # ----------------------------
        docs_all = db.similarity_search("", k=200)

        gpas = []
        decisions = []

        for doc in docs_all:
            text = doc.page_content

            for part in text.split("|"):
                if "gpa" in part.lower():
                    try:
                        gpas.append(float(part.split(":")[1]))
                    except:
                        pass

                if "decision" in part.lower():
                    try:
                        decisions.append(int(part.split(":")[1]))
                    except:
                        pass

        # ----------------------------
        # 5. Highest GPA
        # ----------------------------
        if "highest gpa" in query or "top gpa" in query:
            if gpas:
                return jsonify({
                    "response": f"🎓 The highest GPA is {max(gpas)}"
                })

        # ----------------------------
        # 6. Admission decision
        # ----------------------------
        if "admission" in query or "decision" in query:
            docs = db.similarity_search(query, k=1)

            if docs:
                text = docs[0].page_content

                for part in text.split("|"):
                    if "decision" in part.lower():
                        try:
                            val = int(part.split(":")[1])
                            if val == 1:
                                return jsonify({
                                    "response": "🎉 This student is likely to be ACCEPTED."
                                })
                            else:
                                return jsonify({
                                    "response": "❌ This student is likely to be REJECTED."
                                })
                        except:
                            pass

        # ----------------------------
        # 7. Count accepted students
        # ----------------------------
        if "how many students accepted" in query:
            accepted = decisions.count(1)
            return jsonify({
                "response": f"✅ Total accepted students: {accepted}"
            })

        # ----------------------------
        # 8. Acceptance rate
        # ----------------------------
        if "acceptance rate" in query:
            if decisions:
                rate = (decisions.count(1) / len(decisions)) * 100
                return jsonify({
                    "response": f"📊 Acceptance rate is approximately {rate:.2f}%"
                })

        # ----------------------------
        # 9. Default FAISS search
        # ----------------------------
        docs = db.similarity_search(query, k=1)

        if docs:
            text = docs[0].page_content
            cleaned = text.replace(" | ", "\n")

            return jsonify({
                "response": cleaned + "\n👉 Thank you for your question 😊"
            })

        # ----------------------------
        # 10. Fallback
        # ----------------------------
        return jsonify({
            "response": "Sorry, I couldn't understand your question."
        })

    except Exception as e:
        return jsonify({"response": str(e)})


# ----------------------------
# Run server
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)