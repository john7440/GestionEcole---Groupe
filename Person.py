#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from abc import ABC, abstractmethod

from address import Address


@dataclass
class Person(ABC):
    """
    Classe représentant une personne (abstraite)

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

    @abstractmethod
    def add_address(self) -> str:
        pass

    def __str__(self) -> str:
        """
        Permet de configurer l'affichage d'une personne peu importe son type.
        """
        return f"{self.firstName} {self.lastName}, {self.age} ans, {self.address}"

    def __repr__(self) -> str:
        """
        Permet de configurer l'affichage d'une personne pour le développement.
        """
        return (f"Person({self.firstName!r}, {self.lastName!r}, "
                f"{self.age!r}, {self.address!r})")
