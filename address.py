# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import List,Dict
import person

@dataclass
class Address:
    street: str
    city: str
    zipcode: int
    persons_list: List[person] = field(default_factory=list)

