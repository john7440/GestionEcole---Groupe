from dataclasses import dataclass, field
from typing import ClassVar, List
from person import Person


@dataclass
class Student(Person):
    """
    Classe représentant un étudiant.
    """
    id: int
    courses: List['Course'] = field(default_factory=list)

    def __str__(self) -> str:
        cours = ", ".join(course.name for course in self.courses) if self.courses else "Aucun cours"
        return (f"{self.firstName} {self.lastName}, {self.age} ans, "
                f"{self.address}, ID : {self.id}, Cours : {cours}")

    def __repr__(self) -> str:
        cours = [course.name for course in self.courses]
        return (f"Student({self.firstName}, {self.lastName}, {self.age}, "
                f"{self.address}, id={self.id}, cours={cours})")