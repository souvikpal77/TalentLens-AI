import json

file_path = "data/sample_candidates.json"

with open(file_path, "r", encoding="utf-8") as file:
    candidates = json.load(file)


def extract_features(candidate):
    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    features = {
        "candidate_id": candidate["candidate_id"],
        "title": profile["current_title"],
        "experience": profile["years_of_experience"],
        "industry": profile["current_industry"],
        "total_skills": len(candidate["skills"]),
        "github_score": signals["github_activity_score"],
        "response_rate": signals["recruiter_response_rate"],
        "interview_rate": signals["interview_completion_rate"],
        "profile_score": signals["profile_completeness_score"]
    }

    return features


for candidate in candidates[:5]:
    print(extract_features(candidate))