from abc import ABC
from dataclasses import dataclass
from typing import ClassVar, List

from Person import Person


@dataclass
class Student(Person, ABC):
    """
    Classe représentant un étudiant.
    """

    id: int
    students: ClassVar[List['Student']] = []

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}, {self.age}, {self.address}, {self.id}"

    def __repr__(self) -> str:
        return f"Student({self.firstName}, {self.lastName}, {self.age}, {self.address}, {self.id})"

    @classmethod
    def create_student(cls, student: 'Student') -> 'Student':
        """
        Ajoute un objet Student à la liste des clients.
        :param student: Instance de Student à ajouter
        :return: L'objet Student ajouté
        """
        cls.students.append(student)
        return student

    @classmethod
    def nb_students(cls) -> int:
        """
        Permet de l'affichage du nombre d' eleves passés ce jour
        :return: nombre d'eleves passés ce jour
        """
        return len(cls.students)


    @classmethod
    def print_students(cls) -> None:
        """
        Affiche la liste des eleves passés aujourd'hui
        :return: None
        """
        if not cls.students:
            print("Il n'y a aucun eleve.")
        else:
            print(f"\nListe des {Student.nb_students()} eleves passés aujourd'hui :")
            print("-" * 40)
            for i, student in enumerate(cls.students, start=1):
                print(f"{student.id_customer}. {student.firstname} {student.lastname}")
            print("-" * 40)
