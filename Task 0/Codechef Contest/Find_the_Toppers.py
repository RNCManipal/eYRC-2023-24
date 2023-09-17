'''
# Team ID:          < 2414 >
# Theme:            < Cosmo Logistic >
# Author List:      < Aditya Wadgaonkar,Harikishanthini K,Sujan Adiga,Tanay Srivastava >
# Filename:         < Find_the_Toppers.py >
# Functions:        < find_max_score_students,process_test_cases,main >
# Global variables: < None >
'''


def find_max_score_students(student_scores):
  """
    Find students with the maximum score from a dictionary of student scores.

    Args:
    student_scores (dict): A dictionary mapping student names to their scores.

    Returns:
    list: A sorted list of student names with the maximum score.
    """
  max_score = max(student_scores.values())
  max_score_students = [
      student for student, score in student_scores.items()
      if score == max_score
  ]
  return sorted(max_score_students)


def process_test_cases():
  """
    Process multiple test cases to find students with the highest score in each case.
    """
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


# Function Name:    main (built in)
#        Inputs:    None
#       Outputs:    None
#       Purpose:    To call the process_test_cases() function to take inputs related to program for test cases
if __name__ == "__main__":
  process_test_cases()
