#!/usr/bin/python3



from gradebook import GradeBook
from course import Course
from student import Student

def display_menu():

    """
    Display the main menu for the Grade Book Application.
    """
    print("\nThis is The Grade Book Application, Welcome! 😊")
    print("Thou shall reap what thou sowed 🥱")
    print("\nKindly select an action")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Register Student for Course")
    print("4. Calculate Ranking")
    print("5. Search by Grade")
    print("6. Generate Transcript")
    print("7. View list of students")
    print("8. Exit")

def main():

    """
    Main function to run the Grade Book Application.
    """

    # Create an instance of the GradeBook class
    gradebook = GradeBook()

     # Load existing students and courses from files
    gradebook.load_students()
    gradebook.load_courses()


    while True:
        # Display the menu and get user's choice
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            print("\nThe quest for grades has a new champion! Student record successfully created 😊")


        elif choice == 2:

            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            try:
                credits = float(input("Enter credits: "))
            except ValueError:
                print("Invalid input. Please enter a valid number for credits.")
                continue
            gradebook.add_course(name, trimester, credits)
            print("\nThe course record has been successfully added to the system.")
        
        elif choice == 3:
            # Register a student for a course
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            try:
                grade = float(input(f"Enter grade for {course_name}: "))
            except ValueError:
                print("Invalid input. Please enter a valid number for grade.")
                continue
            print(f"\nRegistering student {student_email} for course {course_name} with grade {grade}")
            gradebook.register_student_for_course(student_email, course_name, grade)
            print("\nStudent registered for the course successfully!")
        
        elif choice == 4:
            print("\nCalculating student rankings...")
            # Calculate and display student rankings based on GPA
            ranking = gradebook.calculate_ranking()
            print("Student Rankings:")
            for idx, student in enumerate(ranking):
                print(f"{idx + 1}. {student.email} (GPA: {student.GPA})")
            print("\nStudent ranking calculated successfully")
            

        elif choice == 5:
            # Search for students within a specified GPA range
            try:
                min_grade = float(input("Enter minimum grade: "))
                max_grade = float(input("Enter maximum grade: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers for grades.")
                continue
            print(f"Searching students with GPA between {min_grade} and {max_grade}")
            students_in_range = gradebook.search_by_grade(min_grade, max_grade)
            print("Students in Grade Range:")
            for student in students_in_range:
                print(f"{student.email} - GPA: {student.GPA}")
            print("\nStudent registered for the course successfully!")

        elif choice == 6:
            # Generate and display a transcript for a specific student
            student_email = input("Enter student email: ")
            gradebook.generate_transcript(student_email)

        elif choice == 7:
            # View list of students
            gradebook.view_students()


        elif choice == 8:
            # Exit the application
            print("\nExiting the application. Bye!\n")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
