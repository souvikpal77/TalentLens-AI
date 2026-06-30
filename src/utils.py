import json

def load_candidates(file_path):
    if file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    elif file_path.endswith(".jsonl"):
        candidates = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    candidates.append(json.loads(line))
        return candidates

    else:
        raise ValueError("Unsupported file format")