"""Projet Informatique
@authors: Mathis URIEN, Kenza BELAID"""

# Imports :
from abc import abstractmethod, ABCMeta, ABC
import random as rd


class Joueur:
    """
    Classe qui définit les attributs et cartes du joueur d'une partie.
    Il y aura ici les joueurs IA et humains. A nous de les définir comme on le souhaite.
    """
    Couleur_joueur = ['aliceblue',
                      'antiquewhite',
                      'aqua',
                      'aquamarine',
                      'azure',
                      'beige',
                      'bisque',
                      'black',
                      'blanchedalmond',
                      'blue',
                      'blueviolet',
                      'brown',
                      'burlywood',
                      'cadetblue',
                      'chartreuse',
                      'chocolate',
                      'coral',
                      'cornflowerblue',
                      'cornsilk',
                      'crimson',
                      'cyan',
                      'darkblue',
                      'darkcyan',
                      'darkgoldenrod',
                      'darkgray',
                      'darkgreen',
                      'darkgrey',
                      'darkkhaki',
                      'darkmagenta',
                      'darkolivegreen',
                      'darkorange',
                      'darkorchid',
                      'darkred',
                      'darksalmon',
                      'darkseagreen',
                      'darkslateblue',
                      'darkslategray',
                      'darkslategrey',
                      'darkturquoise',
                      'darkviolet',
                      'deeppink',
                      'deepskyblue',
                      'dimgray',
                      'dimgrey',
                      'dodgerblue',
                      'firebrick',
                      'floralwhite',
                      'forestgreen',
                      'fuchsia',
                      'gainsboro',
                      'ghostwhite',
                      'gold',
                      'goldenrod',
                      'gray',
                      'grey',
                      'green',
                      'greenyellow',
                      'honeydew',
                      'hotpink',
                      'indianred',
                      'indigo',
                      'ivory',
                      'khaki',
                      'lavender',
                      'lavenderblush',
                      'lawngreen',
                      'lemonchiffon',
                      'lightblue',
                      'lightcoral',
                      'lightcyan',
                      'lightgoldenrodyellow',
                      'lightgray',
                      'lightgreen',
                      'lightgrey',
                      'lightpink',
                      'lightsalmon',
                      'lightseagreen',
                      'lightskyblue',
                      'lightslategray',
                      'lightslategrey',
                      'lightsteelblue',
                      'lightyellow',
                      'lime',
                      'limegreen',
                      'linen',
                      'magenta',
                      'maroon',
                      'mediumaquamarine',
                      'mediumblue',
                      'mediumorchid',
                      'mediumpurple',
                      'mediumseagreen',
                      'mediumslateblue',
                      'mediumspringgreen',
                      'mediumturquoise',
                      'mediumvioletred',
                      'midnightblue',
                      'mintcream',
                      'mistyrose',
                      'moccasin',
                      'navajowhite',
                      'navy',
                      'oldlace',
                      'olive',
                      'olivedrab',
                      'orange',
                      'orangered',
                      'orchid',
                      'palegoldenrod',
                      'palegreen',
                      'paleturquoise',
                      'palevioletred',
                      'papayawhip',
                      'peachpuff',
                      'peru',
                      'pink',
                      'plum',
                      'powderblue',
                      'purple',
                      'red',
                      'rosybrown',
                      'royalblue',
                      'saddlebrown',
                      'salmon',
                      'sandybrown',
                      'seagreen',
                      'seashell',
                      'sienna',
                      'silver',
                      'skyblue',
                      'slateblue',
                      'slategray',
                      'slategrey',
                      'snow',
                      'springgreen',
                      'steelblue',
                      'tan',
                      'teal',
                      'thistle',
                      'tomato',
                      'turquoise',
                      'violet',
                      'wheat',
                      'white',
                      'whitesmoke',
                      'yellow',
                      'yellowgreen']
    convert_color_id = {
        "blanc": "white",
        "bleu": "blue",
        "rouge": "red",
        "vert": "green",
        "jaune": "yellow",
        "orange": "orange",
        "noir": "black",
        "rose": "pink",
        "personnalisée": "random"  # TODO: à modifier dans la phase améliorations. => color picker.
    }

    # DONE: insérer toutes les couleurs possibles => cf. matplotlib.pyplot par exemple ou docs de pygame
    def __init__(self, nom_joueur, nom_couleur, points=0):
        self.nom_joueur: str = nom_joueur  # Nom du joueur
        self.wagons = 45  # Nombre de wagons maximum par joueur
        self.couleur = nom_couleur  # Définit la couleur du joueur
        self.nb_points = points  # Définit le marqueur de points du joueur
        self.__main_wagon = {
            "white": 0,
            "blue": 0,
            "yellow": 0,
            "black": 0,
            "orange": 0,
            "pink": 0,
            "red": 0,
            "green": 0,
            "locomotive": 0
        }
        self.main_destination = []  # Réunit toutes les cartes Objectifs/Destination du joueur. Ne contient que les
        # noms des cartes.
        self.route_prise = []  # Format: [[ville1,ville2],[],...]
        self.IA = False  # Permet de savoir si le joueur est un ordi ou non

    # DONE: if color = random alors assigner une couleur random

    @property
    def main_wagon(self):
        """Accesseur en lecture"""
        return self.__main_wagon

    def add_main_wagon(self, couleur, value):
        """Accesseur de main_cartes"""
        if self.__main_wagon[couleur] <= 0:
            self.__main_wagon[couleur] = 0
        else:
            self.__main_wagon[couleur] += value

    @property
    def couleur(self):
        """
        Accesseur de la variable couleur
        :return: valeur de couleur
        """
        return self.__couleur

    @couleur.setter
    def couleur(self, nom_couleur: str):
        """
        Définit la valeur du paramètre et vérifie les conditions de définition
        :param nom_couleur: str
        :return: None
        """
        assert type(nom_couleur) == str
        if nom_couleur in self.convert_color_id.keys():
            nom_couleur = self.convert_color_id[nom_couleur]
        if "random" in nom_couleur:
            self.__couleur = self.Couleur_joueur.pop(rd.randint(0, len(self.Couleur_joueur) - 1))
        else:
            self.__couleur = nom_couleur
            self.Couleur_joueur.pop(self.Couleur_joueur.index(nom_couleur))


