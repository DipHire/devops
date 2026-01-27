def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total, max_marks):
    return (total / max_marks) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"
