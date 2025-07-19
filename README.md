# 🧠 Alpha – Voice-Controlled Intelligent Assistant 🎙️

**Alpha** is an intelligent voice assistant written in Python. It can open websites, play music, fetch news, and even answer questions using AI – all triggered by your voice!

---

## 🚀 Features

✅ **Voice-activated commands** (Say "Alpha")  
✅ Open websites: YouTube, Google, LinkedIn, GitHub, etc.  
✅ Fetch **technology news** using NewsAPI  
✅ Get **smart answers** from Gemini AI  
✅ **Text-to-speech replies** using gTTS + Pygame  
✅ Modular, beginner-friendly code  

---

## 🧠 Tech Stack

- Python 3.x  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)  
- [gTTS](https://pypi.org/project/gTTS/)  
- [Pygame](https://www.pygame.org/news)  
- [Google Gemini AI](https://ai.google.dev/)  
- [NewsAPI](https://newsapi.org)  
- `.env` via [`python-dotenv`](https://pypi.org/project/python-dotenv/) for secure API keys

---

## ⚙️ Setup Instructions

1. **Clone the repository**

git clone https://github.com/krishhj/alpha-voice-assistant.git
cd alpha-voice-assistant

2. **Install required packages**

pip install -r requirements.txt

3. **Create a .env file**

GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_newsapi_key

4. **Run the assistant**

python alpha.py

---
