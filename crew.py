from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_openai import ChatOpenAI


@CrewBase
class ProjectCrew:
    """Config files"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    """Agents"""

    @agent
    def agent_1(self) -> Agent:
        return Agent(
            config=self.agents_config["agent_1"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,  # Agent can't delegate tasks
        )

    @agent
    def agent_2(self) -> Agent:
        return Agent(
            config=self.agents_config["agent_2"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            # allow_delegation=True, # You can omit this parameter, default is allow_delegation=True
        )

    @agent
    def agent_3(self) -> Agent:
        return Agent(
            config=self.agents_config["agent_3"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
        )

    """Tasks"""

    @task
    def task_1(self) -> Task:
        return Task(
            config=self.tasks_config["task_1"],
            agent=self.agent_1(),
        )

    @task
    def task_2(self) -> Task:
        return Task(
            config=self.tasks_config["task_2"],
            agent=self.agent_2(),
        )

    @task
    def task_3(self) -> Task:
        return Task(
            config=self.tasks_config["task_3"],
            agent=self.agent_3(),
        )

    """Crew"""

    @crew
    def crew(self) -> Crew:
        """Creates the crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            # process=Process.sequential, # You can omit this line, process=Process.sequential is set by default
            # Process Hierarchical example
            process=Process.hierarchical,
            manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
            # Example with memory
            memory=True,
            embedder={
                "provider": "openai",
                "config": {"model": "text-embedding-3-small"},
            },
            verbose=True,  # Can be True or 2
        )
