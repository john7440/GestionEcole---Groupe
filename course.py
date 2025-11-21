# -*- coding: utf-8 -*-
from datetime import datetime, date
from dataclasses import dataclass, field
from typing import List

from teacher import Teacher
from student import Student


@dataclass
class Course:
    name: str
    start_date: date
    end_date: date
    teacher: Teacher
    students: List[Student] = field(default_factory=list)

    def __post_init__(self):
        for student in self.students:
            if self not in student.courses:
                student.courses.append(self)

    def __str__(self) -> str:
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


