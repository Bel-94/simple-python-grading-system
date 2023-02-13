def grade_calculator():
    print("Enter 'q' to quit.")
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
        print(f"Score: {score}, Grade: {grade}") 

grade_calculator()