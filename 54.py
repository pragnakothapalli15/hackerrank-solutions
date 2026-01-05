def calculate_average_scores():
    # Read number of students and subjects
    num_students, num_subjects = map(int, input().split())

    # Read marks for each subject
    marks = [list(map(float, input().split())) for _ in range(num_subjects)]

    # Transpose marks to get student-wise scores
    student_scores = list(zip(*marks))

    # Calculate average score for each student
    average_scores = [sum(scores) / num_subjects for scores in student_scores]

    # Print average scores
    for score in average_scores:
        print(f"{score:.1f}")

if __name__ == "__main__":
    calculate_average_scores()