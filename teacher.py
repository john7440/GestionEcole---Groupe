
from dataclasses import dataclass
from datetime import date
from person import Person
from typing import ClassVar, List

@dataclass
class Teacher(Person):
    """
    Classe représentant un professeur.
    """
    arrivalDate: date
    teachers: ClassVar[List['Teacher']] = []

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}, {self.age}, {self.address}, Arrivé le {self.arrivalDate}"

    def __repr__(self) -> str:
        return f"Teacher({self.firstName}, {self.lastName}, {self.age}, {self.address}, {self.arrivalDate})"

    @classmethod
    def create_teacher(cls, teacher: 'Teacher') -> 'Teacher':
        cls.teachers.append(teacher)
        return teacher

    @classmethod
    def nb_teachers(cls) -> int:
        return len(cls.teachers)
