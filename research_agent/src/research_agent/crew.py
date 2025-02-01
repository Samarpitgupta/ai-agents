from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ResearchAgent():
	"""ResearchAgent crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
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

	# To learn more about structured task outputs,
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task


	@task
	def research_task(self) -> Task:
		base_filename = 'report.md'
		output_file = base_filename
		counter = 1

		# Keep checking and incrementing until we find a filename that doesn't exist
		while os.path.exists(output_file):
			output_file = f'Research_Output{counter}.md'
			counter += 1

		return Task(
			config=self.tasks_config['research_task'],
			output_file=output_file
		)

	@task
	def reporting_task(self) -> Task:
		base_filename = 'report.md'
		output_file = base_filename
		counter = 1

		# Keep checking and incrementing until we find a filename that doesn't exist
		while os.path.exists(output_file):
			output_file = f'FinalReport_{counter}.md'
			counter += 1
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file=output_file
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ResearchAgent crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
