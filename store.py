from bpy import types
from .blender.material import Material 

root_dir = ""
filename = ""

main_collection: types.Collection = None

is_vehicle = False
bones_map: dict[str, str] = {}

materials: list[Material] = []

def get_bone_name(index: int):

  index = index if isinstance(index, int) else int(index)

  return bones_map[index]


def get_material(index: int):

  if index < len(materials):
    return materials[index]
  else:
    breakpoint()
    print(f'{index} out of range {len(materials) - 1}')