from abc import ABC
from dataclasses import dataclass
from Person import Person


@dataclass
class Student(Person, ABC):
    """
    Classe représentant un étudiant.
    """

    id: int

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}, {self.age}, {self.address}, {self.id}"

    def __repr__(self) -> str:
        return f"Student({self.firstName}, {self.lastName}, {self.age}, {self.address}, {self.id})"
