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

    def __str__(self) -> str:
        returned_string: str = ""
        for p in self.persons_list:
            returned_string += p.firstName + " " + p.lastName + ", "

        returned_string += f"{self.street}, {self.city}, {self.zipcode}"
        return returned_string

