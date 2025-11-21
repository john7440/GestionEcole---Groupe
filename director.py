from dataclasses import dataclass, field
from typing import List

from person import Person
from course import Course
from student import Student
from teacher import Teacher
from address import Address


@dataclass
class Director(Person):
    """
    Classe représentant un directeur.
    """

    courses: List[Course] = field(default_factory=list)
    students: List[Student] = field(default_factory=list)
    teachers: List[Teacher] = field(default_factory=list)
    addresses: List[Address] = field(default_factory=list)

    # --- Gestion des étudiants ---
    def add_student(self, student: Student):
        """Ajoute un étudiant au directeur s'il n'est pas déjà présent."""
        if student not in self.students:
            self.students.append(student)
        else:
            print(f"L'étudiant {student.firstName} {student.lastName} est déjà enregistré.")

    def remove_student(self, student: Student):
        """Supprime un étudiant du directeur s'il est présent."""
        if student in self.students:
            self.students.remove(student)
        else:
            print(f"L'étudiant {student.firstName} {student.lastName} n'est pas enregistré.")

    def remove_course(self, course: Course):
        """Supprime un cours s'il existe """
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"Le cours {course.name} n'est pas enregistré.")

    def remove_teacher(self, teacher: Teacher):
        """Supprime un professeur s'il existe """
        if teacher in self.teachers:
            self.teachers.remove(teacher)
        else:
            print(f"Le professeur {teacher.firstName} {teacher.lastName} n'est pas enregistré.")