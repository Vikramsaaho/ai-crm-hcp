from langgraph.graph import StateGraph, END
from typing import TypedDict
from openai import OpenAI
from core.config import OPENAI_API_KEY

from agent.tools import (
    log_interaction_tool,
    fetch_history_tool,
    edit_interaction_tool,
    follow_up_suggestion_tool   # ✅ FIXED NAME
)

client = OpenAI(api_key=OPENAI_API_KEY)


# ---------------- STATE ----------------
class ChatState(TypedDict):
    message: str
    response: str


# ---------------- ROUTER ----------------
def router_node(state: ChatState):
    msg = state["message"].lower()

    if "log" in msg:
        return {"route": "log"}
    elif "history" in msg:
        return {"route": "history"}
    elif "edit" in msg:
        return {"route": "edit"}
    elif "follow" in msg:
        return {"route": "follow"}
    else:
        return {"route": "ai"}


# ---------------- TOOL NODES ----------------
def log_node(state):
    return {"response": log_interaction_tool(state["message"])}


def history_node(state):
    return {"response": fetch_history_tool(state["message"])}


def edit_node(state):
    return {"response": edit_interaction_tool(state["message"])}


def follow_node(state):
    return {"response": follow_up_suggestion_tool(state["message"])}  # FIXED


# ---------------- AI NODE ----------------
def ai_node(state):
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Healthcare CRM AI assistant."},
            {"role": "user", "content": state["message"]}
        ]
    )

    return {"response": res.choices[0].message.content}


# ---------------- GRAPH ----------------
graph = StateGraph(ChatState)

graph.add_node("router", router_node)
graph.add_node("log", log_node)
graph.add_node("history", history_node)
graph.add_node("edit", edit_node)
graph.add_node("follow", follow_node)
graph.add_node("ai", ai_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    lambda x: x["route"],
    {
        "log": "log",
        "history": "history",
        "edit": "edit",
        "follow": "follow",
        "ai": "ai"
    }
)

graph.add_edge("log", END)
graph.add_edge("history", END)
graph.add_edge("edit", END)
graph.add_edge("follow", END)
graph.add_edge("ai", END)

app_graph = graph.compile()