#!/usr/bin/python3


class Student:
    def __init__(self, email, names, courses_registered=None, GPA=0.0):
        """
        Initialize a new Student object.

        Args:
            email (str): The email of the student.
            names (str): The names of the student.
        """
        self.email = email
        self.names = names
        self.courses_registered = courses_registered if courses_registered is not None else []
        self.GPA = GPA

    def register_for_course(self, course, grade):
        """
        Register the student for a course.

        Args:
            course (dict): A dictionary with course details (name, credits, grade).
        """
        self.courses_registered.append({
            'name': course.name,
            'credits': course.credits,
            'grade': grade
        })
        self.calculate_GPA()

    def calculate_GPA(self):
        """
        Calculate the GPA of the student.
        """
        total_credits = sum(course['credits'] for course in self.courses_registered)
        print(f"Total credits: {total_credits}")
        if total_credits == 0:
            self.GPA = 0.0
        else:
            weighted_sum = sum(course['grade'] * course['credits'] for course in self.courses_registered)
            self.GPA = weighted_sum / total_credits
        print(f"Calculated GPA: {self.GPA}")
