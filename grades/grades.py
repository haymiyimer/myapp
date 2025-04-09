# This file helps with grade calculations

def compute_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
