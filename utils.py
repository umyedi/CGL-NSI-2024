_etages = 10  # Nombre d'étages de l'immeuble
_critique = 5  # Plus petit étage pour lequel l'oeufs se casse
_oeufs = 10  # Nombre d'oeufs disponibles


def _set_values(etages=None, critique=None, oeufs=None):
    global _etages, _critique, _oeufs
    if etages:
        _etages = etages
    if critique:
        _critique = critique
    if oeufs:
        _oeufs = oeufs


Infty = float("inf")


def lacher(n):
    global _oeufs, _critique

    if not isinstance(n, int):
        raise ValueError("n must be of type 'int'.")
    if n <= 0:
        raise ValueError("n must be greater than 0")

    if n >= _critique:
        if _oeufs == 0:
            raise ValueError("Vous n'avez plus d'oeufs à lancer")

        _oeufs -= 1
        return True

    return False


class Sommet:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.darete = None  # à remplir plus tard


class Face:
    def __init__(self):
        self.darete = None  # à remplir plus tard


class DArete:
    def __init__(self, source, but, face):
        # si la face n'a pas encore de demi-arête associée
        # on utilise celle-ci
        if face.darete is None:
            face.darete = self
        # si le sommet source n'a pas encore de demi-arête
        # associée on utilise celle-ci
        if source.darete is None:
            source.darete = self
        self.source = source
        self.but = but
        self.face = face
        self.suivant = None  # à remplir plus tard
        self.miroir = None  # à remplir plus tard


def sql_execute(request): ...  # TODO
