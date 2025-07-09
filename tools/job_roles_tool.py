def get_job_roles(field: str) -> str:
    roles = {
        "Web Developer": "Frontend Developer, Backend Developer, Full Stack Engineer, UI Developer",
        "Data Scientist": "Data Analyst, ML Engineer, Business Intelligence Analyst, Research Scientist",
        "AI Engineer": "AI Researcher, NLP Engineer, ML Engineer, Computer Vision Engineer"
    }
    return roles.get(field, "No job roles found for this field.")
