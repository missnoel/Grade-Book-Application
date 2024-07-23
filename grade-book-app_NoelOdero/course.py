#!/usr/bin/python3

class Course:
    def __init__(self, name, trimester,credits):
        """
        Initialize a Course object.

        name param: The name of the course.
        trimester param: The trimester in which the course is offered.
        credits param: The number of credits for the course.
        """
        self.name = name
        self.trimester = trimester
        self.credits = credits