class IA_player(Joueur):
    """Classe qui contient plusieurs modèles de joueurs IAs. A voir selon l'implémentation."""

    def __init__(self, nom_joueur="IA player", nom_couleur="random", IA_level="IA aléatoire", points=0):
        super().__init__(nom_joueur, nom_couleur, points)
        # Difficulté de l'IA : échelle de 0 à 3. IA novice, IA normal, IA expert.
        # Pour IA aléatoire : difficulty = 0.
        self.levels = {
            "IA aléatoire": 0,
            "IA novice": 1,
            "IA normal": 2,
            "IA expert": 3,
        }
        self.difficulty = IA_level

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        self._difficulty = self.levels[value]

    def prendre_wagon(self, partie):
        """
        Fonction pour réaliser l'action "prendre des cartes wagons" pour l'IA de niveau aléatoire.
        """
        if self.difficulty == 0:
            print("prendre_wagon: difficulty 0")
            choix = rd.randint(0, 5)
            partie.prendre_cartes_wagon(choix, choix != 5)

        # A compléter

    def prendre_route(self):
        """
        Fonction pour réaliser l'action "prendre des cartes wagons" pour l'IA de niveau aléatoire.
        """
        if self.difficulty == 0:
            print("prendre_route: difficulty 0")
        # A compléter
        pass

    def prendre_destinations(self):
        """
        Fonction pour réaliser l'action "prendre des cartes wagons" pour l'IA de niveau aléatoire.
        """
        if self.difficulty == 0:
            print("difficulty 0")
        # A compléter
        pass

    def tour(self, partie):
        """
        Réalise le tour de l'IA. Prend en compte le level défini. Les actions sont en fonction.
        """
        if self.difficulty == 0:
            choix = rd.randint(1, 3)
            if choix == 1:
                partie.count_wagon_card = 0
                self.prendre_wagon()
            if choix == 2:
                self.prendre_route()
            if choix == 3:
                self.prendre_destinations()
        # A compléter pour les autres niveaux.


if __name__ == '__main__':
    j = IA_player()
    # for k in range(100):
    #     print(IA_player().main_wagon["grey"])

