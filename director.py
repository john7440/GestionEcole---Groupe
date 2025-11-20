from dataclasses import dataclass, field
from typing import ClassVar, List

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

    courses: List['Course'] = field(default_factory=list)
    students: List['Student'] = field(default_factory=list)
    teachers: List['Teacher'] = field(default_factory=list)
    addresses: List['Address'] = field(default_factory=list)
