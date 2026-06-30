import json

file_path = "data/sample_candidates.json"

with open(file_path, "r", encoding="utf-8") as file:
    candidates = json.load(file)

print(f"Total Candidates: {len(candidates)}\n")

for i, candidate in enumerate(candidates[:5], start=1):
    print("=" * 50)
    print(f"Candidate {i}")
    print("=" * 50)

    print("Candidate ID:", candidate["candidate_id"])
    print("Current Title:", candidate["profile"]["current_title"])
    print("Experience:", candidate["profile"]["years_of_experience"], "years")
    print("Industry:", candidate["profile"]["current_industry"])

    print("\nTop Skills:")
    for skill in candidate["skills"][:5]:
        print("-", skill["name"], f"({skill['proficiency']})")

    print("\nGitHub Activity Score:",
          candidate["redrob_signals"]["github_activity_score"])

    print("Recruiter Response Rate:",
          candidate["redrob_signals"]["recruiter_response_rate"])

    print("\n")