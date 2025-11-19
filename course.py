# -*- coding: utf-8 -*-
from datetime import datetime, date
from dataclasses import dataclass


@dataclass
class Course:
    name: str
    start_date: datetime
    end_date: datetime
