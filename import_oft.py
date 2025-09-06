
from .ofio.oft import Oft
from .utils import debug

def import_oft(filepath = ""):

  debug.log(f'import file: {filepath}')
  oft = Oft(filepath)

  pass
