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
        cls.teachers.append(teacher)
        return teacher

    @classmethod
    def nb_teachers(cls) -> int:
        """
        Permet de l'affichage du nombre d'élèves passé ce jour
        :return: nombre d'élèves passés ce jour
        """
        return len(cls.teachers)

    @classmethod
    def print_teachers(cls) -> None:
        """
        Affiche la liste des élèves passés aujourd'hui
        :return: None
        """
        if not cls.teachers:
            print("Il n'y a aucun professeur.")
        else:
            print(f"\nListe des {Teacher.nb_teachers()} professeurs :")
            print("-" * 40)
            for i, student in enumerate(cls.teachers, start=1):
                print(f"{Teacher.firstName}. {Teacher.lastName} {Teacher.age} - {Teacher.address} ans - {Teacher.arrivalDate}")
            print("-" * 40)
