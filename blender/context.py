import bpy
from bpy.types import Collection, Object
from typing import Literal

def new_collection(name: str, append_to_scene = False, parent: Collection = None):
  # New Collection
  collection = bpy.data.collections.new(name)

  if parent:
    parent.children.link(collection)
  elif append_to_scene:
    bpy.context.scene.collection.children.link(collection)
    
  return collection


def get_collection(name: str):
  return bpy.data.collections.get(name)


def delete_hierarchy():
  bpy.ops.outliner.delete(hierarchy=True)


def select_collection(name: str):
  deselect_all()
  bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[name]


def clean_unused():
  bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=False)


def mode_set(mode: Literal['EDIT', 'OBJECT']):
  bpy.ops.object.mode_set(mode = mode.upper())


def select_all():
  bpy.ops.object.select_all(action='SELECT')


def deselect_all():
  bpy.ops.object.select_all(action='DESELECT')


def set_active(obj: Object):

  if not obj.users_collection:
    bpy.context.collection.objects.link(obj)

  bpy.context.view_layer.objects.active = obj


def join():
  bpy.ops.object.join()


def set_parent(_from: Object, to: Object):
  
  if not isinstance(to, Object):
    return

  deselect_all()
  set_active(_from)
  to.select_set(state=True)
  
  bpy.ops.object.parent_set(type='OBJECT')


def create_empty(name: str, location: list[float]):
  bpy.ops.object.empty_add(type='SINGLE_ARROW', location=location)
  empty_object = bpy.context.object
  empty_object.name = name
  empty_object.empty_display_size = 0.1

  return empty_object


def shade_smooth():
  select_all()
  bpy.ops.object.shade_smooth()
  deselect_all()
