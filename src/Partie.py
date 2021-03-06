"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

# TODO: penser à faire les tests unitaires sur les classes et méthodes
import time


class Jeu(object):
    """Classe qui met en place les parties immuables du jeu pour ensuite être utilisé dans chaque partie."""

    def __init__(self):
        """Définit les éléments immuables du jeu classique.
        ---
        Cartes wagons :
        - Variable : carte_wagons
        - Type : dictionnaire
        - Syntaxe : "nom de la carte": nb de cartes

        Cartes destination :
        - Variable : carte_destination
        - Type : dictionnaire
        - Syntaxe : "Nom de la carte": nb de points
        """
        self.dims_carte = (603, 380)  # TODO: à lier avec l'IHM
        self.carte_wagons = {
            "white": 12,
            "blue": 12,
            "yellow": 12,
            "black": 12,
            "orange": 12,
            "pink": 12,
            "red": 12,
            "green": 12,
            "locomotive": 14
        }
        self.carte_destination = {
            "Los Angeles to New York": 21,
            "Duluth to Houston": 8,
            "Sault Ste Marie to Nashville": 8,
            "New York to Atlanta": 6,
            "Portland to Nashville": 17,
            "Vancouver to Montreal": 20,
            "Duluth to El Paso": 10,
            "Toronto to Miami": 10,
            "Portland to Phoenix": 11,
            "Dallas to New York": 11,
            "Calgary to Salt Lake City": 7,
            "Calgary to Phoenix": 13,
            "Los Angeles to Miami": 20,
            "Winnipeg to Little Rock": 11,
            "San Francisco to Atlanta": 17,
            "Kansas City to Houston": 5,
            "Los Angeles to Chicago": 16,
            "Denver to Pittsburgh": 11,
            "Chicago to Santa Fe": 9,
            "Vancouver to Santa Fe": 13,
            "Boston to Miami": 12,
            "Chicago to New Orleans": 7,
            "Montreal to Atlanta": 9,
            "Seattle to New York": 22,
            "Denver to El Paso": 4,
            "Helena to Los Angeles": 8,
            "Winnipeg to Houston": 12,
            "Montreal to New Orleans": 13,
            "Sault Ste Marie to Oklahoma City": 9,
            "Seattle to Los Angeles": 9
        }
        self.villes = {
            "Los Angeles": Ville("Los Angeles", 4, 5, self.dims_carte[0], self.dims_carte[1]),
            "San Francisco": Ville("San Francisco", 1.5, 9, self.dims_carte[0], self.dims_carte[1]),
            "Portland": Ville("Portland", 2, 17, self.dims_carte[0], self.dims_carte[1]),
            "Seattle": Ville("Seattle", 3, 19, self.dims_carte[0], self.dims_carte[1]),
            "Vancouver": Ville("Vancouver", 3, 21, self.dims_carte[0], self.dims_carte[1]),
            "Calgary": Ville("Calgary", 8, 21.5, self.dims_carte[0], self.dims_carte[1]),
            "Helena": Ville("Helena", 12, 16.5, self.dims_carte[0], self.dims_carte[1]),
            "Salt Lake City": Ville("Salt Lake City", 9, 12, self.dims_carte[0], self.dims_carte[1]),
            "Las Vegas": Ville("Las Vegas", 7, 7.5, self.dims_carte[0], self.dims_carte[1]),
            "Phoenix": Ville("Phoenix", 9, 5, self.dims_carte[0], self.dims_carte[1]),
            "El Paso": Ville("El Paso", 13.5, 4, self.dims_carte[0], self.dims_carte[1]),
            "Santa Fe": Ville("Santa Fe", 14, 7, self.dims_carte[0], self.dims_carte[1]),
            "Denver": Ville("Denver", 14, 10.5, self.dims_carte[0], self.dims_carte[1]),
            "Oklahoma City": Ville("Oklahoma City", 20, 8, self.dims_carte[0], self.dims_carte[1]),
            "Kansas City": Ville("Kansas City", 20.5, 11, self.dims_carte[0], self.dims_carte[1]),
            "Omaha": Ville("Omaha", 19.5, 13, self.dims_carte[0], self.dims_carte[1]),
            "Duluth": Ville("Duluth", 21, 17, self.dims_carte[0], self.dims_carte[1]),
            "Winnipeg": Ville("Winnipeg", 17, 21, self.dims_carte[0], self.dims_carte[1]),
            "Sault Ste Marie": Ville("Sault Ste Marie", 25.5, 19, self.dims_carte[0], self.dims_carte[1]),
            "Dallas": Ville("Dallas", 20.5, 5, self.dims_carte[0], self.dims_carte[1]),
            "Houston": Ville("Houston", 22, 3, self.dims_carte[0], self.dims_carte[1]),
            "New Orleans": Ville("New Orleans", 25.5, 3.5, self.dims_carte[0], self.dims_carte[1]),
            "Little Rock": Ville("Little Rock", 23, 8, self.dims_carte[0], self.dims_carte[1]),
            "Saint Louis": Ville("Saint Louis", 24, 11, self.dims_carte[0], self.dims_carte[1]),
            "Chicago": Ville("Chicago", 25.5, 14, self.dims_carte[0], self.dims_carte[1]),
            "Nashville": Ville("Nashville", 27, 10, self.dims_carte[0], self.dims_carte[1]),
            "Atlanta": Ville("Atlanta", 29, 8, self.dims_carte[0], self.dims_carte[1]),
            "Miami": Ville("Miami", 34, 2, self.dims_carte[0], self.dims_carte[1]),
            "Charleston": Ville("Charleston", 33, 8, self.dims_carte[0], self.dims_carte[1]),
            "Pittsburgh": Ville("Pittsburgh", 30, 15, self.dims_carte[0], self.dims_carte[1]),
            "Toronto": Ville("Toronto", 30, 18, self.dims_carte[0], self.dims_carte[1]),
            "Montreal": Ville("Montreal", 33, 22, self.dims_carte[0], self.dims_carte[1]),
            "Boston": Ville("Boston", 35.5, 19.5, self.dims_carte[0], self.dims_carte[1]),
            "New York": Ville("New York", 33.5, 16.5, self.dims_carte[0], self.dims_carte[1]),
            "Washington": Ville("Washington", 34, 13, self.dims_carte[0], self.dims_carte[1]),
            "Raleigh": Ville("Raleigh", 31.5, 10.5, self.dims_carte[0], self.dims_carte[1])
        }
        self.liens_villes = {
            "Los Angeles": {
                "San Francisco": ["yellow", 3],
                "Las Vegas": ["grey", 2],
                "Phoenix": ["grey", 3],
                "El Paso": ["black", 6]
            },
            "San Francisco": {
                "Portland": ["orange", 5],
                "Salt Lake City": ["orange", 5],
                "Los Angeles": ["yellow", 3]
            },
            "Portland": {
                "Seattle": ["grey", 1],
                "Salt Lake City": ["blue", 6],
                "San Francisco": ["orange", 5]
            },
            "Seattle": {
                "Portland": ["grey", 1],
                "Helena": ["yellow", 6],
                "Vancouver": ["grey", 1],
                "Calgary": ["grey", 4]
            },
            "Vancouver": {
                "Seattle": ["grey", 1],
                "Calgary": ["grey", 3]
            },
            "Calgary": {
                "Winnipeg": ["white", 6],
                "Helena": ["grey", 4],
                "Seattle": ["grey", 4],
                "Vancouver": ["grey", 3]
            },
            "Helena": {
                "Seattle": ["yellow", 6],
                "Calgary": ["grey", 4],
                "Winnipeg": ["blue", 4],
                "Duluth": ["orange", 6],
                "Omaha": ["red", 5],
                "Denver": ["orange", 4],
                "Salt Lake City": ["grey", 3]
            },
            "Salt Lake City": {
                "Portland": ["blue", 6],
                "San Francisco": ["orange", 5],
                "Las Vegas": ["orange", 3],
                "Denver": ["yellow", 3],
                "Helena": ["grey", 3]
            },
            "Las Vegas": {
                "Salt Lake City": ["orange", 3],
                "Los Angeles": ["grey", 2]
            },
            "Phoenix": {
                "El Paso": ["grey", 3],
                "Santa Fe": ["grey", 3],
                "Los Angeles": ["grey", 3],
                "Denver": ["white", 5]
            },
            "El Paso": {
                "Santa Fe": ["grey", 2],
                "Phoenix": ["grey", 3],
                "Los Angeles": ["black", 6],
                "Houston": ["orange", 6],
                "Dallas": ["red", 4],
                "Oklahoma City": ["yellow", 5]
            },
            "Santa Fe": {
                "Phoenix": ["grey", 3],
                "Denver": ["grey", 2],
                "Oklahoma City": ["blue", 3],
                "El Paso": ["grey", 2]
            },
            "Denver": {
                "Santa Fe": ["grey", 2],
                "Phoenix": ["white", 5],
                "Salt Lake City": ["yellow", 3],
                "Helena": ["orange", 4],
                "Omaha": ["grey", 4],
                "Kansas City": ["black", 4],
                "Oklahoma City": ["red", 4]
            },
            "Oklahoma City": {
                "Denver": ["red", 4],
                "Kansas City": ["grey", 2],
                "Santa Fe": ["blue", 3],
                "El Paso": ["yellow", 6],
                "Dallas": ["grey", 2],
                "Little Rock": ["grey", 2]
            },
            "Kansas City": {
                "Denver": ["orange", 4],
                "Omaha": ["grey", 1],
                "Saint Louis": ["grey", 2],
                "Oklahoma City": ["grey", 2]
            },
            "Omaha": {
                "Denver": ["grey", 4],
                "Kansas City": ["grey", 1],
                "Chicago": ["blue", 4],
                "Duluth": ["grey", 2],
                "Helena": ["red", 5]
            },
            "Duluth": {
                "Winnipeg": ["white", 4],
                "Helena": ["orange", 6],
                "Sault Ste Marie": ["grey", 3],
                "Toronto": ["grey", 6],
                "Chicago": ["red", 3],
                "Omaha": ["grey", 2]
            },
            "Sault Ste Marie": {
                "Winnipeg": ["grey", 6],
                "Duluth": ["grey", 3],
                "Toronto": ["grey", 2],
                "Montreal": ["black", 5]
            },
            "Winnipeg": {
                "Calgary": ["white", 6],
                "Helena": ["blue", 4],
                "Duluth": ["black", 4],
                "Sault Ste Marie": ["grey", 6]
            },
            "Dallas": {
                "Houston": ["grey", 1],
                "El Paso": ["red", 4],
                "Oklahoma City": ["grey", 2],
                "Little Rock": ["grey", 2]
            },
            "Houston": {
                "Dallas": ["grey", 1],
                "El Paso": ["orange", 6],
                "New Orleans": ["grey", 2]
            },
            "New Orleans": {
                "Houston": ["grey", 2],
                "Little Rock": ["orange", 3],
                "Atlanta": ["yellow", 4],
                "Miami": ["red", 6]
            },
            "Little Rock": {
                "New Orleans": ["orange", 3],
                "Dallas": ["grey", 2],
                "Oklahoma City": ["grey", 2],
                "Saint Louis": ["grey", 2],
                "Nashville": ["white", 3]
            },
            "Saint Louis": {
                "Little Rock": ["grey", 2],
                "Kansas City": ["grey", 2],
                "Chicago": ["white", 2],
                "Pittsburgh": ["orange", 5],
                "Nashville": ["grey", 2]
            },
            "Chicago": {
                "Saint Louis": ["white", 2],
                "Omaha": ["blue", 4],
                "Duluth": ["red", 3],
                "Toronto": ["white", 4],
                "Pittsburgh": ["black", 3]
            },
            "Nashville": {
                "Saint Louis": ["grey", 2],
                "Pittsburgh": ["yellow", 4],
                "Little Rock": ["white", 3],
                "Atlanta": ["grey", 1],
                "Raleigh": ["black", 3]
            },
            "Atlanta": {
                "Nashville": ["grey", 1],
                "Raleigh": ["grey", 2],
                "Charleston": ["grey", 2],
                "New Orleans": ["yellow", 4],
                "Miami": ["blue", 5]
            },
            "Miami": {
                "New Orleans": ["red", 6],
                "Atlanta": ["blue", 5],
                "Charleston": ["grey", 4]
            },
            "Charleston": {
                "Miami": ["grey", 4],
                "Atlanta": ["grey", 2],
                "Raleigh": ["grey", 2]
            },
            "Pittsburgh": {
                "Washington": ["grey", 2],
                "Raleigh": ["grey", 2],
                "Nashville": ["yellow", 4],
                "Saint Louis": ["orange", 5],
                "Chicago": ["black", 3],
                "Toronto": ["grey", 2],
                "New York": ["orange", 2]
            },
            "Toronto": {
                "Pittsburgh": ["grey", 2],
                "Chicago": ["white", 4],
                "Duluth": ["grey", 6],
                "Sault Ste Marie": ["grey", 2],
                "Montreal": ["grey", 3]
            },
            "Montreal": {
                "Boston": ["grey", 2],
                "New York": ["blue", 3],
                "Toronto": ["grey", 3],
                "Sault Ste Marie": ["black", 5]
            },
            "Boston": {
                "Montreal": ["grey", 2],
                "New York": ["yellow", 2]
            },
            "New York": {
                "Boston": ["yellow", 2],
                "Montreal": ["blue", 3],
                "Pittsburgh": ["orange", 2],
                "Washington": ["black", 2]
            },
            "Washington": {
                "New York": ["black", 2],
                "Pittsburgh": ["grey", 2],
                "Raleigh": ["grey", 2]
            },
            "Raleigh": {
                "Washington": ["grey", 2],
                "Pittsburgh": ["grey", 2],
                "Nashville": ["black", 3],
                "Atlanta": ["grey", 2],
                "Charleston": ["grey", 2]
            }
        }
        self.init_villes()

    def init_villes(self):
        """
        Initialise les liens entre les villes
        """
        for key1 in self.villes.keys():
            for key2, value2 in self.liens_villes[key1].items():
                self.villes[key1].ajout_liens(key2, value2[0], value2[1])

    def show_plateau(self):
        """
        Définit le plateau du jeu
        => Construit le graphe des villes
        Affiche un point pour chaque ville avec le nom en dessous
        Relie chaque ville par un trait gris quand non occupé
        """
        figure = Figure()
        axes = figure.gca()
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        im = plt.imread("img/carte_usa.jpg")

        """Affichage des liens entre les villes :"""
        for nom_ville, ville in self.villes.items():
            x_ville, y_ville = ville.coords
            rx = 603 / 36
            ry = 380 / 23
            for nom_lien, value in ville.liens.items():
                couleur_lien, nb_wagons_lien = value
                x_liens, y_liens = self.villes[nom_lien].coords
                axes.plot((x_ville * rx, x_liens * rx), (y_ville * ry, y_liens * ry), color=couleur_lien, linewidth=5)
                # Pour les lignes en tirets : linestyle="dashed"
            axes.plot(x_ville * rx, y_ville * ry, 'ro')
            axes.text((x_ville - 1) * rx, (y_ville - 1) * ry, nom_ville)
        """Arrière-plan du plateau :"""
        # axes.imshow(im, extent=[1,36,1,22.7])
        axes.imshow(im, extent=[0, 603, 0, 380])
        # axes.imshow(im)
        axes.axis(False)
        # plt.show()
        # im = ax.imshow(im)
        # format image: 603x380
        # Grille pour les points du graphe: 36x22.5
        # Rapport : 1.6
        return figure


