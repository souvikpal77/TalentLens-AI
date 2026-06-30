import csv
import os

from src.scorer import get_final_scores

# ==========================================
# CHANGE DATASET HERE
# ==========================================

DATASET = "data/sample_candidates.json"

# For Hackathon Final
# DATASET = "data/candidates.jsonl"

JD_FILE = "data/job_description.txt"

# ==========================================


def main():

    print("=" * 60)
    print("TalentLens-AI Candidate Ranking System")
    print("=" * 60)

    scores = get_final_scores(
        candidates_file=DATASET,
        jd_file=JD_FILE
    )

    print("\n🏆 TOP 10 CANDIDATES\n")

    for rank, row in enumerate(scores[:10], start=1):

        print(
            f"{rank}. {row['Candidate_ID']} -> {row['Display_Score']}/100"
        )

    os.makedirs("outputs", exist_ok=True)

    output_file = "outputs/submission.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Rank",
            "Candidate_ID",
            "Display_Score",
            "Semantic",
            "Career",
            "Skill",
            "Behavior",
            "Experience"
        ])

        for rank, row in enumerate(scores, start=1):

            writer.writerow([
                rank,
                row["Candidate_ID"],
                row["Display_Score"],
                row["Semantic"],
                row["Career"],
                row["Skill"],
                row["Behavior"],
                row["Experience"]
            ])

    print("\n" + "=" * 60)
    print("✅ submission.csv generated successfully!")
    print(f"📄 Location: {output_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()