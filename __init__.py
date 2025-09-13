# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from . import store
from .utils import path

from bpy.types import Context
from bpy_extras.io_utils import (
    ImportHelper,
    ExportHelper,
    orientation_helper,
    axis_conversion,
)
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    StringProperty,
)
# from .archive.custom_panel import GTAIV_PT_panel, ToggleOperator
import bpy
import os

bl_info = {
  "name" : "io_gtaiv_openformats",
  "author" : "Magico",
  "description" : "",
  "blender" : (4, 0, 0),
  "version" : (0, 0, 1),
  "location" : "File > Import-Export",
  "warning" : "",
  "category" : "Import - Export"
}


def get_version(filepath):
  file = open(filepath, 'r')
  version = file.readline().replace("\n", "").split(" ")
  version.pop(0)
  version = " ".join(version)

  file.close()
  return version


class GTAIVOF_OP_import(bpy.types.Operator, ImportHelper):
  """Import GTAIV OpenFormat (.oft, .odd, .odr)"""
  bl_idname = "import_scene.oft"
  bl_label = 'Import GTA IV OpenFormat'
  bl_options = {'PRESET', 'UNDO'}

  # filter extension
  filepath = ''
  filename_ext = ".oft"
  filter_glob: StringProperty(default="*.oft;*.odd", options={'HIDDEN'})
  import_col: BoolProperty(
      name="Import Collision",
      description="Import collision mesh",
      default=False,
    )

  
  def draw(self, context):
    pass
    
  def execute(this, context):

    ext = path.ext(this.filepath)

    store.filename = path.filename(this.filepath)
    store.root_dir = path.dirname(this.filepath)

    match ext:
      
      case ".oft":
        from .import_oft import import_oft
        import_oft(filepath=this.filepath)

      case ".odd":
        pass
        # version = get_version(self.filepath)
        # match version:
        #   case "110 12":
        #     from . import import_odd
        #     import_odd.import_odd(self.filepath)

    return {'FINISHED'}
   

class OFT_PT_import(bpy.types.Panel):
  bl_space_type = 'FILE_BROWSER'
  bl_region_type = 'TOOL_PROPS'
  bl_label = ""
  bl_parent_id = "FILE_PT_operator"
  bl_options = {'HIDE_HEADER'}
  
  @classmethod
  def poll(cls, context):
    sfile = context.space_data
    operator = sfile.active_operator

    return operator.bl_idname == "IMPORT_SCENE_OT_oft"
  
  def draw(self, context):
    layout = self.layout
    # layout.use_property_split = True
    # layout.use_property_decorate = False  # No animation.
    sfile = context.space_data
    operator = sfile.active_operator

    box = layout.box()
    row = box.row()
    row.prop(operator, "import_col")

    
    # operator = sfile.active_operator
    # row = layout.row()

    # layout.prop(operator, "import_col")



class GTAIVOF_OP_export(bpy.types.Operator, ImportHelper):
  """Export GTA IV in multiple part"""
  bl_idname = "export_scene.ofio"
  bl_label = "Export GTA IV OFIO"
  bl_options = {'PRESET', 'UNDO'}

  # filter extension
  # filename_ext = ".oft"
  # filter_glob: StringProperty(default="*.oft", options={'HIDDEN'})


  def draw(self, context):
    pass

  def execute(self, context):
    from . import export_oft, export_odd

    try:
      collection = bpy.data.collections.get(bpy.context.collection.name)
      gta_iv_data = collection.get("gta_iv_data").to_dict()

    except:
      print("collection not found")
      return {'FINISHED'}
    
    store.collection = bpy.context.collection
    store.export_path = self.filepath
    
    match gta_iv_data["type"]:
      case "odd":
        export_odd.export_odd(gta_iv_data)
      case "oft":
        export_oft.export_oft(gta_iv_data)
    
    return {'FINISHED'}


def menu_func_import(self, context):
  self.layout.operator(GTAIVOF_OP_import.bl_idname, text="GTAIV openFormat (.oft, .odd, .odr)")


def menu_func_export(self, context):
  self.layout.operator(GTAIVOF_OP_export.bl_idname, text="GTAIV OpenFormat")


from .layout import Debug


classes = (
  Debug.DATA_OT_fast_import,
  Debug.DATA_OT_debug_material,
  Debug.VIEW3D_PT_debug_panel,
  GTAIVOF_OP_import,
  OFT_PT_import,
  GTAIVOF_OP_export,
  # TODO remove export mesh
  # GTAIVOF_OP_import_mesh,
  # GTAIVOF_OP_export_mesh
  #  GTAIV_PT_panel,
  #  ToggleOperator
)


def register():
  # import
  for CLASS in classes:
    print(f'register {CLASS.__name__}')
    bpy.utils.register_class(CLASS)

  bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
  bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
  # TODO remove export mesh
  # bpy.types.TOPBAR_MT_file_import.append(menu_func_import_mesh)
  # bpy.types.TOPBAR_MT_file_export.append(menu_func_export_mesh)
  print("register complete")


def unregister():
  for CLASS in classes:
    bpy.utils.unregister_class(CLASS)

  bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
  bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
  # TODO remove export mesh
  # bpy.types.TOPBAR_MT_file_import.remove(menu_func_import_mesh)
  # bpy.types.TOPBAR_MT_file_export.remove(menu_func_export_mesh)
  # print("end")

  # bpy.utils.unregister_class(GTAIV_PT_panel)



