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

    def __str__(self) -> str:
        return (f"Intitulé du cours : {self.name}, début : {self.start_date}, fin : {self.end_date}, "
                f"professeur :{self.teacher}, étudiants inscrits:{self.students} ")

