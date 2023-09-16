
def find_max_score_students(student_scores):
    max_score = max(student_scores.values())
    max_score_students = [student for student, score in student_scores.items() if score == max_score]
    return sorted(max_score_students)

def process_test_cases():
    t = int(input())  

    for _ in range(t):
        n = int(input())  
        student_scores = {}  

        for _ in range(n):
            student_name, score = input().split()
            score = int(score)
            student_scores[student_name] = score

        max_score_students = find_max_score_students(student_scores)
        for student in max_score_students:
            print(student)


if __name__ == "__main__":
    process_test_cases()
