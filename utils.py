_nombre_etages = 10
_etage_critique = 5
_nombre_oeufs = 10

Infty = float("inf")

def lacher(n):
    if not isinstance(n, int):
        raise ValueError("n must be of type 'int'.")
    if n <= 0:
        raise ValueError("n must be greater than 0")
    return n >= _etage_critique

class Sommet:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.darete = None # à remplir plus tard

class Face:
    def __init__(self):
        self.darete = None # à remplir plus tard

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
        self.suivant = None # à remplir plus tard
        self.miroir = None # à remplir plus tard

def sql_execute(request): ... # TODO
