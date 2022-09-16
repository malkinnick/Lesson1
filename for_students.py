student_scores=[3,5,4,4,2]

avg_score=0
for score in student_scores:
    avg_score = avg_score + score

class_avg=avg_score/len(student_scores)
print(class_avg)