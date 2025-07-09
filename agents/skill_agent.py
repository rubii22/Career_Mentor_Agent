from tools.skill_roadmap_tool import get_career_roadmap

class SkillAgent:
    def __init__(self):
        self.name = "SkillAgent"

    def run(self, field: str) -> str:
        intro = "📘 Hello! I'm the Skill Agent. I can provide you with a skill roadmap for any valid field."
        valid_fields = ["Web Developer", "Data Scientist", "AI Engineer"]

        if field in valid_fields:
            skills = get_career_roadmap(field)
            return intro + f"\n📚 To become a {field}, you should learn: {skills}"
        return intro + "\n🔄 Please provide a valid field like Web Developer, Data Scientist, or AI Engineer."
