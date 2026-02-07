"""
Représentation du réseau de métro parisien sous forme de graphe.
Matrice d'adjacence pondérée par les temps de trajet entre stations (en minutes).
"""

from math import atan2, cos, radians, sin, sqrt

from stations import N,get_station_by_id


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calcule la distance en km entre deux points GPS (formule de Haversine).
    """
    R = 6371  # Rayon de la Terre en km

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def estimate_travel_time(station1_id, station2_id, speed_kmh=30):
    station1 = get_station_by_id(station1_id)
    station2 = get_station_by_id(station2_id)
    d_km = haversine_distance(station1["lat"], station1["lon"], station2["lat"], station2["lon"])

    return (d_km/speed_kmh)*60.0 # unit: minute


def apply_crowding_penalty(current_hour):
    """
    Applique un facteur de congestion pour simuler les retards en heure de pointe.
    Le facteur est basé sur la fréquentation des stations (ex. plus fréquentées = plus de congestion).
    """
    crowding_factor_per_hour = {
        0: 0.5,  # 00:00 - 01:00
        1: 0.5,  # 01:00 - 02:00
        2: 0.5,  # 02:00 - 03:00
        3: 0.5,  # 03:00 - 04:00
        4: 0.5,  # 04:00 - 05:00
        5: 0.8,  # 05:00 - 06:00
        6: 1.0,  # 06:00 - 07:00
        7: 1.2,  # 07:00 - 08:00
        8: 1.5,  # 08:00 - 09:00
        9: 1.0,  # 09:00 - 10:00
        10: 0.8,  # 10:00 - 11:00
        11: 0.8,  # 11:00 - 12:00
        12: 0.8,  # 12:00 - 13:00
        13: 0.8,  # 13:00 - 14:00
        14: 0.8,  # 14:00 - 15:00
        15: 0.8,  # 15:00 - 16:00
        16: 1.0,  # 16:00 - 17:00
        17: 1.2,  # 17:00 - 18:00
        18: 1.5,  # 18:00 - 19:00
        19: 1.2,  # 19:00 - 20:00
        20: 0.8,  # 20:00 - 21:00
        21: 0.8,  # 21:00 - 22:00
        22: 0.5,  # 22:00 - 23:00
        23: 0.5,  # 23:00 - 00:00
    }

    # Récupérer l'heure actuelle (en heures) pour appliquer le facteur de congestion
    base_penalty = 0.5

    # Appliquer le facteur de congestion aux nombre de passagers max des stations pour estimer le temps de trajet supplémentaire
    # Calculez une heuristique de penalité basée sur la fréquentation des stations (ex. plus fréquentées = plus de pénalité)

    return 0.0  # Valeur par défaut (à remplacer par le calcul réel)


def apply_random_perturbation_penalty(station1_id, station2_id):
    """
    Applique une pénalité de perturbations aléatoires pour simuler les retards imprévus (ex. incidents, travaux).
    La pénalité est basée sur une probabilité d'incident et une durée moyenne de perturbation.
    """
    import random

    # Liste des perturbations possibles avec leur probabilité et facteur de gravité (en minutes de retard)
    PERTURBATIONS = [
        {
            "type": "incident_voyageur",
            "probability": 0.02,
            "severity": 5.0,
        },  # Malaise voyageur
        {
            "type": "colis_suspect",
            "probability": 0.01,
            "severity": 15.0,
        },  # Colis abandonné
        {
            "type": "panne_technique",
            "probability": 0.03,
            "severity": 8.0,
        },  # Panne de rame
        {
            "type": "affluence_exceptionnelle",
            "probability": 0.05,
            "severity": 3.0,
        },  # Forte affluence
        {
            "type": "travaux",
            "probability": 0.02,
            "severity": 10.0,
        },  # Travaux sur la ligne
        {
            "type": "signal_alarme",
            "probability": 0.04,
            "severity": 2.0,
        },  # Signal d'alarme tiré
        {
            "type": "incident_grave",
            "probability": 0.005,
            "severity": 30.0,
        },  # Incident grave (accident)
        {
            "type": "intemperies",
            "probability": 0.01,
            "severity": 7.0,
        },  # Conditions météo (inondation, etc.)
    ]

    # Utiliser la fonction random pour déterminer si une perturbation se produit et calculer la pénalité correspondante

    return 0.0  # Valeur par défaut (à remplacer par le calcul réel)


def heuristics(station1_id, station2_id, current_hour=8.0):
    return estimate_travel_time(station1_id, station2_id)

# Définition des connexions du réseau par ligne (identifiants des stations)
LIGNE_1 = [
    131,
    91,
    214,
    146,
    240,
    7,
    50,
    111,
    100,
    47,
    67,
    300,
    193,
    152,
    57,
    118,
    279,
    18,
    108,
    253,
    185,
    237,
    276,
    22,
    54,
]

LIGNE_2 = [
    222,
    305,
    50,
    296,
    74,
    180,
    310,
    259,
    206,
    26,
    204,
    6,
    16,
    129,
    291,
    123,
    65,
    20,
    75,
    174,
    198,
    201,
    2,
    12,
    185,
]

LIGNE_3 = [
    213,
    5,
    150,
    224,
    199,
    313,
    168,
    310,
    93,
    275,
    116,
    191,
    246,
    36,
    285,
    250,
    8,
    295,
    252,
    194,
    264,
    198,
    105,
    223,
    104,
]

LIGNE_3BIS = [105, 197, 270, 238]

LIGNE_4 = [
    228,
    289,
    170,
    55,
    16,
    109,
    107,
    53,
    292,
    250,
    92,
    145,
    57,
    63,
    278,
    189,
    273,
    283,
    281,
    182,
    304,
    249,
    83,
    184,
    3,
    221,
    159,
    15,
    13,
]

LIGNE_5 = [
    27,
    28,
    90,
    117,
    232,
    192,
    138,
    123,
    291,
    109,
    107,
    121,
    252,
    188,
    254,
    37,
    18,
    245,
    106,
    277,
    43,
    205,
]

LIGNE_6 = [
    50,
    128,
    29,
    299,
    195,
    25,
    85,
    134,
    42,
    288,
    196,
    182,
    89,
    249,
    83,
    274,
    112,
    71,
    205,
    186,
    61,
    244,
    21,
    84,
    82,
    19,
    202,
    185,
]

LIGNE_7 = [
    130,
    99,
    10,
    230,
    69,
    79,
    256,
    291,
    149,
    56,
    107,
    211,
    41,
    140,
    59,
    191,
    242,
    193,
    218,
    57,
    217,
    293,
    127,
    208,
    46,
    144,
    205,
]

LIGNE_7_VILLEJUIF = [205, 297, 163, 219, 139, 307, 309, 308]

LIGNE_7_IVRY = [163, 226, 220, 203, 157]

LIGNE_7BIS = [149, 123, 30, 39, 32, 207, 241]

LIGNE_7BIS_DANUBE = [32, 81, 241]

LIGNE_8 = [
    14,
    151,
    33,
    97,
    66,
    134,
    87,
    136,
    120,
    67,
    155,
    191,
    255,
    114,
    31,
    292,
    252,
    98,
    282,
    60,
    18,
    141,
    95,
    253,
    181,
    82,
    175,
    239,
    225,
    147,
    49,
    88,
    165,
    164,
    76,
    78,
    77,
    210,
]

LIGNE_9 = [
    216,
    24,
    171,
    233,
    94,
    177,
    176,
    122,
    248,
    135,
    261,
    299,
    119,
    4,
    100,
    280,
    179,
    266,
    116,
    59,
    255,
    114,
    31,
    292,
    252,
    188,
    265,
    312,
    52,
    262,
    185,
    40,
    169,
    231,
    257,
    80,
    160,
]

LIGNE_10 = [
    35,
    34,
    177,
    48,
    178,
    124,
    51,
    11,
    134,
    284,
    86,
    301,
    287,
    154,
    189,
    64,
    173,
    44,
    127,
    106,
]

LIGNE_11 = [
    57,
    118,
    247,
    8,
    252,
    113,
    20,
    243,
    125,
    207,
    294,
    238,
    162,
    286,
    258,
    183,
    132,
    72,
    260,
]

LIGNE_12 = [
    101,
    229,
    172,
    170,
    126,
    137,
    0,
    204,
    272,
    187,
    298,
    275,
    155,
    67,
    9,
    290,
    263,
    287,
    251,
    182,
    96,
    196,
    311,
    303,
    68,
    236,
    70,
    156,
]

LIGNE_13_SAINT_DENIS = [
    58,
    167,
    166,
    235,
    209,
    200,
    103,
    182,
    86,
    271,
    302,
    120,
    47,
    179,
    275,
    148,
    206,
    133,
]

LIGNE_13_ASNIERES = [133, 115, 234, 110, 161, 45, 268, 17, 269]

LIGNE_13_GABRIEL_PERI = [133, 38, 227, 158, 102, 142, 143]

LIGNE_14 = [
    267,
    161,
    227,
    212,
    275,
    155,
    242,
    57,
    108,
    21,
    73,
    23,
    190,
    163,
    306,
    62,
    153,
    215,
    1,
]

TOUTES_LES_LIGNES = [
    ("1", LIGNE_1),
    ("2", LIGNE_2),
    ("3", LIGNE_3),
    ("3bis", LIGNE_3BIS),
    ("4", LIGNE_4),
    ("5", LIGNE_5),
    ("6", LIGNE_6),
    ("7", LIGNE_7),
    ("7", LIGNE_7_VILLEJUIF),
    ("7", LIGNE_7_IVRY),
    ("7bis", LIGNE_7BIS),
    ("7bis", LIGNE_7BIS_DANUBE),
    ("8", LIGNE_8),
    ("9", LIGNE_9),
    ("10", LIGNE_10),
    ("11", LIGNE_11),
    ("12", LIGNE_12),
    ("13", LIGNE_13_SAINT_DENIS),
    ("13", LIGNE_13_ASNIERES),
    ("13", LIGNE_13_GABRIEL_PERI),
    ("14", LIGNE_14),
]


def build_adjacency_matrix():
    """
    Construit la matrice d'adjacence du réseau de métro.
    Les valeurs représentent le temps de trajet en minutes.
    0 signifie pas de connexion directe.

    Retourne une liste de listes (matrice N x N).
    """
    adjacency = [[0.0 for _ in range(N)] for _ in range(N)]

    for _, stations_ligne in TOUTES_LES_LIGNES:
        for i in range(len(stations_ligne) - 1):
            id1 = stations_ligne[i]
            id2 = stations_ligne[i + 1]

            travel_time = estimate_travel_time(id1, id2)

            if adjacency[id1][id2] == 0 or adjacency[id1][id2] > travel_time:
                adjacency[id1][id2] = travel_time
                adjacency[id2][id1] = travel_time

    return adjacency


# Matrice d'adjacence globale (calculée une seule fois)
ADJACENCY_MATRIX = None


def get_adjacency_matrix():
    """
    Retourne la matrice d'adjacence du réseau.
    """
    global ADJACENCY_MATRIX
    if ADJACENCY_MATRIX is None:
        ADJACENCY_MATRIX = build_adjacency_matrix()
    return ADJACENCY_MATRIX


def get_neighbors(station_id):
    """
    Retourne la liste des tuples (neighbor_id, temps de trajet entre station_id et neighbor_id).
    Format: [(station_id, temps_trajet), ...]
    """
    adjacency = get_adjacency_matrix()
    neighbors = []
    for i in range(N):
        if adjacency[station_id][i] > 0:
            neighbors.append((i, adjacency[station_id][i]))
    return neighbors
