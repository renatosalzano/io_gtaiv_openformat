
from .ofio.oft import Oft
from .ofio.mesh.mesh import Mesh

from .utils import path, debug
from .blender import context, test
from . import config

def import_oft(filepath = ""):

  testing = True

  if testing:

    test.print()
    return

  config.root_dir = path.dirname(filepath)
  config.filename = path.filename(filepath)
  config.is_vehicle = True

  src = f'{config.root_dir}/{config.filename}'

  if path.is_dir(src):
    context.clean_unused()
    config.main_collection = context.new_collection(config.filename)
  else:
    raise SystemError(f'missing directory "{config.filename}" in {filepath}')

  debug.log(f'import model at "{filepath}"')

  oft = Oft(filepath)

  lods = oft.drawable.lodgroup.get_lods()

  for lod, filepaths in lods.items():
    for filepath in filepaths:
      debug.log(f'import {lod}.mesh "{filepath}"')
      Mesh(filepath)
      

  context.clean_unused()
  pass
