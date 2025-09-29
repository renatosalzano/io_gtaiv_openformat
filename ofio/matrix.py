import mathutils
from ..utils.parser import ParserMethods
from ..utils import string, debug


class Matrix(ParserMethods):

  def __init__(this):

    this.matrix: list[tuple[float, float, float]] = []


  def set(this, _k, _v, item: list[str]):
    value = list(map(string.to_float, item))

    debug.log(f'[Matrix] set\n {value}')
    # print('SET F50', value)
    this.matrix.append(value)
    pass


  def get_matrix(this):

    r0, r1, r2, r3 = this.matrix
    tX, tY, tZ = r3 # translation

    # matrix = mathutils.Matrix()
    # matrix.Identity([3,4])

    ret = mathutils.Matrix((
      #  X  ,   Y  ,   Z  , Txyz
      (r0[0], r0[1], r0[2], -tX),
      (r1[0], r1[1], r1[2], -tY),
      (r2[0], r2[1], r2[2],  tZ),
      ( 0.0 ,  0.0 ,  0.0 , 1.0),
    ))

    debug.log(f'[Matrix] get\n {ret}')
    return ret