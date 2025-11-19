# -*- coding: utf-8 -*-
from datetime import datetime, date
from dataclasses import dataclass, field
from typing import List

from Teacher import Teacher
from Student import Student


@dataclass
class Course:
    name: str
    start_date: datetime
    end_date: datetime
    teacher: Teacher
    students: List[Student] = field(default_factory=list)