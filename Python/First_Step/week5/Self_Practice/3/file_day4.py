import json
my_skills  = {
    "skill1" : "HTML",
    "skill2" : "CSS",
    "skill3" : "Python",
}
with open("skills.json", "w", encoding="utf-8") as skills_file:
    json.dump(my_skills, skills_file)