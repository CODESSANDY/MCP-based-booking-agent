import yaml
import os
from crewai import Agent, Task, Crew, Process
from src.config.tools.mcp_booking_tool import mcp_booking_tool
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


# Utility to load YAML files
def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Paths for config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_PATH = os.path.join(BASE_DIR, "config", "agents.yaml")
TASKS_PATH = os.path.join(BASE_DIR, "config", "tasks.yaml")

# Load YAML configs
agents_config = load_yaml(AGENTS_PATH)
tasks_config = load_yaml(TASKS_PATH)

def build_crew():
    """
    Constructs the CrewAI crew with 3 agents:
    - Booking Researcher
    - Preference Analyzer
    - Booking Recommender
    """
    # Create agents
    researcher = Agent(
        role=agents_config["booking_researcher"]["role"],
        goal=agents_config["booking_researcher"]["goal"],
        backstory=agents_config["booking_researcher"]["backstory"],
        tools=[mcp_booking_tool],
        verbose=True,
        memory=True,
    )

    analyzer = Agent(
        role=agents_config["preference_analyzer"]["role"],
        goal=agents_config["preference_analyzer"]["goal"],
        backstory=agents_config["preference_analyzer"]["backstory"],
        verbose=True,
        memory=True,
    )

    recommender = Agent(
        role=agents_config["booking_recommender"]["role"],
        goal=agents_config["booking_recommender"]["goal"],
        backstory=agents_config["booking_recommender"]["backstory"],
        verbose=True,
        memory=True,
    )

    # Create tasks
    fetch_task = Task(
        description=tasks_config["fetch_listings_task"]["description"],
        expected_output=tasks_config["fetch_listings_task"]["expected_output"],
        agent=researcher,
        tools=[mcp_booking_tool],
    )

    analyze_task = Task(
        description=tasks_config["analyze_preferences_task"]["description"],
        expected_output=tasks_config["analyze_preferences_task"]["expected_output"],
        agent=analyzer,
    )

    recommend_task = Task(
        description=tasks_config["recommend_task"]["description"],
        expected_output=tasks_config["recommend_task"]["expected_output"],
        agent=recommender,
    )

    # Build crew
    crew = Crew(
        agents=[researcher, analyzer, recommender],
        tasks=[fetch_task, analyze_task, recommend_task],
        process=Process.sequential,  # tasks run in sequence
    )

    return crew
