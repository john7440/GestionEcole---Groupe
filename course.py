# -*- coding: utf-8 -*-
from datetime import datetime, date
from dataclasses import dataclass, field
from typing import List

from teacher import Teacher
from student import Student


@dataclass
class Course:
    name: str
    start_date: datetime
    end_date: datetime
    teacher: Teacher
    students: List[Student] = field(default_factory=list)