from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

@CrewBase
class BloggerAgent():
    """BloggerAgent crew"""

    agents_config = 'config/agents_blogger.yaml'
    tasks_config = 'config/tasks_blogger.yaml'

    @agent
    def trend_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_finder'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @task
    def identify_trending_topics_task(self) -> Task:
        return Task(
            config=self.tasks_config['identify_trending_topics'],
            output_file='trending_topics.txt'
        )

    @task
    def research_topics_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_topics'],
            output_file='research_topics_output.json'
        )

    @task
    def analyze_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_data'],
            output_file='analysis_reports.json'
        )

    @task
    def create_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_content'],
            output_file='final_blog_posts.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the BloggerAgent crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
