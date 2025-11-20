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
