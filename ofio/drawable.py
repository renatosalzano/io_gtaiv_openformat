from ..utils.parser import ParserMethods
from .shadinggroup import Shadinggroup

class Drawable(ParserMethods):

  def __init__(this):
    this.shadinggroup = Shadinggroup()
    this.skel = {}
    this.lodgroup = {}