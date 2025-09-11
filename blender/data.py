import bpy

def load_image(path: str):
  return bpy.data.images.load(path)


def get_image(filename: str):
  return bpy.data.images.get(filename)


def has_image(filename):
  return filename in bpy.data.images