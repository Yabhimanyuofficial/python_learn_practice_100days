student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_exam_scores = 0
for score in student_scores:
    total_exam_scores += score

print(f"The total of all the exam scores is: {total_exam_scores}")
total_exam_scores = sum(student_scores)
print(total_exam_scores)