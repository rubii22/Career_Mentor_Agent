import chainlit as cl
from model.gemini_model import GeminiModel
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

# Shared model & agents
model = GeminiModel()
career_agent = CareerAgent(model)
skill_agent = SkillAgent()
job_agent = JobAgent()

def extract_recommended_field(response: str) -> str:
    for field in ["Web Developer", "Data Scientist", "AI Engineer"]:
        if f"career as a {field}" in response or f"career as an {field}" in response:
            return field
    return None

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content.strip()

    try:
        # If user is asking for roadmap or job roles
        lowered = user_input.lower()
        if "roadmap" in lowered or "skills" in lowered:
            for field in ["Web Developer", "Data Scientist", "AI Engineer"]:
                if field.lower() in lowered:
                    await cl.Message(content=skill_agent.run(field)).send()
                    return
            await cl.Message(content="📌 Please mention a valid field like Web Developer, Data Scientist, or AI Engineer.").send()
            return

        elif "job" in lowered or "roles" in lowered:
            for field in ["Web Developer", "Data Scientist", "AI Engineer"]:
                if field.lower() in lowered:
                    await cl.Message(content=job_agent.run(field)).send()
                    return
            await cl.Message(content="📌 Please mention a valid field like Web Developer, Data Scientist, or AI Engineer.").send()
            return

        # Otherwise, handle career intent
        response = career_agent.run(user_input)
        await cl.Message(content=response).send()

        recommended_field = extract_recommended_field(response)
        if recommended_field:
            await cl.Message(content=skill_agent.run(recommended_field)).send()
            await cl.Message(content=job_agent.run(recommended_field)).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()
