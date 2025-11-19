from abc import ABC
from dataclasses import dataclass
from datetime import datetime

from person import Person


@dataclass
class Teacher(Person, ABC):
    """
    Classe représentant un professeur.
    """

    arrivalDate: datetime

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}, {self.age}, {self.address}, {self.arrivalDate}"

    def __repr__(self) -> str:
        return f"Teacher({self.firstName}, {self.lastName}, {self.age}, {self.address}, {self.arrivalDate})"


    @classmethod
    def create_teacher(cls, teacher: 'Teacher') -> 'Teacher':
        """
        Ajoute un objet teacher à la liste des clients.
        :param teacher: Instance de teacher à ajouter
        :return: L'objet teacher ajouté
        """
        cls.students.append(teacher)
        return teacher

    @classmethod
    def nb_students(cls) -> int:
        """
        Permet de l'affichage du nombre d'élèves passé ce jour
        :return: nombre d'élèves passés ce jour
        """
        return len(cls.students)

    @classmethod
    def print_students(cls) -> None:
        """
        Affiche la liste des élèves passés aujourd'hui
        :return: None
        """
        if not cls.students:
            print("Il n'y a aucun eleve.")
        else:
            print(f"\nListe des {Student.nb_students()} eleves passés aujourd'hui :")
            print("-" * 40)
            for i, student in enumerate(cls.students, start=1):
                print(f"{student.id}. {student.firstName} {student.lastName} - {student.age} ans - {student.address}")
            print("-" * 40)
