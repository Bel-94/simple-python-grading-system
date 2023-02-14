def grade_calculator():
    print("Enter 'q' to quit.")
    grades = []
    total_score = 0 #this is the sum of all the scores entered
    count = 0 #the number of scores entered
    while True:
        score = input("Enter a score between 0 and 100: ")
        if score == 'q':
            break
        score = int(score) #int will change the score from string to int
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
        grades.append((score, grade)) #add the score to the list of the scores, this means each score
        total_score += score #increment the score
        count += 1 #increment the count
    
    print("\nGrades:") # This will print the name Grades in a new line
    for score, grade in grades: # this will loop through the scores entered
        print(f"Score: {score}, Grade: {grade}") #This will print the score and their grades
    
    average_score = total_score / count #This will calculate the average score
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
    print(f"\nAverage Score: {average_score}, Average Grade: {average_grade}") #This will print out the average score and the average grade
    
    print("\nGrade Summary:") #This will print out the grade summary and 
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0
    for score, grade in grades: #This will loop through the grades and print out the grade summary
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