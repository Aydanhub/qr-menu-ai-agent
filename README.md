# 🍽️ QR Menu AI Agent

A smart, AI-powered digital waiter for modern restaurants. Built with FastAPI and Google's Gemini AI, this application provides personalized menu recommendations based on user preferences, dietary restrictions (e.g., allergies, vegan), and conversational context.

## ✨ Features

* **🤖 AI-Powered Recommendations:** Utilizes the Gemini API to analyze customer requests and suggest items exclusively from the predefined restaurant menu.
* **🧠 Conversational Memory:** Maintains chat history to understand follow-up questions (e.g., "What drink goes well with the meal you just suggested?").
* **🛡️ Context Injection & Prompt Engineering:** Strict system instructions prevent the AI from hallucinating or suggesting items outside the actual menu.
* **⚡ High-Performance Backend:** Built on **FastAPI**, providing a fast, lightweight, and modern asynchronous RESTful API.
* **🎨 Premium Frontend:** Features a responsive, "warm minimalism" UI with a dark/cream aesthetic for a luxurious user experience.

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, Uvicorn
* **AI Integration:** Google Generative AI (Gemini Pro/Flash) SDK
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Security:** dotenv (Environment variables), CORS Middleware

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Aydanhub/qr-menu-ai-agent.git](https://github.com/Aydanhub/qr-menu-ai-agent.git)
   cd qr-menu-ai-agent
