from sentence_transformers import SentenceTransformer, util
from src.utils import load_candidates


def build_candidate_text(candidate):
    """
    Convert a candidate profile into one searchable text.
    """

    profile = candidate.get("profile", {})

    text_parts = []

    # Profile
    text_parts.append(profile.get("headline", ""))
    text_parts.append(profile.get("summary", ""))
    text_parts.append(profile.get("current_title", ""))

    # Skills
    for skill in candidate.get("skills", []):
        text_parts.append(skill.get("name", ""))

    # Career
    for job in candidate.get("career_history", []):
        text_parts.append(job.get("title", ""))
        text_parts.append(job.get("description", ""))

    # Education
    for edu in candidate.get("education", []):
        text_parts.append(edu.get("degree", ""))
        text_parts.append(edu.get("field_of_study", ""))

    # Certifications
    for cert in candidate.get("certifications", []):
        text_parts.append(cert.get("name", ""))

    return " ".join(text_parts)


def get_semantic_scores(
    candidates_file="data/sample_candidates.json",
    jd_file="data/job_description.txt"
):
    """
    Returns a dictionary:
    {
        candidate_id: semantic_score
    }

    Supports both:
    - sample_candidates.json
    - candidates.jsonl
    """

    print("Loading Sentence Transformer Model...")

    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    with open(jd_file, "r", encoding="utf-8") as f:
        job_description = f.read()

    jd_embedding = model.encode(
        job_description,
        convert_to_tensor=True
    )

    # Load JSON or JSONL automatically
    candidates = load_candidates(candidates_file)

    scores = {}

    print("\nCalculating Semantic Scores...\n")

    for candidate in candidates:

        candidate_text = build_candidate_text(candidate)

        candidate_embedding = model.encode(
            candidate_text,
            convert_to_tensor=True
        )

        similarity = util.cos_sim(
            jd_embedding,
            candidate_embedding
        ).item()

        scores[candidate["candidate_id"]] = round(similarity, 4)

    return scores


if __name__ == "__main__":

    semantic_scores = get_semantic_scores()

    top10 = sorted(
        semantic_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    print("Top 10 Semantic Candidates\n")

    for candidate, score in top10:
        print(candidate, "->", score)