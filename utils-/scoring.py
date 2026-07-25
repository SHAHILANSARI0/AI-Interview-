def calculate_score(answers):

    total = len(answers)

    answered = 0

    for ans in answers:
        if ans.strip() != "":
            answered += 1

    score = int((answered / total) * 100)

    return score


def performance(score):

    if score >= 90:
        return "Excellent"

    elif score >= 75:
        return "Good"

    elif score >= 50:
        return "Average"

    else:
        return "Needs Improvement"
    
