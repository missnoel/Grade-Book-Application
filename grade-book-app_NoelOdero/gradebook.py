#!/usr/bin/python3

import json
from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        """
        Initialize a new GradeBook object with empty lists for students and courses.
        """
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        """
        Add a new student to the grade book.

        Args:
            email (str): The email of the student.
            names (str): The names of the student.
        """
        student = Student(email, names)
        self.student_list.append(student)
        self.save_students()

    def add_course(self, name, trimester, credits):
        """
        Add a new course to the grade book.

        Args:
            name (str): The name of the course.
            trimester (str): The trimester of the course.
            credits (int): The number of credits for the course.
        """
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        self.save_courses()

    def register_student_for_course(self, student_email, course_name, grade):
        """
        Register a student for a course.

        Args:
            student_email (str): The email of the student.
            course_name (str): The name of the course.
        """
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            self.save_students()
        else:
            print("Student or course not found.")
    def calculate_ranking(self):
        """
        Calculate the ranking of students based on their GPA.

        Returns:
            list: A list of students sorted by GPA in descending order.
        """
        for student in self.student_list:
            student.calculate_GPA()
        sorted_students = sorted(self.student_list, key=lambda s: s.GPA, reverse=True)
        return sorted_students

    def search_by_grade(self, min_grade, max_grade):
        """
        Search for students within a specified GPA range.

        Args:
            min_grade (float): The minimum GPA.
            max_grade (float): The maximum GPA.

        Returns:
            list: A list of students whose GPA falls within the specified range.
        """
        students_in_range = [s for s in self.student_list if min_grade <= s.GPA <= max_grade]
        return students_in_range

    def view_students(self):
        """
        Display a list of all students.
        """
        if not self.student_list:
            print("No students found.")
            return

        print("List of Students:")
        for student in self.student_list:
            print(f"Email: {student.email}, Name: {student.names}, GPA: {student.GPA}")

    def generate_transcript(self, student_email):
        """
        Generate a transcript for a specific student.

        Args:
            student_email (str): The email of the student.
        """
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            student.calculate_GPA()
            print(f"Transcript for {student.names} ({student.email}):")
        
            for course in student.courses_registered:
                print(f"{course['name']} - Grade: {course['grade']}, Credits: {course['credits']}")
            print(f"GPA: {student.GPA}")
        else:
            print("Student not found.")

    def save_students(self):
        """
        Save the student data to a JSON file.
        """
        with open('data/students.json', 'w') as f:
            json.dump([s.__dict__ for s in self.student_list], f, indent=4)

    def save_courses(self):
        """
        Save the course data to a JSON file.
        """
        with open('data/courses.json', 'w') as f:
            json.dump([c.__dict__ for c in self.course_list], f, indent=4)

    def load_students(self):
        """
        Load the student data from a JSON file.
        """
        try:
            with open('data/students.json', 'r') as f:
                students_data = json.load(f)
                self.student_list = [Student(**data) for data in students_data]

                for student in self.student_list:
                    student.calculate_GPA()
        except (FileNotFoundError, json.JSONDecodeError):
            self.student_list = []

    def load_courses(self):
        """
        Load the course data from a JSON file.
        """
        try:
            with open('data/courses.json', 'r') as f:
                courses_data = json.load(f)
                self.course_list = [Course(**data) for data in courses_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.course_list = []
