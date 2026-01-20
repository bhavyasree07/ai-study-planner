import os
from pydantic_ai import Agent
from schemas import StudyPlan

# Temporary local key (safe for testing)
os.environ.setdefault("OPENROUTER_API_KEY", "sk-test")

agent = Agent(
    model="openrouter:mistralai/mistral-7b-instruct",
    result_type=StudyPlan,
    system_prompt=(
        "You are an expert academic mentor. "
        "Create a realistic, easy-to-follow study plan for students."
    ),
)
