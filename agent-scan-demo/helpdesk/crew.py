"""Multi-agent orchestration — agent frameworks that spin up autonomous agents.
Agent Scan should flag the agent-initiation patterns (create_react_agent, Crew)."""
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from crewai import Agent, Crew, Task

def build_langchain_agent(tools):
    llm = ChatOpenAI(model="gpt-4o")
    agent = create_react_agent(llm, tools, prompt="Solve the task")
    return AgentExecutor(agent=agent, tools=tools)

def build_crew():
    researcher = Agent(role="Researcher", goal="find facts", backstory="...")
    writer = Agent(role="Writer", goal="write", backstory="...")
    crew = Crew(agents=[researcher, writer], tasks=[Task(description="report")])
    return crew.kickoff()
