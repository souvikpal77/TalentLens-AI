from src.utils import load_candidates


def calculate_experience_score(candidate):
    """
    Calculates experience score based on
    total years of experience and career history.
    """

    profile = candidate.get("profile", {})
    career = candidate.get("career_history", [])

    score = 0

    # Years of experience
    years = profile.get("years_of_experience", 0)
    score += years * 10

    # Experience bonus
    if years >= 15:
        score += 25
    elif years >= 10:
        score += 20
    elif years >= 7:
        score += 15
    elif years >= 5:
        score += 10
    elif years >= 3:
        score += 5

    # Long-term stability bonus
    total_months = 0

    for job in career:
        total_months += job.get("duration_months", 0)

    if total_months >= 120:
        score += 10
    elif total_months >= 60:
        score += 5

    return round(score, 2)


def get_experience_scores(
    candidates_file="data/sample_candidates.json"
):
    """
    Returns:
    {
        candidate_id : experience_score
    }

    Supports JSON and JSONL.
    """

    candidates = load_candidates(candidates_file)

    scores = {}

    for candidate in candidates:
        scores[candidate["candidate_id"]] = calculate_experience_score(candidate)

    return scores


if __name__ == "__main__":

    scores = get_experience_scores()

    top10 = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    print("\nTop Experience Candidates\n")

    for cid, score in top10:
        print(cid, "->", score)