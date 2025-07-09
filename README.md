# 💼 Career Mentor Agent 🎓

An AI-powered career guidance system that helps students explore suitable career paths, learn required skills, and discover real-world job roles — built using **Google Gemini API** and **Chainlit**, following a structure inspired by the **OpenAI Agent SDK**.

---

## 🚀 Overview

Career planning can be overwhelming — this intelligent assistant makes it easier!  
You simply tell it what you're passionate about, and it recommends a relevant career path, skill roadmap, and job roles using a **multi-agent architecture**.

---

## 🧠 Key Features

✅ Understands user interests and suggests careers  
✅ Provides a **skill roadmap** using a custom tool  
✅ Lists **job roles** for the selected career  
✅ Uses **handoff logic** between agents  
✅ Designed with **Gemini API**, Chainlit, and modular agent-tool SDK structure

---

## 🔗 Architecture

### 🧠 Agents Used:

| Agent        | Role                                                  |
|--------------|-------------------------------------------------------|
| `CareerAgent`| Suggests a career path based on user's input         |
| `SkillAgent` | Returns a list of skills needed for that career      |
| `JobAgent`   | Lists real-world job roles for that career           |

### 🛠️ Tools Used:

| Tool                    | Description                              |
|-------------------------|------------------------------------------|
| `get_career_roadmap()`  | Returns skill roadmap based on field     |
| `get_job_roles()`       | Returns job titles based on field        |

---

## 🔁 Agent Flow (Handoff Logic)

```
User Input ➝ CareerAgent ➝ (detects field)
                      └─> SkillAgent ➝ returns skills
                      └─> JobAgent ➝ returns job roles
```

---

## 📁 Project Structure

```
career-mentor-agent/
│
├── main.py                  # Chainlit message handler & routing
├── .env                     # Gemini API Key
│
├── agents/
│   ├── career_agent.py      # CareerAgent class
│   ├── skill_agent.py       # SkillAgent class
│   └── job_agent.py         # JobAgent class
│
├── model/
│   └── gemini_model.py      # Gemini API model wrapper
│
├── tools/
│   ├── skill_roadmap_tool.py # get_career_roadmap() function
│   └── job_roles_tool.py     # get_job_roles() function
```

---

## 🧪 Example Inputs

| Message                              | Result                                            |
|--------------------------------------|---------------------------------------------------|
| `hi`                                 | Introduction from CareerAgent                    |
| `I enjoy coding and design`          | Suggests "Web Developer" + skills & job roles    |
| `I like solving problems with data`  | Suggests "Data Scientist"                        |
| `Give me a roadmap for AI Engineer`  | Skill roadmap from SkillAgent                    |
| `What are job roles for Web Developer?` | Job titles from JobAgent                      |

---

## 🛠️ Installation Guide

### 1. Clone the repository or copy your project files

### 2. Install dependencies

```bash
pip install chainlit python-dotenv google-generativeai
```

### 3. Add your `.env` file

Create a `.env` file in the root directory and add your Gemini API key:

```ini
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the project

```bash
chainlit run main.py
```

---

## ✅ Assignment Requirements Checklist

| Requirement                         | Status                                      |
|-------------------------------------|---------------------------------------------|
| Use at least 2 tools                | ✅ `get_career_roadmap()`, `get_job_roles()` |
| Use at least 2 agents               | ✅ `CareerAgent`, `SkillAgent`, `JobAgent`   |
| Handoff logic between agents        | ✅ Done in `main.py`                         |
| OpenAI Agent SDK structure followed | ✅ Inspired & modular                        |
| Submit README.md                    | ✅ You're reading it! 🎉                     |
| Submit structured code folder       | ✅ Done and organized                        |

---

## 🧑‍💻 Developer Info

**Rubab Fatima**  
🎓 Frontend Web Developer | Pyhon Programmer | Agentic AI

---

## 💡 Notes

- If you hit a quota error from Gemini API, try again after a few minutes.
- You can easily extend this project to support more fields like UX Designer, Cybersecurity Analyst, etc.

---
