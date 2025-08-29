# Day 03 – Python Crash Demo

# Data types
name = "Nora"
age = 30
skills = ["Python", "Data", "AI"]
is_learning = True

# Function
def introduce(person, skill_list):
    print(f"👋 Hello, I'm {person}.")
    print("🧠 Skills:", ", ".join(skill_list))

# Loop
for i in range(3):
    print(f"🔥 Loop count: {i}")

# Logic
if is_learning:
    print("🚀 You're learning AI. Respect!")
else:
    print("😴 Time to wake up!")

introduce(name, skills)
