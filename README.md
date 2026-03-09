# Exercice POO — Gestion de bibliothèque (Python)

Petit projet d'entraînement pour pratiquer la **programmation orientée objet (POO)** en Python à partir d'un cas concret : la gestion d'une bibliothèque.

## 🎯 Objectifs pédagogiques

Ce projet permet de travailler :

- la création de classes et d'objets ;
- la gestion d'attributs et de méthodes ;
- les relations entre objets (bibliothèque, membres, livres) ;
- l'implémentation progressive d'une logique métier simple ;
- les bonnes pratiques de test manuel dans une fonction `main()`.

## 📁 Structure du projet

- `main.py` : contient tout le squelette de l'exercice (classes + zone de test).
- `README.md` : consignes et guide de progression.

## 🧱 Classes à compléter

Le fichier `main.py` contient 3 classes principales :

### `Livre`

Représente un livre avec :

- `titre`
- `auteur`
- `isbn`
- `disponible` (booléen)

La méthode `afficher_infos()` est déjà fournie et retourne un résumé lisible du livre.

### `Membre`

Représente un membre de la bibliothèque avec :

- `identifiant`
- `nom`
- `livres_empruntes` (liste de `Livre`)

Méthodes à implémenter :

- `emprunter(livre)`
- `rendre(livre)`

### `Bibliotheque`

Représente la bibliothèque avec :

- `nom`
- `catalogue` (liste de `Livre`)
- `membres` (liste de `Membre`)

Méthodes à implémenter :

- `ajouter_livre(livre)`
- `inscrire_membre(membre)`
- `trouver_livre_par_isbn(isbn)`
- `afficher_catalogue()`

## ▶️ Lancer le projet

Prérequis : Python 3.10+ (le code utilise `Livre | None`).

```bash
python main.py
```

À ce stade, seul un test minimal est exécuté dans `main()`.

## ✅ Plan de progression conseillé

1. Implémenter `Membre.emprunter`.
2. Implémenter `Membre.rendre`.
3. Implémenter `Bibliotheque.ajouter_livre`.
4. Implémenter `Bibliotheque.inscrire_membre`.
5. Implémenter `Bibliotheque.trouver_livre_par_isbn`.
6. Implémenter `Bibliotheque.afficher_catalogue`.
7. Enrichir `main()` avec des scénarios de test.

## 🧪 Exemples de scénarios à tester

- Emprunt d'un livre disponible ✅
- Emprunt d'un livre déjà emprunté ❌
- Retour d'un livre emprunté ✅
- Retour d'un livre non emprunté par le membre ❌
- Recherche d'un livre existant par ISBN ✅
- Recherche d'un ISBN inexistant ❌

## 💡 Bonus (facultatif)

- Empêcher l'ajout de deux livres avec le même ISBN.
- Empêcher l'inscription de deux membres avec le même identifiant.
- Ajouter des messages utilisateur clairs (`print`) pour chaque action.
- Ajouter des tests unitaires (`unittest` ou `pytest`).

## 📌 Idée d'amélioration

Quand l'exercice de base est terminé, vous pouvez séparer le projet en modules :

- `models/livre.py`
- `models/membre.py`
- `models/bibliotheque.py`
- `main.py`

Cela vous préparera à des projets Python plus structurés.
