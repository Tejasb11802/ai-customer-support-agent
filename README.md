# 🧠 Customer Support Agent

This project demonstrates a simple customer support assistant powered by [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and OpenAI's GPT models.

It categorizes user queries into one of three categories—**Technical**, **Billing**, or **General**—and then generates a helpful response accordingly.

## 🚀 Features

- Query classification using LLM
- Modular LangGraph graph design
- Streamlined user response pipeline
- Easy to extend for additional categories or actions

## 🧩 Requirements

Install dependencies using pip:

```bash
pip install langgraph langchain openai
```

## 🛠️ Usage

1. Clone the repository or copy the script.

2. Replace the API key placeholder with your actual key in `customer_support_agent.py`:

```python
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key="your-api-key-here")
```

3. Run the script:

```bash
python customer_support_agent.py
```

## 📂 File Structure

- `customer_support_agent.py`: Main script for building and running the LangGraph pipeline.

## 💡 Example

Example query:

```
🧠 Query: My internet is not working since last night.
🤖 Response: It sounds like you're experiencing a technical issue. Please try restarting your router. If the problem persists, contact our support team.
```

## 🤝 Contributing

Feel free to fork and adapt this for more complex support systems. You can add additional nodes for FAQ lookups, ticket generation, or live agent escalation.

---

Made with ❤️ using LangGraph.
