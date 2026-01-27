def validate_marks(marks):
    for m in marks:
        if m < 0 or m > 100:
            return False
    return True

def validate_name(name):
    return name.isalpha()
