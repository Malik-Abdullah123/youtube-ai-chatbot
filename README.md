# 🎥 YouTube AI Chatbot (RAG)

An AI-powered YouTube chatbot that allows users to ask questions about any YouTube video using **Retrieval-Augmented Generation (RAG)**.

The application extracts the transcript from a YouTube video, converts it into embeddings using OpenAI, stores them in a FAISS vector database, and answers user questions through an interactive Flask web interface.

---

## 🚀 Features

- 🎬 Load any YouTube video using its Video ID
- 💬 Chat with the video content
- 🤖 OpenAI GPT-4o Mini for intelligent responses
- 📚 RAG (Retrieval-Augmented Generation)
- 🧠 FAISS Vector Database
- 📄 Automatic Transcript Extraction
- 💻 Beautiful Flask Web Interface
- ⚡ Fast Semantic Search
- 📝 Chat History Support

---

## 🖼️ Demo

> Add screenshots here after running the project.

### Home Page

![Home](images/home.png)

### Chat Interface

![Chat](images/chat.png)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| LangChain | RAG Pipeline |
| OpenAI | LLM & Embeddings |
| FAISS | Vector Database |
| YouTube Transcript API | Transcript Extraction |
| HTML | Frontend |
| CSS | Styling |
| JavaScript | Client-side Logic |

---

## 📂 Project Structure

```text
youtube-ai-chatbot/
│
├── app.py
├── requirements.txt
├── .env
│
├── utils/
│   └── rag.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Malik-Abdullah123/youtube-ai-chatbot.git

cd youtube-ai-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a **.env** file.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. Enter a YouTube Video ID.
2. Click **Load Video**.
3. Transcript is downloaded.
4. Transcript is split into chunks.
5. Embeddings are created using OpenAI.
6. FAISS stores the embeddings.
7. Ask questions about the video.
8. AI retrieves relevant chunks and generates an accurate answer.

---

## 📸 Screenshots

Add your screenshots here.

Example:

```
images/
    home.png
    chat.png
```

---

## 📦 Requirements

- Python 3.12+
- OpenAI API Key
- Internet Connection

---

## 🌟 Future Improvements

- User Authentication
- Dark Mode
- Streamlit Version
- Multi-Video Chat
- PDF Export
- Voice Input
- YouTube Thumbnail Preview
- Chat Memory
- Docker Support
- Deployment on Render

---

## 👨‍💻 Author

**Muhammad Abdullah**

BS Computer Science

University of Lahore

GitHub:
https://github.com/Malik-Abdullah123

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
