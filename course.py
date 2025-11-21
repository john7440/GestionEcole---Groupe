# -*- coding: utf-8 -*-
"""Définition de la classe Course représentant un cours et les inscriptions associées."""

from datetime import date
from dataclasses import dataclass, field
from typing import List

from teacher import Teacher
from student import Student


@dataclass
class Course:
    """
    Représente un cours dans le système.

    Attributs
    ---------
    name : str
        Intitulé du cours.
    start_date : date
        Date de début du cours.
    end_date : date
        Date de fin du cours.
    teacher : Teacher
        Professeur responsable du cours.
    students : List[Student]
        Liste des étudiants inscrits à ce cours.
    """
    name: str
    start_date: date
    end_date: date
    teacher: Teacher
    students: List[Student] = field(default_factory=list)

    def __post_init__(self):
        """
        Met à jour automatiquement la liste des cours de chaque étudiant inscrit.

        Pour chaque étudiant présent dans `students', ajoute ce cours
        à l'attribut `courses` de l'étudiant s'il n'y figure pas déjà.
        """
        for student in self.students:
            if self not in student.courses:
                student.courses.append(self)

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle lisible du cours.

        Les dates sont formatées au format « YYYY-MM-DD » et
        la liste des étudiants est affichée sur plusieurs lignes.

        Returns
        -------
        str
            Description détaillée du cours incluant l'intitulé, les dates,
            le professeur et les étudiants inscrits.
        """
        # formate les dates sans les minutes et secondes
        start = self.start_date.strftime("%Y-%m-%d")
        end = self.end_date.strftime("%Y-%m-%d")

        # affiche correctement les étudiants
        if self.students:
            students_str = "\n    ".join(str(s) for s in self.students)
        else:
            students_str = "Aucun étudiant inscrit"

        return (
            f"Intitulé du cours : {self.name}\n"
            f"Début             : {start}\n"
            f"Fin               : {end}\n"
            f"Professeur        : {self.teacher}\n"
            f"Étudiants inscrits ({len(self.students)}) :\n"
            f"    {students_str}\n\n"
        )