class Ville(object):
    id = -1

    def __init__(self, nom_ville, x, y, width, height):
        self.nom: str = nom_ville
        self.dims_carte = (width, height)
        self.coords = (x, y)
        self.liens = {}  # format: "nom_ville":["couleur_liens",nb_wagons]
        Ville.id += 1
        self.id = Ville.id

    @classmethod
    def get_id(cls):
        return Ville.id

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, value):
        self.__coords = (min(max(0, value[0]), self.dims_carte[0]), min(max(0, value[1]), self.dims_carte[1]))

    def ajout_liens(self, nom_ville2, couleur, nb_wagons):
        self.liens[nom_ville2] = [couleur, nb_wagons]

    def get_nb_wagon_lien(self, nom_ville2):
        """
        Renvoie le nb de wagons nécessaire pour prendre la route.
        """
        return self.liens[nom_ville2][1]


class Partie(Jeu):
    """Classe qui est utilisé pour lancer une partie du jeu.
    Fait appel à la classe Jeu pour accéder à toutes les cartes et informations sur le plateau de jeu."""

    def __init__(self):
        super().__init__()
        self.les_joueurs = {}  # Dictionnaire contenant tous les noms + objet Joueur de la partie.
        self.ordre = []  # Liste de l'ordre dans lequel joue les joueurs. Contient le nom de chaque joueur dans l'ordre.
        self.nb_joueurs: int = 5
        self.pile_cartes_wagon = [carte for carte, nb_carte in self.carte_wagons.items() for k in range(nb_carte)]
        # Définit l'ordre des cartes wagons. C'est la pile de cartes.
        self.pile_cartes_destination = [destination for destination in self.carte_destination.keys()]
        self.defausse_wagon = []
        # self.current_player=self.change_current_player()

    def debut_partie(self, ihm_partie):
        """
        Définition des joueurs
        :return:
        """
        self.nb_joueurs = len(ihm_partie.les_joueurs)
        for player_input in ihm_partie.les_joueurs:
            nom = player_input[0]
            couleur = player_input[1]
            if "IA" in nom:
                self.les_joueurs[nom] = IA_player(nom, couleur)
            else:
                self.les_joueurs[nom] = Joueur(nom, couleur)
            self.ordre.append(nom)
        # DONE: Demander le nb total de joueurs de la partie, nb joueurs humains. => compléter par des joueurs IAs
        # DONE: vérifier que nb_joueurs est compris entre 2 et 5. => vérifié dans l'IHM car on ne peut pas dépasser 5.

    # @property
    # def nb_joueurs(self):
    #     """Accesseur en lecture du nombre de joueurs de la partie"""
    #     return self.__nb_joueurs
    #
    # @nb_joueurs.setter
    # def nb_joueurs(self, value):
    #     """Accesseur en écriture du nombre de joueurs de la partie"""
    #     #DONE: traiter le cas où la valeur n'est pas un int mais du texte par exemple. => solution dans l'IHM.
    #
    #     # if type(value) != int:
    #     #     print("Indiquer un nombre.")
    #     #     self.nb_joueurs = input("Nombre de joueurs pour la partie")
    #     if int(value) not in range(2, 6):
    #         print("Le nombre de joueurs doit être compris entre 2 et 5 pour lancer une partie.\nCela est différent du "
    #               "nombre de joueurs IAs.\nVeuillez rentrer à nouveau une valeur correcte.")
    #         self.nb_joueurs = input("Nombre de joueurs pour la partie")
    #     self.__nb_joueurs = int(value)

    def rotation_joueur(self, index):
        """
        Réalise la rotation des joueurs selon l'indice fourni dans le sens horaire.
        :return:
        L'ordre des joueurs
        """
        if index != 0:
            temp_joueur = []
            while len(self.ordre) > index:
                temp_joueur.append(self.ordre.pop(index))
            while len(self.ordre) > 0:
                temp_joueur.append(self.ordre.pop(0))
            self.ordre = temp_joueur
        return "L'ordre des joueurs est établi comme suit : \n" + self.liste_joueurs()

    def choix_tour_joueur(self, ihm_partie):
        """
        Définit le tour des joueurs en fonction de celui qui a le plus voyagé puis selon sens horaire.
        :return:
        L'ordre des joueurs de la partie
        """
        joueur_voyageur = ihm_partie.joueur_le_plus_voyageur
        self.rotation_joueur(self.ordre.index(joueur_voyageur))

    def liste_joueurs(self):
        """
        Renvoie la liste des joueurs en partie dans l'ordre de leur tour.
        :return:
        """
        liste_joueurs = ""
        for joueur in self.ordre:
            liste_joueurs += joueur + "\n"
        return liste_joueurs

    def tour(self, joueur, ihm_partie):
        """
        Réalise 1 tour de tous les joueurs où chacun joue leur tour de jeu en fonction de toutes les actions possibles.
        :return:
        """
        """Les choix sont faits en direct par le joueur dans l'IHM.
        Les fonctions de contrôle du jeu sont appelées dans la partie IHM."""
        print(IhmJoueur(ihm_partie).launch_joueur(joueur))
        return True
        # print("C'est le tour de " + joueur.nom_joueur)
        # choix: int = int(input(
        #     "Que voulez-vous faire ?\n" + "1. Prendre des cartes Wagon\n2. Prendre possession d'une route\n3. "
        #                                   "Prendre des cartes Destination supplémentaires\nIndiquer le numéro "
        #                                   "de l'action choisie"))
        # choix=1 # à lier avec l'IHM.
        # if choix == 1:
        #     self.prendre_cartes_wagon(joueur, ihm_partie)
        # elif choix == 2:
        #     self.prendre_route(joueur)
        # else:
        #     print("Non disponible pour le moment")
        #     # self.prendre_cartes_Destination()

    @staticmethod
    def melange_cartes(pile_cartes: list):
        """
        Mélange des cartes.
        Renvoie un paquet totalement mélangé aléatoirement.
        :return:
        """
        n = len(pile_cartes)
        for k in range(n):
            index1, index2 = r.randint(0, n - 1), r.randint(0, n - 1)
            pile_cartes[index1], pile_cartes[index2] = pile_cartes[index2], pile_cartes[index1]
        return pile_cartes

    @staticmethod
    def melange_americain(paquet: list):
        """
        Mélange les cartes à la façon américaine.
        Renvoie un paquet mélangé selon cette façon.

        Principe du mélange :
            On prend la moitié du paquet.
            On mélange les cartes en les entrelaçant aléatoirement (entre 1 et 3 cartes de chaque petit paquet)
            On les réunit pour terminer le mélange.
        :return:
        """
        n = len(paquet)
        p1 = paquet[0:n // 2]
        n1 = len(p1)
        p2 = paquet[n // 2:]
        n2 = len(p2)
        # TODO : pour les tests, vérifier que len(p1)+len(p2)=len(paquet)
        for carte in p2:
            index = r.randint(0, n1)
            p1.insert(index, carte)
        return p1

    def prendre_cartes_wagon(self, joueur, ihm_partie):
        """
         1. Prendre des cartes Wagon :
        – le joueur peut prendre 2 cartes Wagon.
        Il peut prendre n’importe quelle carte visible parmi les 5 posées sur la table ou tirer une carte du dessus de
        la pioche (tirage en aveugle). Si le joueur prend une carte visible, il la remplace immédiatement par une
        autre du dessus de la pioche. Il peut ensuite prendre une deuxième carte, soit visible, soit en aveugle (voir
        section Cartes Wagon pour les cartes Locomotive).
        :return:
        """
        """Indication sur les cartes Wagon : 
        Cartes Wagon 
        
        Il existe 8 types de wagons différents en plus de la locomotive. Les couleurs de chaque carte Wagon 
        correspondent aux couleurs présentes sur le plateau afin de relier les villes : bleu, violet, orange, blanc, 
        vert, jaune, noir et rouge. Les locomotives sont multicolores et, comme des cartes joker, peuvent remplacer 
        n’importe quelle couleur lors de la prise de possession d’une route."""

        """"
        Il est possible de ne jouer que des cartes Locomotive pour prendre une route. Si une carte Locomotive figure 
        parmi les 5 cartes visibles, le joueur peut la prendre, mais son tour s’arrête alors. La locomotive compte 
        comme si l’on avait pris 2 cartes. Si, après avoir pris une carte visible (qui n’est pas une locomotive), 
        la carte de remplacement est une locomotive, le joueur ne peut pas la prendre. Si, au cours du jeu, 
        3 cartes visibles sur 5 sont des locomotives, les 5 cartes sont alors immédiatement défaussées et remplacées 
        par 5 nouvelles cartes. 
        
        Note : Si un joueur a la chance de tirer une locomotive en aveugle, au sommet de la pioche, les autres 
        joueurs n’en savent rien et cette carte ne compte que pour une seule carte piochée. Un joueur peut avoir en 
        main et à tout moment autant de cartes qu’il le souhaite. Quand la pioche de cartes est épuisée, les cartes 
        défaussées sont soigneusement mélangées pour reconstituer une nouvelle pioche. Il est important de bien 
        mélanger les cartes car elles ont été défaussées par séries de couleurs ! Dans le cas peu probable où il n’y 
        aurait plus de cartes disponibles (si toutes les cartes sont dans les mains des joueurs) un joueur ne peut 
        plus prendre de cartes. Il ne peut donc que prendre possession d’une route ou tirer de nouvelles cartes 
        Destination. """

        "Version console"  # Commenté pour éviter les inputs et arrêt de l'IHM.
        # print("Voici les cartes sur la table :")
        # DONE: Vérifier le cas pour les locomotives pr mélanger à nouveau si besoin => vérif_locomotive()
        # self.verif_locomotive()
        # for k in range(5):  # On montre les 5 premières cartes de la pile pour faire les cartes face visible.
        #     print(self.pile_cartes_wagon[k])
        # # print("Vous pouvez choisir 2 cartes")
        # visible = input("Voulez-vous une 1ère carte visible ? [y/n]") == "y"
        # nom_carte = ""
        # if visible:
        #     nom_carte = input("Quelle carte voulez-vous ? Indiquer un nom de carte parmi celle visible.")
        #     while nom_carte not in self.pile_cartes_wagon[0:5]:
        #         print("Il faut que la carte soit parmi celles face visible.\nRecommencer.")
        #         nom_carte = input("Quelle carte voulez-vous ? Indiquer un nom de carte parmi celle visible.")
        #     joueur.main_wagon[nom_carte] += 1
        #     self.pile_cartes_wagon.pop(
        #         self.pile_cartes_wagon.index(nom_carte))
        #     # Pour l'instant, on enlève la première occurrence du nom_carte et non celle choisi parmi les 5. A vérifier.
        #     print("Vous avez choisi la carte " + str(nom_carte))
        # else:
        #     carte = self.pile_cartes_wagon.pop(6)  # Car c'est la carte au-dessus de la pile après les cartes visibles.
        #     joueur.main_wagon[carte] += 1
        #     print("Vous avez pris une carte face cachée.")
        #     # DONE: ajouter une fonctionnalité pour que le joueur puisse voir la carte sans que les autres la voient.
        #     #  Solution : Faire un jeu contre IA ou faire plusieurs fenêtres ou jouer en LAN ou jouer en
        #     #  ligne/multijoueur.
        # if nom_carte != "locomotive":
        #     for k in range(5):
        #         print(self.pile_cartes_wagon[k])
        #     visible = input("Voulez-vous une 2e carte visible ? [y/n]") == "y"
        #     if visible:
        #         nom_carte = input("Quelle carte voulez-vous ? Indiquer un nom de carte parmi celle visible.")
        #         while nom_carte not in self.pile_cartes_wagon[0:5]:
        #             print("Il faut que la carte soit parmi celles face visible.\nRecommencer.")
        #             nom_carte = input("Quelle carte voulez-vous ? Indiquer un nom de carte parmi celle visible.")
        #         joueur.main_wagon[nom_carte] += 1
        #         self.pile_cartes_wagon.pop(self.pile_cartes_wagon.index(nom_carte))
        #         # DONE: améliorer le retrait des cartes. Pour l'instant, on enlève la première occurrence du
        #         #  nom_carte et non celle choisi parmi les 5. A vérifier.
        #         print("Vous avez choisi la carte " + str(nom_carte))
        #     else:
        #         carte = self.pile_cartes_wagon.pop(6)  # Car c'est la carte au-dessus de la pile après celles visibles.
        #         joueur.main_wagon[carte] += 1
        #         print("Vous avez pris une carte face cachée.")
        # print("Fin du tour.")

        " Version pour l'IHM"
        # Carte visible
        if ihm_partie.visible_wagon:
            nom_carte = ihm_partie.visible_wagon
            joueur.main_wagon[nom_carte] += 1
            return "locomotive" in nom_carte
        # Carte face cachée
        if ihm_partie.hide_wagon:
            nom_carte = ihm_partie.hide_wagon
            joueur.main_wagon[nom_carte] += 1
            return False  # Même si on tire une carte locomotive, cela compte quand même comme 1 seule carte tirée.

        # DONE: vérifier que le joueur ne peut ajouter que 2 cartes au max.
        # DONE: vérifier qu'il peut prendre 2 cartes au total.
        # DONE: vérifier le cas où il prend une locomotive lorsque c'est face visible.
        # DONE: vérifier le cas où il n'y a plus de cartes et qu'il faut mélanger la défausse. => dans verif_locomotive
        # TODO: vérifier le cas où toutes les cartes ont été prises par les joueurs. => option plus disponible tant
        #  qu'il n'en défausse pas. => se fait tout seul ? car les cartes ne s'affichent plus ? à vérifier.

    def verif_locomotive(self):
        """
        Vérifie que les cartes face visible ne présentent pas plus de 3 cartes locomotives.
        Sinon, défausse les 5 cartes et en remet 5.
        :return:
        """
        n = len(self.pile_cartes_wagon)
        if self.pile_cartes_wagon[:5].count("locomotive") >= 3:
            for k in range(5):
                self.defausse_wagon.append(self.pile_cartes_wagon.pop(0))
            if n < 5:  # renouvellement de la pile de cartes wagon
                self.pile_cartes_wagon = self.pile_cartes_wagon \
                                         + self.melange_americain(self.melange_cartes(self.defausse_wagon))
                self.defausse_wagon.clear()

    def prendre_route(self, joueur):
        """
        2. Prendre possession d’une route :
        – Le joueur peut s’emparer d’une route sur le plateau en posant autant de cartes Wagon de la couleur
        de la route que d’espaces composant la route. Après avoir défaussé ses cartes, le joueur pose alors ses wagons
        sur chaque espace constituant la route. Enfin, il déplace son marqueur de score en se référant au tableau de
        décompte des points.
        :return:
        """

        """Indication:
        Prendre possession des routes
        Pour prendre possession d’une route, un joueur doit jouer une série de cartes égale au
        nombre d’espaces composant la route. La série de cartes doit être composée de cartes du
        même type. La plupart des routes nécessitent une série de cartes de couleur spécifique. Par
        exemple, les routes bleues sont capturées en posant des cartes Wagon bleues. Certaines
        routes – en gris sur le plateau - peuvent être capturées en utilisant n’importe quelle série
        d’une même couleur.
        Lorsqu’une route a été capturée, le joueur pose ses wagons en plastique sur chacun des
        espaces qui constituent la route. Toutes les cartes utilisées pour s’approprier cette route
        sont défaussées.
        Un joueur peut prendre possession de n’importe quelle route sur le plateau de jeu. Il n’est
        pas obligé de se connecter avec les routes déjà à son actif. Un joueur ne peut jamais prendre
        plus d’une route par tour de jeu.
        Une route prise par un joueur devient sa propriété exclusive. Aucun
        autre joueur ne peut plus revendiquer son
        usage ou son occupation.
        Certaines villes sont reliées par des routes
        doubles. Un même joueur ne peut pas prendre
        2 routes reliant les 2 mêmes villes.
        Note importante : Dans une configuration
        à 2 ou 3 joueurs, seule l’une des routes constituant la double
        connexion peut être utilisée. Un joueur peut donc prendre
        possession de l’une des 2 routes disponibles, la route restante
        demeurant fermée jusqu’à la fin de la partie.
        """
        nom_route = [input("Quelle route voulez-vous prendre ? Indiquer le nom de la première ville."),
                     input("Indiquer le nom de la seconde ville")]
        # TODO: pour l'IHM, faire en fonction des cliques du joueur sur la carte pour relier les 2.
        #  Click sur le lien entre les villes ou clique sur les 2 villes.
        route = self.liens_villes[nom_route[0]][nom_route[1]]  # contient [couleur,nb_segments]
        # Vérification que le joueur peut prendre une route :
        if route[0] == "grey":
            couleur = input("La route est grise. Avec quelle couleur voulez-vous la prendre ?")
        else:
            couleur = route[1]
        if joueur.main_wagon[couleur] == route[1]:
            # défausse des cartes de la main vers la défausse
            for k in range(route[1]):
                self.defausse_wagon.append(
                    couleur)  # à voir : on a plusieurs solutions pour la défausse des cartes.
            # retrait des wagons de la main du joueur :
            joueur.main_wagon[couleur] -= route[1]
            # TODO: faire un accesseur en écriture pour vérifier qu'aucune entrée de wagons soient négatives.
            # ajout de la route au joueur :
            joueur.route_prise.append(nom_route)
            print("Vous avez pris la route de {} à {}".format(nom_route[0], nom_route[1]))
            # calcul des points gagnés :
            pts = Score.calcul_pts_route(joueur)
            print("Vous avez gagné {} points".format(pts))
            # TODO: implémenter la méthode du calcul du score en fonction du nb de wagons posés. cf. Classe Score.
            # Score.points() => à corriger en fonction de l'implémentation

    def preparation_partie(self):
        """
        Prépare la partie selon les règles.
        Préparation du jeu :
        Mélangez les cartes Wagon et distribuez-en 4 à chacun des joueurs. Placez le reste
        des cartes près du plateau, face cachée, puis retournez les cinq premières cartes que
        vous posez à côté, face visible.
        Posez la carte Chemin le plus long, face visible, à côté du plateau.
        Mélangez les cartes Destination et distribuez-en 3 à chaque joueur. Chaque joueur
        peut maintenant regarder ses destinations afin de décider lesquelles conserver. Il doit
        garder au moins 2 cartes, mais peut conserver les 3 s’il le souhaite. Chaque carte rendue
        est placée sous le talon des cartes Destination. Le paquet de cartes Destination est ensuite
        placé face cachée à côté du plateau. Les joueurs gardent leurs destinations secrètes
        jusqu’à la fin du jeu.
        Vous êtes maintenant prêts à jouer.
        :return:
        """
        self.pile_cartes_wagon = self.melange_cartes(self.pile_cartes_wagon)
        self.pile_cartes_wagon = self.melange_americain(self.pile_cartes_wagon)
        self.pile_cartes_destination = self.melange_cartes(self.pile_cartes_destination)
        self.pile_cartes_destination = self.melange_americain(self.pile_cartes_destination)
        for joueur in self.les_joueurs.values():
            for k in range(4):
                joueur.main_wagon[self.pile_cartes_wagon.pop(0)] += 1
            for i in range(3):
                joueur.main_destination.append(self.pile_cartes_destination.pop(0))

    def partie(self, ihm_partie):
        """
        fait tourner une partie complète du jeu. du début à la fin.
        :return:
        """
        self.debut_partie(ihm_partie)
        self.preparation_partie()
        """
        # Règle du jeu :
        ## Tour de jeu
        Le joueur qui a le plus voyagé commence."""
        self.choix_tour_joueur(ihm_partie)
        """Par la suite, on joue dans le sens des aiguilles d’une montre. 
        À son tour, le joueur doit faire une et une seule des trois actions suivantes : 
        1. Prendre des cartes Wagon
        2. Prendre possession d’une route
        3. Prendre des cartes Destination supplémentaires
        """
        i = 0
        nom = self.ordre[i]
        joueur = self.les_joueurs[nom]
        fin_tour = False
        while joueur.wagons > 2:
            if not fin_tour:
                fin_tour = self.tour(joueur, ihm_partie)
            else:
                if i == len(self.ordre) - 1:
                    i = 0
                else:
                    i += 1
                nom = self.ordre[i]
                joueur = self.les_joueurs[nom]
                fin_tour = False
        self.rotation_joueur(i)
        for nom in self.ordre:
            self.tour(self.les_joueurs[nom], ihm_partie)
        print("Fin de partie\nAffichage du score bientôt disponible")
        """
        Fin du jeu
        Lorsque la réserve de wagons d’un joueur est de 0, 1 ou 2 wagons après avoir joué son tour, 
        chaque joueur, en incluant celui-ci, joue encore un tour. À l’issue de ce dernier tour, le jeu s’arrête et 
        chacun compte ses points """


class Partie_qt(Jeu):
    """Classe qui est utilisé pour lancer une partie du jeu.
    Fait appel à la classe Jeu pour accéder à toutes les cartes et informations sur le plateau de jeu."""
    traduction_color = {
        "white": "blanc",
        "blue": "bleu",
        "yellow": "jaune",
        "black": "noir",
        "orange": "orange",
        "pink": "rose",
        "red": "rouge",
        "green": "vert",
        "grey": "gris",
        "locomotive": "locomotive"
    }

    def __init__(self):
        super().__init__()
        self.les_routes = []
        self.init_les_routes()
        self.count_wagon_card = 0
        self.idx_current_player = 0
        self.current_player_name = ""
        self.current_player: Joueur = None
        self.LAST_TURN = False
        self.les_joueurs = {}  # Dictionnaire contenant tous les noms + objet Joueur de la partie.
        self.ordre = []  # Liste de l'ordre dans lequel joue les joueurs. Contient le nom de chaque joueur dans l'ordre.
        self.nb_joueurs: int = 5
        self.pile_cartes_wagon = [carte for carte, nb_carte in self.carte_wagons.items() for k in range(nb_carte)]
        # Définit l'ordre des cartes wagons. C'est la pile de cartes.
        self.pile_cartes_destination = [destination for destination in self.carte_destination.keys()]
        self.defausse_wagon = []

    def debut_partie(self, ihm_partie):
        """
        Définition des joueurs
        :return:
        """
        self.nb_joueurs = ihm_partie.nb_joueurs_tot
        for player_input in ihm_partie.les_joueurs[:self.nb_joueurs]:
            nom = player_input[0]
            couleur = player_input[1]
            ia_level = player_input[2]
            if ia_level:
                self.les_joueurs[nom] = IA_player(nom, couleur, ia_level)
            else:
                self.les_joueurs[nom] = Joueur(nom, couleur)
            self.ordre.append(nom)
        # DONE: Demander le nb total de joueurs de la partie, nb joueurs humains. => compléter par des joueurs IAs
        # DONE: vérifier que nb_joueurs est compris entre 2 et 5. => vérifié dans l'IHM car on ne peut pas dépasser 5.

    def rotation_joueur(self, index):
        """
        Réalise la rotation des joueurs selon l'indice fourni dans le sens horaire.
        :return:
        L'ordre des joueurs
        """
        if index != 0:
            temp_joueur = []
            while len(self.ordre) > index:
                temp_joueur.append(self.ordre.pop(index))
            while len(self.ordre) > 0:
                temp_joueur.append(self.ordre.pop(0))
            self.ordre = temp_joueur
        return "L'ordre des joueurs est établi comme suit : \n" + self.liste_joueurs()

    def choix_tour_joueur(self, ihm_partie):
        """
        Définit le tour des joueurs en fonction de celui qui a le plus voyagé puis selon sens horaire.
        :return:
        L'ordre des joueurs de la partie
        """
        joueur_voyageur = ihm_partie.joueur_le_plus_voyageur
        self.rotation_joueur(self.ordre.index(joueur_voyageur))

    def liste_joueurs(self):
        """
        Renvoie la liste des joueurs en partie dans l'ordre de leur tour.
        Pour la phase de test du jeu sur console/terminal.
        """
        liste_joueurs = ""
        for joueur in self.ordre:
            liste_joueurs += joueur + "\n"
        return liste_joueurs

    @staticmethod
    def melange_cartes(pile_cartes: list):
        """
        Mélange des cartes.
        Renvoie un paquet totalement mélangé aléatoirement.
        :return:
        """
        n = len(pile_cartes)
        for K in range(n):
            index1, index2 = r.randint(0, n - 1), r.randint(0, n - 1)
            pile_cartes[index1], pile_cartes[index2] = pile_cartes[index2], pile_cartes[index1]
        return pile_cartes

    @staticmethod
    def melange_americain(paquet: list):
        """
        Mélange les cartes à la façon américaine.
        Renvoie un paquet mélangé selon cette façon.

        Principe du mélange :
            On prend la moitié du paquet.
            On mélange les cartes en les entrelaçant aléatoirement (entre 1 et 3 cartes de chaque petit paquet)
            On les réunit pour terminer le mélange.
        :return:
        """
        n = len(paquet)
        p1 = paquet[0:n // 2]
        n1 = len(p1)
        p2 = paquet[n // 2:]
        n2 = len(p2)
        # TODO : pour les tests, vérifier que len(p1)+len(p2)=len(paquet)
        for carte in p2:
            index = r.randint(0, n1)
            p1.insert(index, carte)
        return p1

    def prendre_cartes_wagon(self, idx_carte_prise, carte_visible):
        """
         1. Prendre des cartes Wagon :
        – le joueur peut prendre 2 cartes Wagon.
        Il peut prendre n’importe quelle carte visible parmi les 5 posées sur la table ou tirer une carte du dessus de
        la pioche (tirage en aveugle). Si le joueur prend une carte visible, il la remplace immédiatement par une
        autre du dessus de la pioche. Il peut ensuite prendre une deuxième carte, soit visible, soit en aveugle (voir
        section Cartes Wagon pour les cartes Locomotive).
        :return:
        """
        """Indication sur les cartes Wagon : 
        Cartes Wagon 

        Il existe 8 types de wagons différents en plus de la locomotive. Les couleurs de chaque carte Wagon 
        correspondent aux couleurs présentes sur le plateau afin de relier les villes : bleu, violet, orange, blanc, 
        vert, jaune, noir et rouge. Les locomotives sont multicolores et, comme des cartes joker, peuvent remplacer 
        n’importe quelle couleur lors de la prise de possession d’une route."""

        """"
        Il est possible de ne jouer que des cartes Locomotive pour prendre une route. Si une carte Locomotive figure 
        parmi les 5 cartes visibles, le joueur peut la prendre, mais son tour s’arrête alors. La locomotive compte 
        comme si l’on avait pris 2 cartes. Si, après avoir pris une carte visible (qui n’est pas une locomotive), 
        la carte de remplacement est une locomotive, le joueur ne peut pas la prendre. Si, au cours du jeu, 
        3 cartes visibles sur 5 sont des locomotives, les 5 cartes sont alors immédiatement défaussées et remplacées 
        par 5 nouvelles cartes. 

        Note : Si un joueur a la chance de tirer une locomotive en aveugle, au sommet de la pioche, les autres 
        joueurs n’en savent rien et cette carte ne compte que pour une seule carte piochée. Un joueur peut avoir en 
        main et à tout moment autant de cartes qu’il le souhaite. Quand la pioche de cartes est épuisée, les cartes 
        défaussées sont soigneusement mélangées pour reconstituer une nouvelle pioche. Il est important de bien 
        mélanger les cartes car elles ont été défaussées par séries de couleurs ! Dans le cas peu probable où il n’y 
        aurait plus de cartes disponibles (si toutes les cartes sont dans les mains des joueurs) un joueur ne peut 
        plus prendre de cartes. Il ne peut donc que prendre possession d’une route ou tirer de nouvelles cartes 
        Destination. """

        " Version pour l'IHM"
        # FIXED: adaptation à la nouvelle IHM.
        self.update_wagons_stack()
        if self.count_wagon_card < 2:
            carte_prise = self.pile_cartes_wagon.pop(idx_carte_prise)
            if "locomotive" in carte_prise and carte_visible:
                if self.count_wagon_card == 1:
                    self.pile_cartes_wagon.insert(idx_carte_prise, "locomotive")
                    return "Vous ne pouvez plus piocher une carte locomotive"
                self.count_wagon_card += 2
                self.current_player.main_wagon[carte_prise] += 1
            else:
                self.count_wagon_card += 1
                self.current_player.main_wagon[carte_prise] += 1
            return f"Vous avez pris un wagon {self.traduction_color[carte_prise]}"
        return "Vous ne pouvez plus piocher"

    def update_wagons_stack(self):
        """
        Update the wagons' stack according to rules.
        """
        n = len(self.pile_cartes_wagon)
        if self.pile_cartes_wagon[:5].count("locomotive") >= 3:
            for k in range(5):
                self.defausse_wagon.append(self.pile_cartes_wagon.pop(0))
        if n < 5 and self.defausse_wagon:  # renouvellement de la pile de cartes wagon
            self.pile_cartes_wagon = self.pile_cartes_wagon \
                                     + self.melange_americain(self.melange_cartes(self.defausse_wagon))
            self.defausse_wagon.clear()

    def prendre_route(self, ihm_partie):
        """
        2. Prendre possession d’une route :
        – Le joueur peut s’emparer d’une route sur le plateau en posant autant de cartes Wagon de la couleur
        de la route que d’espaces composant la route. Après avoir défaussé ses cartes, le joueur pose alors ses wagons
        sur chaque espace constituant la route. Enfin, il déplace son marqueur de score en se référant au tableau de
        décompte des points.
        :return:
        """

        """Indication:
        Prendre possession des routes
        Pour prendre possession d’une route, un joueur doit jouer une série de cartes égale au
        nombre d’espaces composant la route. La série de cartes doit être composée de cartes du
        même type. La plupart des routes nécessitent une série de cartes de couleur spécifique. Par
        exemple, les routes bleues sont capturées en posant des cartes Wagon bleues. Certaines
        routes – en gris sur le plateau - peuvent être capturées en utilisant n’importe quelle série
        d’une même couleur.
        Lorsqu’une route a été capturée, le joueur pose ses wagons en plastique sur chacun des
        espaces qui constituent la route. Toutes les cartes utilisées pour s’approprier cette route
        sont défaussées.
        Un joueur peut prendre possession de n’importe quelle route sur le plateau de jeu. Il n’est
        pas obligé de se connecter avec les routes déjà à son actif. Un joueur ne peut jamais prendre
        plus d’une route par tour de jeu.
        Une route prise par un joueur devient sa propriété exclusive. Aucun
        autre joueur ne peut plus revendiquer son
        usage ou son occupation.
        Certaines villes sont reliées par des routes
        doubles. Un même joueur ne peut pas prendre
        2 routes reliant les 2 mêmes villes.
        Note importante : Dans une configuration
        à 2 ou 3 joueurs, seule l’une des routes constituant la double
        connexion peut être utilisée. Un joueur peut donc prendre
        possession de l’une des 2 routes disponibles, la route restante
        demeurant fermée jusqu’à la fin de la partie.
        """
        # Récupération des infos de la dialog_take_road
        nom_route = ihm_partie.ui_take_road.choose_road.currentText()
        type_wagon = self.current_player.convert_color_id[ihm_partie.ui_take_road.choose_wagons.currentText()]
        choix_locomotive = ihm_partie.ui_take_road.choose_locomotive.currentText() == "Oui"
        nb_locomotive = ihm_partie.ui_take_road.spinbox_nb_locomotive.value()

        # Traitement des infos reçues
        print(nom_route)  # Debug
        ville1, ville2 = [k.strip() for k in nom_route.strip().split("-")]
        couleur, nb_segments = self.villes[ville1].liens[ville2]  # contient [couleur,nb_segments]
        # Vérification que le joueur peut prendre une route :
        print(f"On checke {nom_route} avec couleur {couleur}")

        # Si on prend la route avec la même couleur sans locomotive OU si route grise et type_wagon sans locomotive
        # OU uniquement des locomotives.
        if self.current_player.main_wagon[type_wagon] >= nb_segments:
            print("On a récupéré la route !")

            # défausse des cartes de la main vers la défausse
            for K in range(nb_segments):
                self.defausse_wagon.append(type_wagon)

            # retrait des wagons de la main du joueur :
            self.current_player.main_wagon[type_wagon] -= nb_segments

            # retrait du nb de wagons à poser sur la route. => condition d'arrêt de la partie.
            self.current_player.wagons -= nb_segments

            # ajout de la route au joueur :
            self.current_player.route_prise.append([ville1, ville2])
            ihm_partie.ui.label_interaction_joueur.setText(
                f"Vous avez pris la route de {ville1} à {ville2}")
            time.sleep(10)

            # Suppression de la route de la liste des routes disponibles
            self.les_routes.remove(
                [ville1, ville2])  # FIXED: x not in list. Le format des données n'était pas respecté.

            # calcul des points gagnés :
            pts = Score(self).calcul_pts_route(self.current_player)
            ihm_partie.ui.score_joueur.setText(str(self.current_player.nb_points))
            print(f"Vous avez gagné {pts} points")
            ihm_partie.ui.label_interaction_joueur.setText(f"Vous avez gagné {pts} points !")

            # Affichage de la route gagnée:
            ihm_partie.update_route_prise()

            # Update de la main des cartes du joueur
            ihm_partie.ui.update_main_joueur()

            # On désactive les autres fonctionnalités du tour pour signaler la fin de tour
            return ihm_partie.fin_tour()

        # Si on prend la route avec le type de wagon choisi + des cartes locomotives :
        elif self.current_player.main_wagon[type_wagon] + self.current_player.main_wagon["locomotive"] >= nb_segments \
                and choix_locomotive:
            # défausse des cartes de la main vers la défausse
            for k in range(nb_locomotive):
                self.defausse_wagon.append("locomotive")
            for k in range(nb_segments - nb_locomotive):
                self.defausse_wagon.append(type_wagon)

            # retrait des wagons de la main du joueur :
            self.current_player.main_wagon["locomotive"] -= nb_locomotive
            self.current_player.main_wagon[type_wagon] -= nb_segments - nb_locomotive

            # ajout de la route au joueur :
            self.current_player.route_prise.append([ville1, ville2])
            ihm_partie.ui.label_interaction_joueur.setText(
                f"Vous avez pris la route de {ville1} à {ville2}")
            time.sleep(10)

            # Suppression de la route de la liste des routes disponibles
            self.les_routes.remove(
                [ville1, ville2])  # FIXED: x not in list. Le format des données n'était pas respecté.

            # calcul des points gagnés :
            pts = Score(self).calcul_pts_route(self.current_player)
            ihm_partie.ui.score_joueur.setText(str(self.current_player.nb_points))
            print(f"Vous avez gagné {pts} points")
            ihm_partie.ui.label_interaction_joueur.setText(f"Vous avez gagné {pts} points !")

            # Affichage de la route gagnée:
            ihm_partie.update_route_prise()

            # Update de la main des cartes du joueur
            ihm_partie.ui.update_main_joueur()

            # On désactive les autres fonctionnalités du tour pour signaler la fin de tour
            return ihm_partie.fin_tour()
        else:
            print("On ne peut pas prendre la route")
            ihm_partie.ui.label_interaction_joueur.setText(f"Vous ne pouvez pas prendre la route.")

    def preparation_partie(self):
        """
        Prépare la partie selon les règles.
        Préparation du jeu :
        Mélangez les cartes Wagon et distribuez-en 4 à chacun des joueurs. Placez le reste
        des cartes près du plateau, face cachée, puis retournez les cinq premières cartes que
        vous posez à côté, face visible.
        Posez la carte Chemin le plus long, face visible, à côté du plateau.
        Mélangez les cartes Destination et distribuez-en 3 à chaque joueur. Chaque joueur
        peut maintenant regarder ses destinations afin de décider lesquelles conserver. Il doit
        garder au moins 2 cartes, mais peut conserver les 3 s’il le souhaite. Chaque carte rendue
        est placée sous le talon des cartes Destination. Le paquet de cartes Destination est ensuite
        placé face cachée à côté du plateau. Les joueurs gardent leurs destinations secrètes
        jusqu’à la fin du jeu.
        Vous êtes maintenant prêts à jouer.
        :return:
        """
        self.pile_cartes_wagon = self.melange_cartes(self.pile_cartes_wagon)
        self.pile_cartes_wagon = self.melange_americain(self.pile_cartes_wagon)
        self.pile_cartes_destination = self.melange_cartes(self.pile_cartes_destination)
        self.pile_cartes_destination = self.melange_americain(self.pile_cartes_destination)
        for joueur in self.les_joueurs.values():
            for k in range(4):
                joueur.main_wagon[self.pile_cartes_wagon.pop(0)] += 1
            for i in range(3):
                joueur.main_destination.append(self.pile_cartes_destination.pop(0))
        self.init_les_routes()

    def change_current_player(self):
        """
        Incrémente l'index du joueur actuel en bouclant par rapport aux nb de joueurs. (%len(self.ordre))
        Renvoie le nom du joueur actuel suivant.
        """
        # Changement de joueur actuel
        self.idx_current_player += 1
        self.idx_current_player = self.idx_current_player % len(self.ordre)
        self.current_player_name = self.ordre[self.idx_current_player]
        self.current_player = self.les_joueurs[self.current_player_name]

    def change_turn(self, ihm_partie):
        """
        Change de tour de joueur actuel.
        Vérifie si ce n'est pas le dernier tour ou la fin de la partie.
        Lance l'action en fonction de ces conditions. (last_turn, end_game,turn)
        """
        if self.current_player.wagons < 2:
            self.LAST_TURN = True
            return self.last_turn(ihm_partie)
        if self.LAST_TURN and self.idx_current_player == len(self.ordre):
            return ihm_partie.fin_partie()
        self.change_current_player()
        self.turn(ihm_partie)

    def last_turn(self, ihm_partie):
        self.idx_current_player = self.ordre.index(self.current_player_name)
        self.rotation_joueur(self.idx_current_player)
        self.idx_current_player = self.ordre.index(self.current_player_name)
        self.change_current_player()
        self.turn(ihm_partie)

    def end_game(self, ihm_partie):
        """
        Fin de partie.
        Affiche le bouton pour finir la partie et bloque toutes les actions possibles par le joueur.
        Cache le bouton de fin de tour.
        """
        # Calcul des points finaux:
        # for joueur in self.les_joueurs.values():
        #     Score(self).calcul_pts_destinations(joueur)
        # ihm_partie.fin_partie()
        # Affichage du bouton Fin de Partie pour indiquer que la partie est finie.
        print("This is the endgame.")

    def turn(self, ihm_partie):
        """
        This is a turn.
        Lance le tour du joueur actuel et son IHM correspondant.
        """
        # initialisation des paramètres pour les actions du joueur
        self.count_wagon_card = 0
        ihm_partie.tour_joueur(self.current_player)
        print(f"Turn of {self.current_player.nom_joueur}")

    def partie(self, ihm_partie):
        """
        fait tourner une partie complète du jeu. du début à la fin.
        :return:
        """
        print("Préparation de la partie")
        self.debut_partie(ihm_partie)
        self.preparation_partie()
        """
        # Règle du jeu :
        ## Tour de jeu
        Le joueur qui a le plus voyagé commence."""
        self.choix_tour_joueur(ihm_partie)
        """Par la suite, on joue dans le sens des aiguilles d’une montre. 
        À son tour, le joueur doit faire une et une seule des trois actions suivantes : 
        1. Prendre des cartes Wagon
        2. Prendre possession d’une route
        3. Prendre des cartes Destination supplémentaires
        """
        self.idx_current_player = 0
        self.current_player_name = self.ordre[self.idx_current_player]
        self.current_player = self.les_joueurs[self.current_player_name]
        self.turn(ihm_partie)
        """
        Fin du jeu
        Lorsque la réserve de wagons d’un joueur est de 0, 1 ou 2 wagons après avoir joué son tour, 
        chaque joueur, en incluant celui-ci, joue encore un tour. À l’issue de ce dernier tour, le jeu s’arrête et 
        chacun compte ses points """

    def draw_plateau(self):
        """
        Définit le plateau du jeu
        => Construit le graphe des villes
        Affiche un point pour chaque ville avec le nom en dessous
        Relie chaque ville par un trait gris quand non occupé
        """
        figure = Figure()
        axes = figure.gca()
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        im = plt.imread("img/carte_usa.jpg")

        """Affichage des liens entre les villes :"""
        for nom_ville, ville in self.villes.items():
            x_ville, y_ville = ville.coords
            rx = 603 / 36
            ry = 380 / 23
            for nom_lien, value in ville.liens.items():
                couleur_lien, nb_wagons_lien = value
                x_liens, y_liens = self.villes[nom_lien].coords
                axes.plot((x_ville * rx, x_liens * rx), (y_ville * ry, y_liens * ry), color=couleur_lien, linewidth=5)
                # Pour les lignes en tirets : linestyle="dashed"
            axes.plot(x_ville * rx, y_ville * ry, 'ro')
            axes.text((x_ville - 1) * rx, (y_ville - 1) * ry, nom_ville)
        """Arrière-plan du plateau :"""
        # axes.imshow(im, extent=[1,36,1,22.7])
        # axes.imshow(im, extent=[0, 603, 0, 380])
        axes.imshow(im)
        axes.axis(False)
        # plt.show()
        # im = ax.imshow(im)
        # format image: 603x380
        # Grille pour les points du graphe: 36x22.5
        # Rapport : 1.6
        return figure

    def init_les_routes(self):
        for key in self.villes.keys():
            for lien in self.villes[key].liens.keys():
                if [key, lien][::-1] not in self.les_routes and [key, lien] not in self.les_routes:
                    self.les_routes.append([key, lien])  # format : [[ville1,ville2],...,[villeN,villeN+1]] en str

    def show_route_prise(self):
        """
        Définit le plateau du jeu
        => Construit le graphe des villes
        Affiche un point pour chaque ville avec le nom en dessous
        Relie chaque ville par un trait gris quand non occupé
        """
        figure = Figure()
        axes = figure.gca()
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        im = plt.imread("img/carte_usa.jpg")

        """Affichage des liens entre les villes :"""
        for joueur in self.les_joueurs.values():
            for route in joueur.route_prise:
                ville1, ville2 = route
                ville1, ville2 = self.villes[ville1], self.villes[ville2]
                x_ville, y_ville = ville1.coords
                x_lien, y_lien = ville2.coords
                rx = 603 / 36
                ry = 380 / 23
                axes.plot((x_ville * rx, x_lien * rx), (y_ville * ry, y_lien * ry), color=joueur.couleur, linewidth=5)
                axes.plot(x_ville * rx, y_ville * ry, 'ro')
                axes.text((x_ville - 1) * rx, (y_ville - 1) * ry, ville1.nom)

        """Arrière-plan du plateau :"""
        axes.imshow(im, extent=[0, 603, 0, 380])
        axes.axis(False)

        # format image: 603x380
        # Grille pour les points du graphe: 36x22.5
        # Rapport : 1.6
        return figure


# Imports :
from Joueur import *
from Score import Score
import matplotlib.pyplot as plt
import random as r
# from interface import IhmJoueur
from matplotlib.figure import Figure

if __name__ == '__main__':
    p = Partie_qt()
    j = Jeu()
    # p.update_choix_route()
    # p.partie()
    print("hello world")
    # p.show_plateau()
    # j.show_plateau()

    # # Test
    # from matplotlib.figure import Figure
    # from PyQt5 import QtWidgets
    # from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    # import sys
    #
    # app = QtWidgets.QApplication(sys.argv)
    #
    # # scene = QtWidgets.QGraphicsScene()
    # # view = QtWidgets.QGraphicsView(scene)
    #
    # canvas = FigureCanvas(p.show_plateau())
    # # proxy_widget = scene.addWidget(canvas)
    # # or
    # # proxy_widget = QtWidgets.QGraphicsProxyWidget()
    # # proxy_widget.setWidget(canvas)
    # # scene.addItem(proxy_widget)
    #
    # view=canvas
    # # view.resize(640, 480)
    # view.show()
    #
    # app.exec_()

# A conserver au cas où, pour plus tard :

# def prendre_cartes_Destination(self):
#     """
#     3. Prendre des cartes Destination supplémentaires :
#     – Le joueur prend 3 cartes Destination du dessus de la pioche. Il doit en conserver au moins une,
#     mais peut aussi garder 2 ou 3 cartes. Chaque carte qui n’est pas conservée est posée face cachée sous la pioche
#     des cartes Destination.
#     :return:
#     """
#
# """Indication Prendre des cartes Destination Un joueur peut utiliser son tour de jeu pour récupérer des cartes
# Destination supplémentaires. Pour cela, il doit prendre 3 cartes sur le dessus de la pile des cartes Destination.
# Il doit conserver au moins l’une des trois cartes, mais peut bien sûr en garder 2 ou même 3. S’il reste moins de 3
# cartes Destination dans la pile, le joueur ne peut prendre que le nombre de cartes disponibles. Chaque carte qui
# n’est pas conservée par le joueur est remise face cachée sous la pile. Chaque carte Destination fait référence à
# deux villes de la carte et un nombre de points y est associé. Si le joueur réalise la connexion entre les deux
# villes d’une carte Destination, il remporte le nombre de points indiqué sur la carte et l’additionne,
# en fin de partie, aux points déjà acquis. La route reliant ces deux villes doit être formée uniquement par les
# trains de ce joueur. Si la connexion n’est pas réalisée, le joueur déduit de son nombre de points déjà acquis le
# nombre indiqué sur la carte. Les cartes Destination sont gardées secrètes tout au long de la partie. Elles sont
# rendues publiques à la fin de la partie et chaque joueur calcule son score. Au cours du jeu, un joueur peut avoir
# autant de cartes Destination qu’il le souhaite. """
#
#     print("Je prends une carte Destination")
#     print("A implémenter")
#     return None
