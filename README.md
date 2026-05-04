# Exercice POO — Gestion d'une bibliothèque (Python)

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

## 🧱 Classes

Le fichier `main.py` contient 3 classes principales :

### `Livre`

Représente un livre avec :

- `titre`
- `auteur`
- `isbn`
- `disponible` (booléen)

La méthode `afficher_infos()` retourne un résumé lisible du livre.

### `Membre`

Représente un membre de la bibliothèque avec :

- `identifiant`
- `nom`
- `livres_empruntes` (liste de `Livre`)

Méthodes :

- `emprunter(livre)`
- `rendre(livre)`

### `Bibliotheque`

Représente la bibliothèque avec :

- `nom`
- `catalogue` (liste de `Livre`)
- `membres` (liste de `Membre`)

Méthodes :

- `ajouter_livre(livre)`
- `inscrire_membre(membre)`
- `trouver_livre_par_isbn(isbn)`
- `afficher_catalogue()`

## ▶️ Lancer le projet

Prérequis : Python 3.10+ (le code utilise `Livre | None`).

```bash
python main.py
```

Des tests de typage, cohérence et de structure sont exécutés dans `main()`.

## 📌 Idée d'amélioration

On peut séparé le projet en modules :

- `models/livre.py`
- `models/membre.py`
- `models/bibliotheque.py`
- `main.py`