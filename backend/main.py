from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class UserInput(BaseModel):
    subject: str
    syllabus: str
    exam_date: str
    hours_per_day: int

@app.post("/generate-plan")
async def generate_plan(data: UserInput):
    prompt = f"""
Subject: {data.subject}
Syllabus: {data.syllabus}
Exam Date: {data.exam_date}
Daily Study Hours: {data.hours_per_day}
"""
    result = await agent.run(prompt)
    return result.data
