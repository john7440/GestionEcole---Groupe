from abc import ABC
from dataclasses import dataclass
from xmlrpc.client import DateTime

from Person import Person


@dataclass
class Teacher(Person, ABC):
    """
    Classe représentant un professeur.
    """

    arrivalDate: DateTime

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}, {self.age}, {self.address}, {self.arrivalDate}"

    def __repr__(self) -> str:
        return f"Teacher({self.firstName}, {self.lastName}, {self.age}, {self.address}, {self.arrivalDate})"
