
from .ofio.oft import Oft
from .ofio.mesh.mesh import Mesh

from .utils import debug

def import_oft(filepath = ""):

  debug.log(f'import file: {filepath}')
  oft = Oft(filepath)

  lods = oft.drawable.lodgroup.get_lods()

  for lod, filepaths in lods.items():
    for filepath in filepaths:
      Mesh(filepath)

  # breakpoint()
  pass
