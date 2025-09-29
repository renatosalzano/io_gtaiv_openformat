
from ..utils.parser import ParserMethods
from ..utils import debug
from .matrix import Matrix
import mathutils

class ChildStruct(ParserMethods):

  def __init__(this):
    this.pristineMass = 0.0
    this.damagedMass = 0.0
    this.f50: Matrix = None

    this._parent: ChildStruct | None = None
    this._transform: mathutils.Matrix = None





def invert_matrix(matrix: mathutils.Matrix):
  x, y, z = matrix.translation

  return mathutils.Matrix().Translation((-x, -y, z))