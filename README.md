# 📚 Application de Gestion Scolaire

Cette application est le fruit d'une collaboration avec Rafael Da Silva, Rémi Campistron, Rafaël Ducasse et Théo Sarhane. Elle permet de gérer les enseignants et les cours au sein d’un établissement scolaire.  
Elle propose des fonctionnalités adaptées à trois profils : **Directeur**, **Élève**, et **Enseignant**.

---

## 👨‍💼 Pour le Directeur

### Gestion des élèves
- ➕ Ajouter un élève à la liste des élèves  
- 📋 Afficher la liste des élèves  
- 🔍 Consulter le détail d’un élève : identité, âge, adresse  
- ✏️ Modifier un élève : mettre à jour ses informations (nom, prénom, âge, adresse, etc.)  
- 🗑️ Supprimer un élève de la liste  
- ✅ Valider l’inscription d’un élève

### Gestion des enseignants
- 📋 Afficher la liste des enseignants : prénom, nom, âge, date d’arrivée, adresse  
- 🔍 Consulter le détail d’un enseignant : identité, adresse, date d’arrivée, liste des cours  
- ➕ Ajouter un enseignant : saisir prénom, nom, âge, adresse, date d’arrivée  
- ✏️ Modifier un enseignant : mettre à jour ses informations  
- 🗑️ Supprimer un enseignant  

### Gestion des cours
- 📋 Afficher la liste des cours : dénomination, date de début, date de fin, enseignant responsable  
- 🔍 Consulter le détail d’un cours : dénomination, dates, enseignant, liste des élèves inscrits  
- ➕ Ajouter un cours : dénomination, date de début, date de fin, enseignant assigné  
- ✏️ Modifier un cours : mettre à jour la dénomination, les dates, l’enseignant assigné  
- 🗑️ Supprimer un cours  

---

## 🎓 Pour l’Élève

- 📝 Faire une demande d’inscription : saisir prénom, nom, âge, adresse  
  - La demande est enregistrée comme **« en attente »**  
  - Le directeur valide ou refuse la demande  
- 📋 Consulter la liste des cours proposés : dénomination, dates, enseignant responsable  

---

## 👨‍🏫 Pour l’Enseignant

- 📋 Afficher les élèves d’un cours : dénomination, dates de début et de fin  
- 📋 Consulter la liste des cours auxquels il est assigné : dénomination, dates de début et de fin  

---

## 🚀 Installation & Utilisation

1. Clonez le projet :  
   ```bash
    git clone https://github.com/john7440/GestionEcole---Groupe.git
