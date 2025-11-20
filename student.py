from dataclasses import dataclass, field
from typing import ClassVar, List
from person import Person


@dataclass
class Student(Person):
    """
    Classe représentant un étudiant.
    """
    id: int
    students: ClassVar[List['Student']] = []
    courses: List['Course'] = field(default_factory=list)

    def __str__(self) -> str:
        cours = ", ".join(course.name for course in self.courses) if self.courses else "Aucun cours"
        return (f"{self.firstName} {self.lastName}, {self.age} ans, "
                f"{self.address}, ID : {self.id}, Cours : {cours}")

    def __repr__(self) -> str:
        cours = [course.name for course in self.courses]
        return (f"Student({self.firstName}, {self.lastName}, {self.age}, "
                f"{self.address}, id={self.id}, cours={cours})")

    # --- Gestion des étudiants ---
    @classmethod
    def create_student(cls, student: 'Student') -> 'Student':
        cls.students.append(student)
        return student

    @classmethod
    def nb_students(cls) -> int:
        return len(cls.students)

    @classmethod
    def print_students(cls) -> None:
        if not cls.students:
            print("Il n'y a aucun eleve.")
        else:
            print(f"\nListe des {Student.nb_students()} eleves passés aujourd'hui :")
            print("-" * 40)
            for i, student in enumerate(cls.students, start=1):
                print(f"{student.id}. {student.firstName} {student.lastName} - {student.age} ans - {student.address}")
            print("-" * 40)

    # --- Gestion de l'inscription au cours ---
    def enroll_in_course(self, course: 'Course'):
        """Inscrit l'étudiant à un cours."""
        if course not in self.courses:
            self.courses.append(course)
            if self not in course.students:
                course.students.append(self)
