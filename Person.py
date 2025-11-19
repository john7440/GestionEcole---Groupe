#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Person:
    """
    Classe représentant une person

    Attributs :
        firstName : prénom de la personne
        lastName : nom de la personne
        age : âge de la personne
        adress : adresse de la personne
    """

    firstName: str
    lastName: str
    age: int
    """ adress : Adress"""


    def __str__(self) -> str:
        """
        Permet de configurer l'affichage d'une personne peu importe son ty
        :return: Prenom, nom ,age et adresse de la personne
        """
        return f"{self.firstName} {self.lastName} {self.age}"