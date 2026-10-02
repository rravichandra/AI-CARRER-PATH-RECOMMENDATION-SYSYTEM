# recommendation_engine.py

CAREER_DATABASE = {
    "Data Scientist": {
        "skills": ["python", "math", "statistics", "sql", "machine learning"],
        "description": "Analyzes complex data to help organizations make strategic decisions."
    },
    "Software Engineer": {
        "skills": ["java", "python", "data structures", "git", "problem solving"],
        "description": "Designs, builds, and maintains software applications."
    },
    "UI/UX Designer": {
        "skills": ["figma", "wireframing", "creativity", "user research", "css"],
        "description": "Designs intuitive and visually appealing digital interfaces."
    },
    "Cybersecurity Analyst": {
        "skills": ["networking", "linux", "security", "python", "ethical hacking"],
        "description": "Protects company networks and systems from cyber threats."
    }
}

def recommend_career(user_skills):
    user_skill_set = set(skill.strip().lower() for skill in user_skills)
    scores = {}

    for career, details in CAREER_DATABASE.items():
        required_skills = set(details["skills"])
        matched = user_skill_set.intersection(required_skills)
        
        if required_skills:
            match_percentage = (len(matched) / len(required_skills)) * 100
        else:
            match_percentage = 0.0
            
        scores[career] = (match_percentage, details["description"])

    # Sort recommendations by highest percentage match
    sorted_recommendations = sorted(scores.items(), key=lambda x: x[1][0], reverse=True)
    return sorted_recommendations