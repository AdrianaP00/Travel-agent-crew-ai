from crewai import Agent

researcher = Agent(
    role="Senior Data Researcher",
    goal="Uncover cutting-edge developments in AI",
    backstory="A seasoned researcher with a knack for uncovering the latest developments in AI.",
    tools=[SerperDevTool()],
    verbose=True
)