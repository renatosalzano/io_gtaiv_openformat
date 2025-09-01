from .fragments import Fragments
from ..utils.parser import Parser, ParserMethods
from ..utils import debug

class Oft(ParserMethods):

  def __init__(this, filepath: str = ''):

    this.Version = '112 2'
    this.fragments = Fragments()
    this.drawable = {}
    this.f8 = {}

    Parser(filepath, this)

    debug.debug_object(this)
    print('END')

    pass




