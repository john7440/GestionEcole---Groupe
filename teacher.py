
from dataclasses import dataclass
from datetime import datetime
from person import Person
from typing import ClassVar, List

@dataclass
class Teacher(Person):
    """
    Classe représentant un professeur.
    """
    arrivalDate: datetime
    teachers: ClassVar[List['Teacher']] = []

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}, {self.age}, {self.address}, {self.arrivalDate}"

    def __repr__(self) -> str:
        return f"Teacher({self.firstName}, {self.lastName}, {self.age}, {self.address}, {self.arrivalDate})"

    @classmethod
    def create_teacher(cls, teacher: 'Teacher') -> 'Teacher':
        cls.teachers.append(teacher)
        return teacher

    @classmethod
    def nb_teachers(cls) -> int:
        return len(cls.teachers)

    @classmethod
    def print_teachers(cls) -> None:
        if not cls.teachers:
            print("Il n'y a aucun professeur.")
        else:
            print(f"\nListe des {cls.nb_teachers()} professeurs :")
            print("-" * 40)
            for i, teacher in enumerate(cls.teachers, start=1):
                print(f"{i}. {teacher.firstName} {teacher.lastName} - {teacher.age} ans - {teacher.address} - Arrivé le {teacher.arrivalDate}")
            print("-" * 40)
