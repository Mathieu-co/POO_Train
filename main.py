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
        - Retourner une chaîne lisible avec les infos du livre
        - Ajouter l'état (disponible / emprunté)
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
        TODO:
        - Vérifier si le livre est disponible
        - L'ajouter à livres_empruntes
        - Mettre livre.disponible à False
        - Gérer le cas où le livre est déjà emprunté
        """
        pass

    def rendre(self, livre: Livre) -> None:
        """
        TODO:
        - Vérifier que le membre a bien ce livre
        - Le retirer de livres_empruntes
        - Mettre livre.disponible à True
        - Gérer le cas où le livre n'est pas dans la liste
        """
        pass


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
    print(livre1.afficher_infos())


if __name__ == "__main__":
    main()
