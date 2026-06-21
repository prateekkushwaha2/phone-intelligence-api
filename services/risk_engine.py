def calculate_risk(data):

    score = 0

    if not data.get("valid"):
        score += 60

    if data.get("carrier") == "":
        score += 10

    if score >= 60:
        level = "high"

    elif score >= 20:
        level = "medium"

    else:
        level = "low"

    return {
        "score": score,
        "level": level
    }
