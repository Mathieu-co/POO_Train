"""
Exercice POO - Gestion de bibliothèque

Objectif:
- Manipuler des classes simples
- Gérer des relations entre objets
- Implémenter progressivement la logique métier
"""


class Livre:
    """Représente un livre dans la bibliothèque."""

    def __init__(self, titre: str, auteur: str, isbn: str) -> None:
        # Attributs de base du livre
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

        # Indique si le livre peut être emprunté
        self.disponible = True

    def afficher_infos(self) -> str:
        """
        - Retourne une chaîne lisible avec les infos du livre
        - Ajoute l'état (disponible / emprunté)
        """
        if self.disponible:
            etat = "Disponible"

        else:
            etat = "Emprunté"
        return f"Titre : {self.titre}\nAuteur : {self.auteur}\nISBN : {self.isbn}\nÉtat : {etat}"


class Membre:
    """Représente une personne inscrite à la bibliothèque."""

    def __init__(self, identifiant: int, nom: str) -> None:
        self.identifiant = identifiant
        self.nom = nom

        # Liste des livres actuellement empruntés par ce membre
        self.livres_empruntes = []

    def emprunter(self, livre: Livre) -> None:
        """
        - Vérification si le livre est disponible
        - On ajoute à livres_empruntes
        - Disponibilité du livre change
        - Le cas où le livre est déjà emprunté est géré
        """
        if livre in self.livres_empruntes:
            print(f"Vous avez déjà emprunté le livre {livre.titre}.")
            return

        if not livre.disponible:
            print(f"Le livre {livre.titre} est indisponible.")
            return

        self.livres_empruntes.append(livre)
        livre.disponible = False

    def rendre(self, livre: Livre) -> None:
        """
        - Vérifier que le membre a bien ce livre
        - Le retirer de livres_empruntes
        - Mettre livre.disponible à True
        - Gérer le cas où le livre n'est pas dans la liste
        """
        if livre not in self.livres_empruntes:
            print(f"Vous n'avez pas emprunté le livre {livre.titre}")
            return

        self.livres_empruntes.remove(livre)
        livre.disponible = True


class Bibliotheque:
    """Classe principale qui orchestre livres et membres."""

    def __init__(self, nom: str) -> None:
        self.nom = nom
        self.catalogue = []  # Liste de Livre
        self.membres = []  # Liste de Membre

    def ajouter_livre(self, livre: Livre) -> None:
        """
        TODO:
        - Ajouter le livre au catalogue
        - Option bonus: éviter les doublons d'ISBN
        """
        pass

    def inscrire_membre(self, membre: Membre) -> None:
        """
        TODO:
        - Ajouter le membre à la liste des membres
        - Option bonus: empêcher deux identifiants identiques
        """
        pass

    def trouver_livre_par_isbn(self, isbn: str) -> Livre | None:
        """
        TODO:
        - Parcourir le catalogue
        - Retourner le livre correspondant ou None
        """
        pass

    def afficher_catalogue(self) -> None:
        """
        TODO:
        - Afficher les informations de chaque livre
        - Utiliser la méthode afficher_infos de Livre
        """
        pass


def main() -> None:
    """
    Zone de test progressive.

    Étapes suggérées:
    1) Créer 2 livres
    2) Créer 1 membre
    3) Ajouter les livres à la bibliothèque
    4) Tester emprunt puis retour
    """
    livre1 = Livre("1984", "George Orwell", "12345")
    livre2 = Livre("Dune", "Frank Herbert", "67890")

    membre1 = Membre(1, "Alice")
    membre2 = Membre(2, "Bob")

    print("=== État initial ===")
    print(livre1.afficher_infos())
    print()
    print(livre2.afficher_infos())
    print()

    print("=== Emprunt par Alice ===")
    membre1.emprunter(livre1)
    print(livre1.afficher_infos())
    print(
        "Livres empruntés par Alice :",
        [livre.titre for livre in membre1.livres_empruntes],
    )
    print()

    print("=== Alice emprunte le même livre ===")
    membre1.emprunter(livre1)
    print(livre1.afficher_infos())
    print()

    print("=== Bob emprunt un autre livre ===")
    membre2.emprunter(livre2)
    print(livre2.afficher_infos())
    print(
        "Livres emprunté par Bob :", [livre.titre for livre in membre2.livres_empruntes]
    )
    print()

    print("=== Alice rend son livre ===")
    membre1.rendre(livre1)
    print(livre1.afficher_infos())
    print(
        "Livres empruntés par Alice :",
        [livre.titre for livre in membre1.livres_empruntes],
    )
    print()

    print("=== Alice essaie encore de rendre le même livre ===")
    membre1.rendre(livre1)
    print()

    print("=== Bob essaie de rendre le livre qu'il n'a pas ===")
    membre2.rendre(livre1)
    print()


if __name__ == "__main__":
    main()
