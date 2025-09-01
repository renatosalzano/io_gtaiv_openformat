from mathutils import Matrix
from ..utils.parser import ParserMethods
from ..utils import string


class F50(ParserMethods):

  def __init__(this):

    this.matrix: list[tuple[float, float, float]] = []


  def set(this, _k, _v, item: list[str]):
    value = list(map(string.to_float, item))
    print('SET F50', value)
    this.matrix.append(value)
    pass


  def get_matrix(self):
    X, Y, Z, Txyz = self.matrix

    matrix = Matrix((
    #  X    , Y    , Z    , Txyz
      (*X, -Txyz[0]),
      (*Y, -Txyz[1]),
      (*Z, Txyz[2]),
      (0.0, 0.0, 0.0, 1.0),
    ))
    return matrix