# -*- coding: utf-8 -*-
"""Définition de la classe Address représentant une adresse et les personnes qui y habitent."""

from dataclasses import dataclass, field
from typing import List
import person


@dataclass
class Address:
    """
    Représente une adresse postale.

    Attributs
    ---------
    street : str
        Rue et numéro de l'adresse.
    city : str
        Ville.
    zipcode : str
        Code postal.
    persons_list : List[person]
        Liste des personnes associées à cette adresse.
    """
    street: str
    city: str
    zipcode: str
    persons_list: List[person] = field(default_factory=list)

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle de l'adresse.

        La chaîne retournée contient d'abord la liste des personnes
        (prénom et nom séparés par une virgule), suivie de l'adresse
        complète (rue, ville, code postal).

        Returns
        -------
        str
            Description textuelle de l'adresse et des personnes associées.
        """
        returned_string: str = ""
        for p in self.persons_list:
            returned_string += p.firstName + " " + p.lastName + ", "

        returned_string += f"{self.street}, {self.city}, {self.zipcode}"
        return returned_string