# Couleurs possibles par pygame :
# Couleur_joueur = ['aliceblue', 'antiquewhite', 'antiquewhite1', 'antiquewhite2', 'antiquewhite3', 'antiquewhite4',
#                       'aqua', 'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'azure',
#                       'azure1', 'azure3', 'azure2', 'azure4', 'beige', 'bisque', 'bisque1', 'bisque2', 'bisque3',
#                       'bisque4', 'black', 'blanchedalmond', 'blue', 'blue1', 'blue2', 'blue3', 'blue4', 'blueviolet',
#                       'brown', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood', 'burlywood1', 'burlywood2',
#                       'burlywood3', 'burlywood4', 'cadetblue', 'cadetblue1', 'cadetblue2', 'cadetblue3', 'cadetblue4',
#                       'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate',
#                       'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3',
#                       'coral4', 'cornflowerblue', 'cornsilk', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4',
#                       'crimson', 'cyan', 'cyan1', 'cyan2', 'cyan3', 'cyan4', 'darkblue', 'darkcyan', 'darkgoldenrod',
#                       'darkgoldenrod1', 'darkgoldenrod2', 'darkgoldenrod3', 'darkgoldenrod4', 'darkgray', 'darkgreen',
#                       'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkolivegreen1', 'darkolivegreen2',
#                       'darkolivegreen3', 'darkolivegreen4', 'darkorange', 'darkorange1', 'darkorange2', 'darkorange3',
#                       'darkorange4', 'darkorchid', 'darkorchid1', 'darkorchid2', 'darkorchid3', 'darkorchid4',
#                       'darkred', 'darksalmon', 'darkseagreen', 'darkseagreen1', 'darkseagreen2', 'darkseagreen3',
#                       'darkseagreen4', 'darkslateblue', 'darkslategray', 'darkslategray1', 'darkslategray2',
#                       'darkslategray3', 'darkslategray4', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink',
#                       'deeppink1', 'deeppink2', 'deeppink3', 'deeppink4', 'deepskyblue', 'deepskyblue1', 'deepskyblue2',
#                       'deepskyblue3', 'deepskyblue4', 'dimgray', 'dimgrey', 'dodgerblue', 'dodgerblue1', 'dodgerblue2',
#                       'dodgerblue3', 'dodgerblue4', 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4',
#                       'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'gold1', 'gold2',
#                       'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'gray',
#                       'gray0', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9',
#                       'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18',
#                       'gray19', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27',
#                       'gray28', 'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36',
#                       'gray37', 'gray38', 'gray39', 'gray40', 'gray41', 'gray42', 'gray43', 'gray44', 'gray45',
#                       'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54',
#                       'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63',
#                       'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72',
#                       'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81',
#                       'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90',
#                       'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray96', 'gray97', 'gray98', 'gray99',
#                       'gray100', 'green', 'green1', 'green2', 'green3', 'green4', 'greenyellow', 'grey', 'grey0',
#                       'grey1', 'grey2', 'grey3', 'grey4', 'grey5', 'grey6', 'grey7', 'grey8', 'grey9', 'grey10',
#                       'grey11', 'grey12', 'grey13', 'grey14', 'grey15', 'grey16', 'grey17', 'grey18', 'grey19',
#                       'grey20', 'grey21', 'grey22', 'grey23', 'grey24', 'grey25', 'grey26', 'grey27', 'grey28',
#                       'grey29', 'grey30', 'grey31', 'grey32', 'grey33', 'grey34', 'grey35', 'grey36', 'grey37',
#                       'grey38', 'grey39', 'grey40', 'grey41', 'grey42', 'grey43', 'grey44', 'grey45', 'grey46',
#                       'grey47', 'grey48', 'grey49', 'grey50', 'grey51', 'grey52', 'grey53', 'grey54', 'grey55',
#                       'grey56', 'grey57', 'grey58', 'grey59', 'grey60', 'grey61', 'grey62', 'grey63', 'grey64',
#                       'grey65', 'grey66', 'grey67', 'grey68', 'grey69', 'grey70', 'grey71', 'grey72', 'grey73',
#                       'grey74', 'grey75', 'grey76', 'grey77', 'grey78', 'grey79', 'grey80', 'grey81', 'grey82',
#                       'grey83', 'grey84', 'grey85', 'grey86', 'grey87', 'grey88', 'grey89', 'grey90', 'grey91',
#                       'grey92', 'grey93', 'grey94', 'grey95', 'grey96', 'grey97', 'grey98', 'grey99', 'grey100',
#                       'honeydew', 'honeydew1', 'honeydew2', 'honeydew3', 'honeydew4', 'hotpink', 'hotpink1', 'hotpink2',
#                       'hotpink3', 'hotpink4', 'indianred', 'indianred1', 'indianred2', 'indianred3', 'indianred4',
#                       'indigo', 'ivory', 'ivory1', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3',
#                       'khaki4', 'lavender', 'lavenderblush', 'lavenderblush1', 'lavenderblush2', 'lavenderblush3',
#                       'lavenderblush4', 'lawngreen', 'lemonchiffon', 'lemonchiffon1', 'lemonchiffon2', 'lemonchiffon3',
#                       'lemonchiffon4', 'lightblue', 'lightblue1', 'lightblue2', 'lightblue3', 'lightblue4',
#                       'lightcoral', 'lightcyan', 'lightcyan1', 'lightcyan2', 'lightcyan3', 'lightcyan4',
#                       'lightgoldenrod', 'lightgoldenrod1', 'lightgoldenrod2', 'lightgoldenrod3', 'lightgoldenrod4',
#                       'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightpink1',
#                       'lightpink2', 'lightpink3', 'lightpink4', 'lightsalmon', 'lightsalmon1', 'lightsalmon2',
#                       'lightsalmon3', 'lightsalmon4', 'lightseagreen', 'lightskyblue', 'lightskyblue1', 'lightskyblue2',
#                       'lightskyblue3', 'lightskyblue4', 'lightslateblue', 'lightslategray', 'lightslategrey',
#                       'lightsteelblue', 'lightsteelblue1', 'lightsteelblue2', 'lightsteelblue3', 'lightsteelblue4',
#                       'lightyellow', 'lightyellow1', 'lightyellow2', 'lightyellow3', 'lightyellow4', 'linen', 'lime',
#                       'limegreen', 'magenta', 'magenta1', 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1',
#                       'maroon2', 'maroon3', 'maroon4', 'mediumaquamarine', 'mediumblue', 'mediumorchid',
#                       'mediumorchid1', 'mediumorchid2', 'mediumorchid3', 'mediumorchid4', 'mediumpurple',
#                       'mediumpurple1', 'mediumpurple2', 'mediumpurple3', 'mediumpurple4', 'mediumseagreen',
#                       'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue',
#                       'mintcream', 'mistyrose', 'mistyrose1', 'mistyrose2', 'mistyrose3', 'mistyrose4', 'moccasin',
#                       'navajowhite', 'navajowhite1', 'navajowhite2', 'navajowhite3', 'navajowhite4', 'navy', 'navyblue',
#                       'oldlace', 'olive', 'olivedrab', 'olivedrab1', 'olivedrab2', 'olivedrab3', 'olivedrab4', 'orange',
#                       'orange1', 'orange2', 'orange3', 'orange4', 'orangered', 'orangered1', 'orangered2', 'orangered3',
#                       'orangered4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'palegreen', 'palegreen1',
#                       'palegreen2', 'palegreen3', 'palegreen4', 'palegoldenrod', 'paleturquoise', 'paleturquoise1',
#                       'paleturquoise2', 'paleturquoise3', 'paleturquoise4', 'palevioletred', 'palevioletred1',
#                       'palevioletred2', 'palevioletred3', 'palevioletred4', 'papayawhip', 'peachpuff', 'peachpuff1',
#                       'peachpuff2', 'peachpuff3', 'peachpuff4', 'peru', 'pink', 'pink1', 'pink2', 'pink3', 'pink4',
#                       'plum', 'plum1', 'plum2', 'plum3', 'plum4', 'powderblue', 'purple', 'purple1', 'purple2',
#                       'purple3', 'purple4', 'red', 'red1', 'red2', 'red3', 'red4', 'rosybrown', 'rosybrown1',
#                       'rosybrown2', 'rosybrown3', 'rosybrown4', 'royalblue', 'royalblue1', 'royalblue2', 'royalblue3',
#                       'royalblue4', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'saddlebrown', 'sandybrown',
#                       'seagreen', 'seagreen1', 'seagreen2', 'seagreen3', 'seagreen4', 'seashell', 'seashell1',
#                       'seashell2', 'seashell3', 'seashell4', 'sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4',
#                       'silver', 'skyblue', 'skyblue1', 'skyblue2', 'skyblue3', 'skyblue4', 'slateblue', 'slateblue1',
#                       'slateblue2', 'slateblue3', 'slateblue4', 'slategray', 'slategray1', 'slategray2', 'slategray3',
#                       'slategray4', 'slategrey', 'snow', 'snow1', 'snow2', 'snow3', 'snow4', 'springgreen',
#                       'springgreen1', 'springgreen2', 'springgreen3', 'springgreen4', 'steelblue', 'steelblue1',
#                       'steelblue2', 'steelblue3', 'steelblue4', 'tan', 'tan1', 'tan2', 'tan3', 'tan4', 'teal',
#                       'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato1', 'tomato2',
#                       'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4',
#                       'violet', 'violetred', 'violetred1', 'violetred2', 'violetred3', 'violetred4', 'wheat', 'wheat1',
#                       'wheat2', 'wheat3', 'wheat4', 'white', 'whitesmoke', 'yellow', 'yellow1', 'yellow2', 'yellow3',
#                       'yellow4', 'yellowgreen']
