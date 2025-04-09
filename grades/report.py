# This is the main file that brings everything together

import grades
import attendance

# Student details
name = "Mary"
student_grades = [70, 80, 90]
total_classes = 20
classes_attended = 18

# Calculate grade average and letter
avg = grades.compute_average(student_grades)
letter = grades.get_letter_grade(avg)

# Calculate attendance
att_percent = attendance.get_attendance_percentage(total_classes, classes_attended)
attendance_ok = attendance.has_good_attendance(att_percent)

# Show the report
print("---- Student Report ----")
print("Name:", name)
print("Grades:", student_grades)
print("Average:", round(avg, 2))
print("Letter Grade:", letter)
print("Attendance:", round(att_percent, 1), "%")
print("Good Attendance:", "Yes" if attendance_ok else "No")
