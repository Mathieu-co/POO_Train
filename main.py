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
        self.catalogue: list[Livre] = []  # Liste de Livre
        self.membres: list[Membre] = []  # Liste de Membre

    def ajouter_livre(self, livre: Livre) -> None:
        """
        - Ajout d'un livre au catalogue
        - On évite les doublons d'ISBN
        - On vérifie que l'objet est bien un Livre
        """
        if not isinstance(livre, Livre):
            raise TypeError("livre doit être une instance de Livre")

        for livre_existant in self.catalogue:
            if livre_existant.isbn == livre.isbn:
                raise ValueError(
                    f"Le livre {livre.titre}  ISBN {livre.isbn} est déjà présent dans la bibliothèque"
                )

        self.catalogue.append(livre)

    def inscrire_membre(self, membre: Membre) -> None:
        """
        - Ajout d'un membre à la liste des membres
        - On empèche deux identifiants identiques
        - On vérifie que l'objet est bien un Membre
        """
        if not isinstance(membre, Membre):
            raise TypeError("membre doit être une instance de Membre")

        for membre_existant in self.membres:
            if membre_existant.identifiant == membre.identifiant:
                raise ValueError(
                    f"Le membre {membre.nom} numéro {membre.identifiant} est déjà inscrit."
                )

        self.membres.append(membre)

    def trouver_livre_par_isbn(self, isbn: str) -> Livre | None:
        """
        - Parcourir le catalogue
        - Retourner le livre correspondant ou None
        """
        if not isinstance(isbn, str):
            raise TypeError("ISBN doit être une chaine de caractères")

        for livre in self.catalogue:
            if livre.isbn == isbn:
                return livre

        return None

    def afficher_catalogue(self) -> None:
        """
        TODO:
        - Afficher les informations de chaque livre
        - Utiliser la méthode afficher_infos de Livre
        """
        pass


