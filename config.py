from bpy import types

root_dir = ""
filename = ""

main_collection: types.Collection = None

is_vehicle = False
bones_map: dict[str, str] = {}

def get_bone_name(index: int):

  index = index if isinstance(index, int) else int(index)

  return bones_map[index]