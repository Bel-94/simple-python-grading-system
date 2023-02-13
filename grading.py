def grade_calculator():
    print("Enter 'q' to quit.")
    grades = []
    total_score = 0
    count = 0
    while True:
        score = input("Enter a score between 0 and 100: ")
        if score == 'q':
            break
        score = int(score)
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades.append((score, grade))
        total_score += score
        count += 1
    
    print("\nGrades:")
    for score, grade in grades:
        print(f"Score: {score}, Grade: {grade}")
    
    average_score = total_score / count
    if average_score >= 90:
        average_grade = 'A'
    elif average_score >= 80:
        average_grade = 'B'
    elif average_score >= 70:
        average_grade = 'C'
    elif average_score >= 60:
        average_grade = 'D'
    else:
        average_grade = 'F'
    print(f"\nAverage Score: {average_score}, Average Grade: {average_grade}")
    
    print("\nGrade Summary:")
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0
    for score, grade in grades:
        if grade == 'A':
            a_count += 1
        elif grade == 'B':
            b_count += 1
        elif grade == 'C':
            c_count += 1
        elif grade == 'D':
            d_count += 1
        else:
            f_count += 1
    print(f"A: {a_count}")
    print(f"B: {b_count}")
    print(f"C: {c_count}")
    print(f"D: {d_count}")
    print(f"F: {f_count}")

grade_calculator()