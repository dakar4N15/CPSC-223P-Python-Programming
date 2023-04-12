# Name: William Sutanto
# Date: 4/5/2023
# File Purpose: Lab 08 main file

#Import the Faculty and Student classes from the people module.
from people import *

#Declare a variable to hold a list of faculty.
faculty_list = []
#Declare a variable to hold a list of students.
students_list = []

exit = False    #loop controler

while(exit == False):
    #output menu choices
    print("\n      *** TUFFY TITAN STUDENT/FACULTY MAIN MENU\n")
    print("1. Add faculty")
    print("2. Print faculty")
    print("3. Add student")
    print("4. Print student")
    print("9. Exit the program\n")
    
    #prompt the user for menu choice and call the appropriate people function or exit
    user_input = input("Enter menu choice: ")
    
    if(user_input == "1"):
        first_name = input("\nEnter first name: ")
        last_name = input("Enter last name: ")
        department = input("Enter department: ")
        new_faculty = Faculty(first_name, last_name, department)
        faculty_list.append(new_faculty)

    elif(user_input == "2"):
        print("\n======================= FACULTY =======================")
        print("Record  Name                  Department")
        print("======  ====================  =========================")
        for i, faculty in enumerate(faculty_list):
            print(f'{i:<7} {faculty.firstname + " " + faculty.lastname:<21} {faculty.department}')
    
    elif(user_input == "3"):
        first_name = input("\nEnter first name: ")
        last_name = input("Enter last name: ")
        class_year = input("Enter class year: ")
        major = input("Enter major: ")
        faculty = input("Enter faculty advisor: ")
        advisor = faculty_list[int(faculty)]
        new_student = Student(first_name, last_name)
        new_student.set_class(class_year)
        new_student.set_major(major)
        new_student.set_advisor(advisor)
        students_list.append(new_student)

    elif(user_input == "4"):
        print("\n===================================== STUDENTS ======================================")
        print("Name                  Class      Major                      Advisor")
        print("====================  ========   =========================  =========================")
        for i, student in enumerate(students_list):
            print(f'{student.firstname + " " + student.lastname:<21} {student.classyear:<10} {student.major:<26} {student.advisor.firstname} {student.advisor.lastname}')
        
    elif(user_input == "9"):
        exit = True
    else:
        print("Invalid choice!")

