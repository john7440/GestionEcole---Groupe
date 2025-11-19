#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass

from address import Address


@dataclass
class Person:
    """
    Classe représentant une person

    Attributs :
        firstName : prénom de la personne
        lastName : nom de la personne
        age : âge de la personne
        address : adresse de la personne
    """

    firstName: str
    lastName: str
    age: int
    address: Address

    def __str__(self) -> str:
        """
        Permet de configurer l'affichage d'une personne peu importe son ty
        :return: Prenom, nom, age et adresse de la personne
        """
        return f"{self.firstName} {self.lastName} {self.age} {self.address}"

    def __repr__(self) -> str:
        """
        Permet de configurer l'affichage d'une personne pour le développement
        :return: Prenom, nom, age et adresse de la personne
        """
        return f"Person({self.firstName} {self.lastName} {self.age} {self.address})"
