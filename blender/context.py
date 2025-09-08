import bpy
from bpy.types import Collection, Object
from typing import Literal

def new_collection(name, append_to_scene = False, parent: Collection = None):
  # New Collection
  collection = bpy.data.collections.new(name)

  if parent:
    parent.children.link(collection)
  elif append_to_scene:
    bpy.context.scene.collection.children.link(collection)
    
  return collection


def clean_unused():
  bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=False)


def mode_set(mode: Literal['EDIT', 'OBJECT']):
  bpy.ops.object.mode_set(mode = mode.upper())


def select_all():
  bpy.ops.object.select_all(action='SELECT')


def deselect_all():
  bpy.ops.object.select_all(action='DESELECT')


def set_active(obj: Object):
  bpy.context.view_layer.objects.active = obj


def join():
  bpy.ops.object.join()