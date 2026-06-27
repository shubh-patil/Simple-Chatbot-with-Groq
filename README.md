# 🏋️ Fitness Query Resolver (Streamlit + Groq + LangChain)

A simple AI-powered chatbot that answers **fitness, workout, and weight loss related questions** using **Groq-hosted LLaMA models**, **LangChain**, and a **Streamlit web interface**.

---

## 🚀 Features

* 💬 Ask fitness-related questions in natural language
* 🧠 AI-powered answers using LLaMA 3.3 (Groq API)
* ⚡ Fast inference via Groq infrastructure
* 🌐 Simple and interactive Streamlit UI
* 🔐 Secure API key management using `.env`

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API
* LangChain
* python-dotenv

---

## 📁 Project Structure

```
.
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fitness-query-resolver.git
cd fitness-query-resolver
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` file

Add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_PROJECT=FitnessChatbot
LANGCHAIN_TRACING_V2=true
```

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. User enters a fitness-related question in Streamlit UI
2. Query is sent to LLaMA 3.3 model via Groq API
3. LangChain formats and processes the messages
4. AI returns a structured fitness response

---

## 🧪 Example Questions

* “How can I lose belly fat in 2 months?”
* “Best diet plan for weight loss in India?”
* “How many calories should I eat daily?”
* “Home workout plan for beginners?”

---

## 📌 Future Improvements

* 🔥 Add chat memory (conversation history)
* 📊 Add calorie & BMI calculator
* 🥗 Generate personalized diet plans
* 🏃 Add workout split generator
* 📱 Deploy on Streamlit Cloud

---

## ⚠️ Notes

* Requires a valid Groq API key
* Keep `.env` file private (do not upload to GitHub)
* Ensure stable internet connection for API calls

---

## 👨‍💻 Author

Built as a learning project to explore:

* GenAI application development
* LangChain orchestration
* Streamlit UI building
* LLM integration using Groq

---

## 📜 License

This project is open-source and available under the MIT License.
"# Simple-Chatbot-with-Groq" 
