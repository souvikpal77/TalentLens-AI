from pathlib import Path
import re

jd_path = Path("data/job_description.txt")

with open(jd_path, "r", encoding="utf-8") as file:
    jd = file.read()

print("=" * 70)
print("JOB DESCRIPTION ANALYSIS")
print("=" * 70)

# -------------------------
# Skills Dictionary
# -------------------------

skills = [
    "python",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "llm",
    "rag",
    "retrieval",
    "vector database",
    "faiss",
    "pinecone",
    "embedding",
    "recommendation",
    "ranking",
    "sql",
    "aws",
    "docker",
    "kubernetes",
    "git"
]

found_skills = []

for skill in skills:
    if re.search(skill, jd, re.IGNORECASE):
        found_skills.append(skill)

print("\nRequired Skills")
print("----------------")

for skill in found_skills:
    print("✓", skill)

# -------------------------
# Experience
# -------------------------

experience = re.findall(r"\d+\+?\s*years?", jd, re.IGNORECASE)

print("\nExperience")
print("----------------")

if experience:
    for exp in experience:
        print(exp)
else:
    print("Not Mentioned")

# -------------------------
# Degree
# -------------------------

degrees = [
    "b.tech",
    "b.e",
    "bachelor",
    "master",
    "m.tech",
    "phd"
]

print("\nEducation")
print("----------------")

degree_found = False

for degree in degrees:
    if re.search(degree, jd, re.IGNORECASE):
        print("✓", degree)
        degree_found = True

if not degree_found:
    print("Not Mentioned")

print("\nAnalysis Completed Successfully")