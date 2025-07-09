from tools.job_roles_tool import get_job_roles

class JobAgent:
    def __init__(self):
        self.name = "JobAgent"

    def run(self, field: str) -> str:
        intro = "💼 I'm the Job Agent. I can tell you real-world job roles for your chosen field."
        valid_fields = ["Web Developer", "Data Scientist", "AI Engineer"]

        if field in valid_fields:
            roles = get_job_roles(field)
            return intro + f"\n💼 Job roles for {field} include: {roles}"
        return intro + "\n🔄 Please provide a valid field like Web Developer, Data Scientist, or AI Engineer."
