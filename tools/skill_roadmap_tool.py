def get_career_roadmap(field: str) -> str:
    roadmaps = {
        "Web Developer": "HTML, CSS, JavaScript, Git, React, Node.js, Responsive Design",
        "Data Scientist": "Python, Statistics, Pandas, Machine Learning, SQL, Data Visualization",
        "AI Engineer": "Python, Deep Learning, TensorFlow, NLP, PyTorch, MLOps, Cloud AI APIs"
    }
    return roadmaps.get(field, "No roadmap found for this field.")
