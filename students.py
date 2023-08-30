"""Read the student file
put the student name & page view in dic
sort based on the page view 
print a file list of student with page view less than 100
separate first name and last name."""

import csv

#reading the csv file:
with open('student.csv', 'r+') as studentfile:
    data=studentfile.readlines()
 
    #put the student name & page view in dic
    student = {}
    for line in data:
        parts = line.strip().split(',')
        student_name = parts[0]
        page_views = parts[9]
        student[student_name] = page_views
        
# print(student)

    #sort based on the page view 
    sorted_students = sorted(student.items(), key=lambda x: x[1])
    print(sorted_students)

    # #print a file list of student with page view less than 100
    # for student in sorted_students:
    #     if student[1] < 100:
    #         print(student[0])
    
    #separate first name and last name.

    for student in sorted_students:
        if student[1]=='-':
            # student[1]=0, cant do this because it is a tuple
            pass
        else:
            if int(student[1]) < 100:
                first_name, last_name = student[0].split()
                print("First Name:", first_name, "Last Name:", last_name)

