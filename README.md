
# Customer Support Agent

This is a basic but effective customer support assistant built using LangGraph, LangChain, and OpenAI's GPT models. The goal is to automatically categorize incoming user queries as either **Technical**, **Billing**, or **General**, and then provide a relevant, helpful response.

The assistant uses a modular graph structure to break down the logic step by step—making it easy to understand, modify, and extend with more features like FAQs, ticket creation, or escalation.

---

## Features

- Automatically classifies customer queries using a language model.
- Generates relevant responses based on the category.
- Built on a simple graph pipeline for easy customization.
- Easy to extend for more complex workflows.

---

## How to Use

1. Clone or download the repository and open the folder.

2. Open the file `customer_support_agent.py` and add your OpenAI API key where it says:

   ```python
   llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key="your-api-key-here")
   ```

3. Install the required packages:

   ```bash
   pip install langgraph langchain openai
   ```

4. Run the script:

   ```bash
   python customer_support_agent.py
   ```

---

## Example

Here’s how it works with a sample query:

```
Query: My internet is not working since last night.
Response: Please restart your router and try again. If the issue persists, contact technical support.
```

---

## Notes

You can use this as a base to build more advanced support tools. Try adding things like:

- Auto-generated support tickets  
- FAQ search  
- Escalation to a human agent  

This was a fun project to explore how LangGraph workflows can simplify real-world tasks like support automation.
