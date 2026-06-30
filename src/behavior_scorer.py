from src.utils import load_candidates


def calculate_behavior_score(candidate):
    """
    Calculates a behavioral score based on Redrob engagement signals.
    """

    signals = candidate.get("redrob_signals", {})

    score = 0

    # Profile completeness
    score += signals.get("profile_completeness_score", 0) * 0.20

    # Open to work
    if signals.get("open_to_work_flag", False):
        score += 10

    # Recruiter response
    score += signals.get("recruiter_response_rate", 0) * 20

    # Interview completion
    score += signals.get("interview_completion_rate", 0) * 15

    # Offer acceptance
    offer_rate = signals.get("offer_acceptance_rate", -1)
    if offer_rate != -1:
        score += offer_rate * 10

    # GitHub activity
    github = signals.get("github_activity_score", -1)
    if github != -1:
        score += github * 0.15

    # Search appearance
    score += min(signals.get("search_appearance_30d", 0), 100) * 0.05

    # Saved by recruiters
    score += min(signals.get("saved_by_recruiters_30d", 0), 50) * 0.30

    # Recruiter profile views
    score += min(signals.get("profile_views_received_30d", 0), 100) * 0.05

    return round(score, 2)


def get_behavior_scores(
    candidates_file="data/sample_candidates.json"
):
    """
    Returns:
    {
        candidate_id : behavior_score
    }

    Supports both JSON and JSONL datasets.
    """

    candidates = load_candidates(candidates_file)

    scores = {}

    for candidate in candidates:
        scores[candidate["candidate_id"]] = calculate_behavior_score(candidate)

    return scores


if __name__ == "__main__":

    scores = get_behavior_scores()

    top10 = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    print("\nTop Behavioral Candidates\n")

    for candidate, score in top10:
        print(candidate, "->", score)