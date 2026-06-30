from src.utils import load_candidates

PROFICIENCY_SCORE = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
    "expert": 4
}


def calculate_skill_score(candidate):
    """
    Calculates skill score based on:
    - Skill proficiency
    - Endorsements
    - Duration of skill usage
    """

    score = 0

    skills = candidate.get("skills", [])

    for skill in skills:

        proficiency = skill.get("proficiency", "beginner").lower()

        score += PROFICIENCY_SCORE.get(proficiency, 1) * 5

        score += min(skill.get("endorsements", 0), 20) * 0.5

        score += min(skill.get("duration_months", 60), 60) * 0.1

    return round(score, 2)


def get_skill_scores(
    candidates_file="data/sample_candidates.json"
):
    """
    Returns:
    {
        candidate_id : skill_score
    }

    Supports JSON and JSONL.
    """

    candidates = load_candidates(candidates_file)

    scores = {}

    for candidate in candidates:
        scores[candidate["candidate_id"]] = calculate_skill_score(candidate)

    return scores


if __name__ == "__main__":

    scores = get_skill_scores()

    top10 = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    print("\nTop Skill Scores\n")

    for cid, score in top10:
        print(cid, "->", score)