def main() -> None:
    """
    Zone de test plus complète.

    L'objectif est de vérifier:
    - les créations d'objets
    - les ajouts valides
    - les recherches
    - les erreurs prévues
    - les emprunts et les retours
    """
    def afficher_section(titre: str) -> None:
        print(f"\n=== {titre} ===")

    def verifier(condition: bool, message: str) -> None:
        assert condition, message
        print(f"OK - {message}")

    def verifier_exception(
        exception_attendue: type[Exception],
        action,
        message: str,
    ) -> None:
        try:
            action()
        except exception_attendue as erreur:
            print(f"OK - {message} : {erreur}")
        else:
            raise AssertionError(f"Erreur attendue non levée : {message}")

    def titres_empruntes(membre: Membre) -> list[str]:
        return [livre.titre for livre in membre.livres_empruntes]

    bibliotheque = Bibliotheque("Bibliothèque municipale")

    livre1 = Livre("1984", "George Orwell", "12345")
    livre2 = Livre("Dune", "Frank Herbert", "67890")
    livre3 = Livre("Fondation", "Isaac Asimov", "11111")
    livre_doublon_isbn = Livre("Le Meilleur des mondes", "Aldous Huxley", "12345")

    membre1 = Membre(1, "Alice")
    membre2 = Membre(2, "Bob")
    membre_doublon_id = Membre(1, "Charlie")

    afficher_section("Création des objets")
    verifier(bibliotheque.nom == "Bibliothèque municipale", "le nom de la bibliothèque est correct")
    verifier(livre1.disponible, "un nouveau livre est disponible")
    verifier(membre1.livres_empruntes == [], "un nouveau membre ne possède aucun livre")

    afficher_section("Ajout des livres")
    for livre in [livre1, livre2, livre3]:
        bibliotheque.ajouter_livre(livre)

    verifier(len(bibliotheque.catalogue) == 3, "trois livres sont dans le catalogue")
    verifier(
        [livre.titre for livre in bibliotheque.catalogue] == ["1984", "Dune", "Fondation"],
        "les titres du catalogue sont corrects",
    )

    afficher_section("Inscription des membres")
    bibliotheque.inscrire_membre(membre1)
    bibliotheque.inscrire_membre(membre2)

    verifier(len(bibliotheque.membres) == 2, "deux membres sont inscrits")
    verifier(
        [membre.nom for membre in bibliotheque.membres] == ["Alice", "Bob"],
        "les noms des membres sont corrects",
    )

    afficher_section("Recherche par ISBN")
    verifier(
        bibliotheque.trouver_livre_par_isbn("12345") is livre1,
        "la recherche retourne le bon livre",
    )
    verifier(
        bibliotheque.trouver_livre_par_isbn("00000") is None,
        "la recherche retourne None pour un ISBN absent",
    )

    afficher_section("Erreurs attendues")
    verifier_exception(
        ValueError,
        lambda: bibliotheque.ajouter_livre(livre_doublon_isbn),
        "impossible d'ajouter deux livres avec le même ISBN",
    )
    verifier_exception(
        ValueError,
        lambda: bibliotheque.inscrire_membre(membre_doublon_id),
        "impossible d'inscrire deux membres avec le même identifiant",
    )
    verifier_exception(
        TypeError,
        lambda: bibliotheque.ajouter_livre("pas un livre"),
        "ajouter_livre refuse un objet qui n'est pas un Livre",
    )
    verifier_exception(
        TypeError,
        lambda: bibliotheque.inscrire_membre("pas un membre"),
        "inscrire_membre refuse un objet qui n'est pas un Membre",
    )
    verifier_exception(
        TypeError,
        lambda: bibliotheque.trouver_livre_par_isbn(12345),
        "trouver_livre_par_isbn refuse un ISBN qui n'est pas une chaîne",
    )

    afficher_section("Affichage des informations d'un livre")
    infos_livre1 = livre1.afficher_infos()
    print(infos_livre1)
    verifier("1984" in infos_livre1, "afficher_infos contient le titre")
    verifier("George Orwell" in infos_livre1, "afficher_infos contient l'auteur")
    verifier("Disponible" in infos_livre1, "afficher_infos indique l'état disponible")

    afficher_section("Emprunt simple")
    membre1.emprunter(livre1)
    verifier(not livre1.disponible, "le livre emprunté devient indisponible")
    verifier(
        titres_empruntes(membre1) == ["1984"],
        "le livre apparaît dans les emprunts d'Alice",
    )

    afficher_section("Emprunt du même livre par la même personne")
    membre1.emprunter(livre1)
    verifier(
        titres_empruntes(membre1) == ["1984"],
        "le livre n'est pas ajouté deux fois à Alice",
    )

    afficher_section("Emprunt d'un livre déjà pris par un autre membre")
    membre2.emprunter(livre1)
    verifier(
        titres_empruntes(membre2) == [],
        "Bob ne peut pas emprunter un livre déjà pris",
    )

    afficher_section("Emprunts multiples")
    membre1.emprunter(livre2)
    membre2.emprunter(livre3)
    verifier(
        titres_empruntes(membre1) == ["1984", "Dune"],
        "Alice peut emprunter plusieurs livres disponibles",
    )
    verifier(
        titres_empruntes(membre2) == ["Fondation"],
        "Bob peut emprunter un autre livre disponible",
    )

    afficher_section("Retour d'un livre")
    membre1.rendre(livre1)
    verifier(livre1.disponible, "le livre rendu redevient disponible")
    verifier(
        titres_empruntes(membre1) == ["Dune"],
        "le livre rendu disparaît des emprunts d'Alice",
    )

    afficher_section("Retour impossible")
    membre1.rendre(livre1)
    verifier(
        titres_empruntes(membre1) == ["Dune"],
        "rendre un livre absent ne modifie pas les emprunts d'Alice",
    )
    membre2.rendre(livre1)
    verifier(
        titres_empruntes(membre2) == ["Fondation"],
        "Bob ne peut pas rendre un livre qu'il n'a pas",
    )

    afficher_section("Ré-emprunt après retour")
    membre2.emprunter(livre1)
    verifier(not livre1.disponible, "un livre rendu peut être emprunté par un autre membre")
    verifier(
        titres_empruntes(membre2) == ["Fondation", "1984"],
        "le livre ré-emprunté apparaît chez Bob",
    )

    afficher_section("État final")
    for livre in bibliotheque.catalogue:
        print(livre.afficher_infos())
        print()

    print("Tous les tests de main() sont passés.")


if __name__ == "__main__":
    main()
