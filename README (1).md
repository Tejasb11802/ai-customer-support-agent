# 🧠 Customer Support Agent

This project showcases a simple yet powerful customer support assistant built using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and OpenAI's GPT models.

It intelligently classifies customer queries into three categories—**Technical**, **Billing**, or **General**—and delivers an appropriate response for each.

---

## 🚀 Features

- Automatic query classification using a language model
- Modular graph structure powered by LangGraph
- Easy-to-follow response generation pipeline
- Fully customizable to support more categories or actions

---

## 🧩 Requirements

Install the required libraries:

```bash
pip install langgraph langchain openai
```

---

## 🛠️ How to Use

1. **Clone or download** the repository and open the project folder.

2. **Set your OpenAI API key** inside `customer_support_agent.py`:

```python
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key="your-api-key-here")
```

3. **Run the script**:

```bash
python customer_support_agent.py
```

---

## 📁 Project Files

- `customer_support_agent.py` – Core script that builds and runs the customer support graph.

---

## 💬 Example Output

```
🧠 Query: My internet is not working since last night.
🤖 Response: Please restart your router and try again. If the issue persists, contact technical support.
```

---

## 🤝 Contributions

You’re welcome to fork and extend this project! Consider adding nodes for FAQs, support ticket generation, or escalation to live agents.

---

Made with ❤️ using LangGraph + LangChain.
