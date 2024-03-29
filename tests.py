import utils
from random import randint


def test_verif_etage_critique(function: callable):

    utils._set_values(etages=10, critique=2, oeufs=float("inf"))
    assert function(utils._critique) == True

    utils._set_values(critique=randint(3, 100))
    assert function(utils._critique - 1) == False
    assert function(utils._critique) == True
    assert function(utils._critique + 1) == False


def test_critique_un_seul_oeuf(function: callable):
    utils._set_values(etages=10, critique=1, oeufs=1)
    assert function(utils._etages) == 1

    utils._set_values(etages=100, critique=randint(2, 100), oeufs=1)
    assert function(utils._etages) == utils._critique

    utils._set_values(etages=10, critique=100, oeufs=1)
    assert function(utils._etages) == 11


def test_critique_dichotomie(function: callable):
    utils._set_values(etages=1, critique=1, oeufs=1)
    assert function(utils._etages) == 1

    utils._set_values(etages=100, critique=randint(2, 100), oeufs=100)
    assert function(utils._etages) == utils._critique

    utils._set_values(etages=10, critique=100, oeufs=10)
    assert function(utils._etages) == 11


def test_L(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_Lprec(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_strategie(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_faces(function: callable):
    assert function((0, 0, 0)) == [
        [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0)],
        [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 1)],
        [(0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1)],
        [(0, 1, 0), (0, 1, 1), (1, 1, 0), (1, 1, 1)],
        [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1)],
        [(1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)],
    ]
    assert function((4, -5, 1)) == [
        [(4, -5, 1), (4, -4, 1), (5, -5, 1), (5, -4, 1)],
        [(4, -5, 2), (4, -4, 2), (5, -5, 2), (5, -4, 2)],
        [(4, -5, 1), (4, -5, 2), (5, -5, 1), (5, -5, 2)],
        [(4, -4, 1), (4, -4, 2), (5, -4, 1), (5, -4, 2)],
        [(4, -5, 1), (4, -5, 2), (4, -4, 1), (4, -4, 2)],
        [(5, -5, 1), (5, -5, 2), (5, -4, 1), (5, -4, 2)],
    ]


def test_nb_faces_visibles(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_surface_externe(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_voisins(function: callable):
    x, y, z = randint(-100, 100), randint(-100, 100), randint(-100, 100)
    assert len(function((x, y, z))) == 26
    assert (x, y, z) not in function((x, y, z))
    assert function((x, y, z)) == [
        (x - 1, y - 1, z - 1),
        (x - 1, y - 1, z),
        (x - 1, y - 1, z + 1),
        (x - 1, y, z - 1),
        (x - 1, y, z),
        (x - 1, y, z + 1),
        (x - 1, y + 1, z - 1),
        (x - 1, y + 1, z),
        (x - 1, y + 1, z + 1),
        (x, y - 1, z - 1),
        (x, y - 1, z),
        (x, y - 1, z + 1),
        (x, y, z - 1),
        (x, y, z + 1),
        (x, y + 1, z - 1),
        (x, y + 1, z),
        (x, y + 1, z + 1),
        (x + 1, y - 1, z - 1),
        (x + 1, y - 1, z),
        (x + 1, y - 1, z + 1),
        (x + 1, y, z - 1),
        (x + 1, y, z),
        (x + 1, y, z + 1),
        (x + 1, y + 1, z - 1),
        (x + 1, y + 1, z),
        (x + 1, y + 1, z + 1),
    ]


def test_evolution(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_faces_adjacentes_sommet(function: callable):
    F = [[0, 1, 2, 3], [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4]]
    assert function(F, 0) == [[0, 1, 2, 3], [0, 1, 4], [3, 0, 4]]


def test_faces_adjacentes_cote(function: callable):
    F = [[0, 1, 2, 3], [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4]]
    assert function(F, 0) == [[0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4]]


def test_triangule(function: callable):  # TODO
    raise ValueError("The test function isn't done yet.")


def test_variables(b, f):
    raise ValueError("The test function isn't done yet.")


def test_valide_sommet(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_valide_face(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_valide_darete(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_faces_voisines(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_composante_connexe(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_separe_face(function: callable):
    raise ValueError("The test function isn't done yet.")


def test_serialise(function: callable):
    raise ValueError("The test function isn't done yet.")
