# This file helps with attendance calculations

def get_attendance_percentage(total_classes, attended_classes):
    if total_classes == 0:
        return 0
    return (attended_classes / total_classes) * 100

def has_good_attendance(percentage):
    return percentage >= 75
