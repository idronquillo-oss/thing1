def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")

display_header()

def get_student_info():
    name = input("Please enter your name: ")
    a1 = int(input("Please enter your score for assessment 1: "))
    a2 = int(input("Please enter your score for assessment 2: "))
    a3 = int(input("Please enter your score for assessment 3: "))
    return name, a1, a2, a3
def evaluate_performance():

    average = (a1+a2+a3)/3
    if average < 75:
        n = "Needs Improvement"
    elif average >= 75:
        n = "Fairly Satisfactory"
    elif average >= 80:
        n = "Satisfactory"
    elif average >= 85:
        n = "Very Satisfactory"
    else:
        n = "Outstanding"
    return average, n

def display_report():
    print("STUDENT PERFORMANCE REPORT")
    print(f"Name: {name}")
    print(f"Assessment Scores: {a1}, {a2}, {a3}")
    print(f"Average score: {average:.2f}")
    print(n)


name, a1, a2, a3 = get_student_info()
average, n = evaluate_performance()
display_report()



