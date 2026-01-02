# 🧠 LangChain LLM Demo (Google Gemini)

A simple, beginner-friendly demonstration of using a **Large Language Model (LLM)** with **LangChain**, powered by **Google Gemini**.

This example focuses on **basic LLM invocation** (not chat models) to help understand how LangChain interacts with foundation models at a low level.

---

## 🚀 About This Example

This script demonstrates:
- How to initialize an **LLM (not ChatModel)** in LangChain
- How to connect **Google Gemini** using an API key
- How to invoke the model with a prompt
- How LLMs differ from chat-based models in LangChain

This is ideal for learners starting their **GenAI / LangChain journey**.

---

## 📂 File Overview

```bash
📁 1.LLMs
│
├── 1_llm_demo.py
└── README.md
```

---

## 📄 File Explanation

> 1_llm_demo.py
- Uses GoogleGenerativeAI from LangChain
- Integrates Google Gemini (gemini-2.5-flash)
- Demonstrates basic prompt → response workflow
- Uses .invoke() to get a raw LLM output

> Example task:
Asking a factual question: “Who is the Prime Minister of India now?”

---

## 🧠 Key Concepts Covered

- What is an LLM in LangChain
- Difference between:
  - LLM (single-turn text generation)
  - ChatModel (role-based conversations)
- Prompt execution using .invoke()
- Model selection and configuration

--- 

## 🎯 Use Cases

- Learning LangChain fundamentals
- Understanding LLM vs ChatModel
- Quick factual queries
- Lightweight GenAI experiments

---

## 👨‍💻 Author

Manthan Jadav
AI / ML & GenAI Enthusiast

🔗 GitHub: https://github.com/Manthan2110

🔗 LinkedIn: https://www.linkedin.com/in/manthanjadav/

---

⭐ If this helped you understand LangChain basics, consider starring the repository!
