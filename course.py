# -*- coding: utf-8 -*-
from datetime import datetime, date
from dataclasses import dataclass
from Teacher import Teacher


@dataclass
class Course:
    name: str
    start_date: datetime
    end_date: datetime
    teacher: Teacher
