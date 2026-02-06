from langgraph.graph import StateGraph

# --- Define Agents ---

def planner(state):
    task = state["input"]
    return {"task": f"Plan steps to answer: {task}"}

def researcher(state):
    task = state["task"]
    return {"data": f"Research data collected for -> {task}"}

def reasoner(state):
    data = state["data"]
    return {"analysis": f"Reasoning based on data: {data}"}

def responder(state):
    analysis = state["analysis"]
    return {"output": f"Final Answer generated using {analysis}"}

# --- Build Graph ---

graph = StateGraph(dict)

graph.add_node("planner", planner)
graph.add_node("researcher", researcher)
graph.add_node("reasoner", reasoner)
graph.add_node("responder", responder)

graph.set_entry_point("planner")

graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "reasoner")
graph.add_edge("reasoner", "responder")

app = graph.compile()

# --- Run ---
if __name__ == "__main__":
    result = app.invoke({"input": "Explain LangChain"})
    print(result["output"])
