# app.py
import tkinter as tk
from tkinter import messagebox
import json
from recommendation_engine import recommend_career

def get_recommendation():
    name = entry_name.get().strip()
    skills_input = entry_skills.get().strip()

    if not name or not skills_input:
        messagebox.showwarning("Input Error", "Please enter both your name and skills.")
        return

    user_skills = [s.strip() for s in skills_input.split(",")]
    recommendations = recommend_career(user_skills)

    # Clear existing text in result box
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    result_text.insert(tk.END, f"=== Career Recommendation Report for {name} ===\n\n")

    for career, (score, desc) in recommendations:
        result_text.insert(tk.END, f"• {career}: {score:.1f}% Match\n")
        result_text.insert(tk.END, f"  Overview: {desc}\n\n")

    result_text.config(state=tk.DISABLED)

    # Save student record automatically
    top_match = recommendations[0]
    save_record(name, user_skills, top_match[0], top_match[1][0])

def save_record(name, skills, career, score):
    record = {
        "name": name,
        "skills": skills,
        "top_recommendation": career,
        "match_score": score
    }
    try:
        try:
            with open("history.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(record)

        with open("history.json", "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error saving record:", e)

# Window Setup
window = tk.Tk()
window.title("AI Career Path Recommendation System")
window.geometry("520x580")

tk.Label(window, text="AI Career Recommendation System", font=("Arial", 14, "bold")).pack(pady=15)

tk.Label(window, text="Student Name:", font=("Arial", 10, "bold")).pack(anchor="w", padx=25)
entry_name = tk.Entry(window, width=55)
entry_name.pack(padx=25, pady=5)

tk.Label(window, text="Enter Your Skills (separated by commas):\nExample: python, math, sql, linux", font=("Arial", 10)).pack(anchor="w", padx=25, pady=(10, 0))
entry_skills = tk.Entry(window, width=55)
entry_skills.pack(padx=25, pady=5)

btn = tk.Button(window, text="Analyze & Recommend", command=get_recommendation, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=15)

result_text = tk.Text(window, width=58, height=16, state=tk.DISABLED)
result_text.pack(padx=25, pady=10)

window.mainloop()