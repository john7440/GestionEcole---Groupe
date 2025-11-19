#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Person:
    """
    Classe représentant une person

    Attributs :
        name : nom de la personne
        age : âge de la personne
    """

    firstName: str
    lastName: str
    age: int
    """ adress : Adress"""