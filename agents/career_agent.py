class CareerAgent:
    def __init__(self, model):
        self.model = model
        self.introduced = False

    def run(self, user_input: str) -> str:
        intro = (
            "👋 Hi! I'm your **Career Mentor Agent**.\n"
            "🧠 I specialize in helping students explore careers based on their interests.\n"
            "💼 I can guide you on career options, required skills, and how to get started.\n"
            "📩 Just tell me what you like doing or your dream field!\n"
        )

        if not self.introduced:
            self.introduced = True
            return intro

        if len(user_input.strip()) < 10:
            return "❗ Please share something about your interests, skills, or goals so I can guide you better."

        prompt = (
            "You are a career advisor. Based on the user's input, recommend ONE suitable career from: "
            "Web Developer, Data Scientist, or AI Engineer. "
            "Explain why it fits, what skills are needed, and how to begin.\n\n"
            f"User: {user_input}"
        )

        return self.model.generate(prompt)
