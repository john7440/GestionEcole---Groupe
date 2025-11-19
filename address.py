# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    zipcode: int


