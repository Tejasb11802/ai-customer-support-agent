import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda, RunnableConfig
from langchain_core.output_parsers import StrOutputParser

# --- Setup ---
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# --- Shared state ---
class AgentState(dict):
    query: str
    category: str
    response: str

# --- Node 1: Categorization ---
def categorize(state: AgentState):
    prompt = PromptTemplate.from_template(
        "Classify the customer query into one of the following categories: Technical, Billing, General.\nQuery: {query}"
    )
    chain = prompt | llm
    category = chain.invoke({"query": state["query"]}).content.strip()
    return {**state, "category": category}

# --- Node 2: Category-specific responders ---
def tech_response(state: AgentState):
    prompt = PromptTemplate.from_template("Technical Support Response to: {query}")
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content.strip()
    return {**state, "response": response}

def billing_response(state: AgentState):
    prompt = PromptTemplate.from_template("Billing Support Response to: {query}")
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content.strip()
    return {**state, "response": response}

def general_response(state: AgentState):
    prompt = PromptTemplate.from_template("General Support Response to: {query}")
    chain = prompt | llm
    response = chain.invoke({"query": state["query"]}).content.strip()
    return {**state, "response": response}

# --- Conditional logic ---
def route_category(state: AgentState):
    return state["category"].lower()

# --- Graph Building ---
builder = StateGraph(AgentState)
builder.add_node("categorize", categorize)
builder.add_node("technical", tech_response)
builder.add_node("billing", billing_response)
builder.add_node("general", general_response)

builder.set_entry_point("categorize")
builder.add_conditional_edges("categorize", route_category, {
    "technical": "technical",
    "billing": "billing",
    "general": "general"
})
builder.add_edge("technical", END)
builder.add_edge("billing", END)
builder.add_edge("general", END)

graph = builder.compile()

# --- Testing ---
if __name__ == "__main__":
    queries = [
        "My internet is not working since last night.",
        "Why was I charged twice on my credit card?",
        "What are your customer support hours?"
    ]
    for q in queries:
        print(f"\n🧠 Query: {q}")
        result = graph.invoke({"query": q})
        print(f"🤖 Response: {result['response']}")