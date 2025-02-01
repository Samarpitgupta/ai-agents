# ResearchAgent Crew: Advanced Content Research System

Welcome to the ResearchAgent Crew - an AI-powered content research and creation system combining cutting-edge investigation techniques with human-centric content design. Powered by [crewAI](https://crewai.com), this system enables collaborative AI agents to perform deep research and produce high-quality, human-readable content.

## Key Features & Insights

### Advanced Research Capabilities
- **Multi-Source Trend Analysis**  
  Scans Google Trends, social platforms (Reddit/Twitter/TikTok), news cycles, and cultural undercurrents
- **Truth Verification Engine**  
  Cross-checks facts across academic papers, verified news sources, and primary data
- **Temporal Analysis**  
  Examines historical context + future projections (2025+ scenarios)
- **Cultural Relevance Scoring**  
  Identifies authentic trends with longevity estimates (1-10 scale)

### Intelligent Content Generation
- **Cognitive Flow Optimization**  
  Structures content using natural human curiosity patterns
- **Readability Engineering**  
  Implements Flesch-Kincaid optimization for accessibility
- **Multi-Format Blending**  
  Combines text, visual metaphors, and data snapshots seamlessly
- **Interactive Elements**  
  Includes comprehension checkpoints and natural language FAQs

### Generated Insights
- Cultural Relevance Scores for trends
- Accuracy Confidence Levels (fact verification metrics)
- Narrative Flow Maps with engagement hotspots
- Alternative Future Scenarios (3 projections minimum)
- Source Reliability Index (1-5 scale)


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/research_agent/config/agents.yaml` to define your agents
- Modify `src/research_agent/config/tasks.yaml` to define your tasks
- Modify `src/research_agent/crew.py` to add your own logic, tools and specific args
- Modify `src/research_agent/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the research-agent Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Doccumentation

- Visit our [documentation](https://docs.crewai.com)
- [Chat with our docs](https://chatg.pt/DWjSBZn)
