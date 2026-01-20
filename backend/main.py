from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI()

class UserInput(BaseModel):
    subject: str
    syllabus: str
    exam_date: str
    hours_per_day: int

@app.post("/generate-plan")
async def generate_plan(data: UserInput):
    prompt = f"""
You are an academic mentor.

Subject: {data.subject}
Syllabus: {data.syllabus}
Exam Date: {data.exam_date}
Daily Study Hours: {data.hours_per_day}

Create a clear, practical study plan.
"""

    try:
        result = await agent.run(prompt)
        return {"response": result.output_text}
    except Exception as e:
        # 🔥 Fallback response (IMPORTANT)
        return {
            "response": (
                "Here is a sample study plan:\n\n"
                "• Study core concepts daily\n"
                "• Revise previous topics every 3 days\n"
                "• Practice questions regularly\n"
                "• Do full revision in the last week\n\n"
                "Tip: Stay consistent and avoid last-minute stress."
            ),
            "note": "AI service temporarily unavailable, fallback used."
        }

