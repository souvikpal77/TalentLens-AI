from src.utils import load_candidates


def calculate_career_score(candidate):
    """
    Calculates a career relevance score based on
    experience, job titles and career progression.
    """

    profile = candidate.get("profile", {})
    career = candidate.get("career_history", [])

    score = 0

    # Years of Experience
    years = profile.get("years_of_experience", 0)
    score += years * 4

    # Current Position Bonus
    current_title = profile.get("current_title", "").lower()

    senior_titles = [
        "lead",
        "senior",
        "principal",
        "architect",
        "manager",
        "head",
        "director",
        "staff"
    ]

    for word in senior_titles:
        if word in current_title:
            score += 20
            break

    # Career Stability
    total_months = 0

    for job in career:
        total_months += job.get("duration_months", 0)

    score += min(total_months / 12, 20)

    # Number of Relevant Jobs
    score += min(len(career) * 3, 15)

    return round(score, 2)


def get_career_scores(
    candidates_file="data/sample_candidates.json"
):
    """
    Returns:
    {
        candidate_id : career_score
    }

    Supports both JSON and JSONL datasets.
    """

    candidates = load_candidates(candidates_file)

    scores = {}

    for candidate in candidates:
        scores[candidate["candidate_id"]] = calculate_career_score(candidate)

    return scores


if __name__ == "__main__":

    scores = get_career_scores()

    top10 = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    print("\nTop Career Scores\n")

    for candidate, score in top10:
        print(candidate, "->", score)