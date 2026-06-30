"""
TalentLens-AI
Final Scoring Engine
"""

from src.semantic_matcher import get_semantic_scores
from src.behavior_scorer import get_behavior_scores
from src.career_analyzer import get_career_scores
from src.skill_scorer import get_skill_scores
from src.experience_scorer import get_experience_scores


def normalize(value, minimum, maximum):
    """
    Normalize a value between 0 and 1.
    """
    if maximum == minimum:
        return 0

    return (value - minimum) / (maximum - minimum)


def get_final_scores(
    candidates_file="data/sample_candidates.json",
    jd_file="data/job_description.txt"
):
    """
    Returns a detailed AI ranking with a professional
    100-point display score.
    """

    semantic = get_semantic_scores(candidates_file, jd_file)
    behavior = get_behavior_scores(candidates_file)
    career = get_career_scores(candidates_file)
    skill = get_skill_scores(candidates_file)
    experience = get_experience_scores(candidates_file)

    sem_min, sem_max = min(semantic.values()), max(semantic.values())
    beh_min, beh_max = min(behavior.values()), max(behavior.values())
    car_min, car_max = min(career.values()), max(career.values())
    skill_min, skill_max = min(skill.values()), max(skill.values())
    exp_min, exp_max = min(experience.values()), max(experience.values())

    results = []

    for cid in semantic.keys():

        semantic_score = round(
            normalize(semantic[cid], sem_min, sem_max) * 40,
            2
        )

        career_score = round(
            normalize(career[cid], car_min, car_max) * 20,
            2
        )

        skill_score = round(
            normalize(skill[cid], skill_min, skill_max) * 15,
            2
        )

        behavior_score = round(
            normalize(behavior[cid], beh_min, beh_max) * 15,
            2
        )

        experience_score = round(
            normalize(experience[cid], exp_min, exp_max) * 10,
            2
        )

        final_score = round(
            semantic_score
            + career_score
            + skill_score
            + behavior_score
            + experience_score,
            2
        )

        results.append({
            "Candidate_ID": cid,
            "Semantic": semantic_score,
            "Career": career_score,
            "Skill": skill_score,
            "Behavior": behavior_score,
            "Experience": experience_score,
            "Final_Score": final_score
        })

    # Convert highest candidate to 100
    highest = max(row["Final_Score"] for row in results)

    for row in results:
        row["Display_Score"] = round(
            (row["Final_Score"] / highest) * 100,
            2
        )

    results.sort(
        key=lambda x: x["Display_Score"],
        reverse=True
    )

    return results


if __name__ == "__main__":

    scores = get_final_scores()

    print("\n" + "=" * 60)
    print("TOP 10 FINAL SCORES")
    print("=" * 60)

    for i, row in enumerate(scores[:10], start=1):

        print(
            f"\n{i}. {row['Candidate_ID']}"
        )

        print(f"Display Score : {row['Display_Score']}/100")
        print(f"Semantic      : {row['Semantic']}/40")
        print(f"Career        : {row['Career']}/20")
        print(f"Skill         : {row['Skill']}/15")
        print(f"Behavior      : {row['Behavior']}/15")
        print(f"Experience    : {row['Experience']}/10")