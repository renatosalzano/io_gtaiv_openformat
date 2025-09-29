from ...utils.parser import ParserMethods
from mathutils import Matrix

class BoundTransform(ParserMethods):

  def __init__(this):
    this.matrix = []

  def set(this, k, v, item):
    x, y, z = item

    this.matrix.append((
      float(x),
      float(y),
      float(z)
    ))
  

  def get_matrix(self):
    X, Y, Z, Txyz = self.matrix

    ret = Matrix((
    #  X    , Y    , Z    , Txyz
      (*X, Txyz[0]),
      (*Y, Txyz[1]),
      (*Z, Txyz[2]),
      (0.0, 0.0, 0.0, 1.0),
    ))
    return ret