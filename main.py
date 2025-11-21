# test_students.py
# -*- coding: utf-8 -*-
from datetime import datetime, date

from address import Address
from student import Student
from teacher import Teacher
from course import Course   # <-- Manquait dans ton code


def test_create_students():
    """Crée des étudiants et les renvoie."""

    # Création des adresses
    address1 = Address(street="123 Rue de Paris", city="Paris", zipcode="75001")
    address2 = Address(street="45 Avenue de Lyon", city="Lyon", zipcode="69000")
    address3 = Address(street="78 Boulevard Saint-Germain", city="Paris", zipcode="75005")

    # Création des étudiants
    student1 = Student(firstName="Alice", lastName="Dupont", age=20, address=address1, id=1)
    student2 = Student(firstName="Bob", lastName="Martin", age=22, address=address2, id=2)
    student3 = Student(firstName="Charlie", lastName="Durand", age=21, address=address3, id=3)

    return [student1, student2, student3]


def test_create_teachers():
    """Crée des professeurs et les renvoie."""

    # Création des adresses
    address1 = Address(street="123 Rue de Paris", city="Paris", zipcode="75001")
    address2 = Address(street="45 Avenue de Lyon", city="Lyon", zipcode="69000")
    address3 = Address(street="78 Boulevard Saint-Germain", city="Paris", zipcode="75005")

    # Création des professeurs avec jour/mois/année
    teacher1 = Teacher(firstName="Pierre", lastName="Dupont", age=40, address=address1,
                       arrivalDate=date(2020, 2, 10))
    teacher2 = Teacher(firstName="Martin", lastName="Dumoulin", age=35, address=address2,
                       arrivalDate=date(2015, 4, 10))
    teacher3 = Teacher(firstName="Sandra", lastName="Dupré", age=30, address=address3,
                       arrivalDate=date(2023, 5, 17))

    return [teacher1, teacher2, teacher3]


def test_create_courses(teachers, students):
    """Crée des cours et les renvoie."""

    teacher1, teacher2, teacher3 = teachers
    student1, student2, student3 = students

    course1 = Course(
        name="Algèbre avancée",
        start_date=datetime(2025, 2, 1),
        end_date=datetime(2025, 6, 30),
        teacher=teacher1,
        students=[student1, student2, student3]
    )

    course2 = Course(
        name="Introduction à la programmation",
        start_date=datetime(2025, 3, 1),
        end_date=datetime(2025, 7, 31),
        teacher=teacher2,
        students=[student1, student3]
    )

    course3 = Course(
        name="Physique fondamentale",
        start_date=datetime(2025, 4, 1),
        end_date=datetime(2025, 8, 31),
        teacher=teacher3,
        students=[student2]
    )

    return [course1, course2, course3]


if __name__ == "__main__":
    print("\n--- Création des étudiants ---\n")
    student_list = test_create_students()
    for student in student_list:
        print(student)

    print("\n--- Création des professeurs ---\n")
    teacher_list = test_create_teachers()
    for teacher in teacher_list:
        print(teacher)

    print("\n--- Création des cours ---\n")
    course_list = test_create_courses(teacher_list, student_list)
    for course in course_list:
        print(course)
