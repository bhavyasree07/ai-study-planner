from pydantic_ai import Agent

agent = Agent(
    model="openrouter:mistralai/mistral-7b-instruct",
    system_prompt="You are an expert academic mentor who creates clear study plans."
)
