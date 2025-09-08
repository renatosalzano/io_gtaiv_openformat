import bpy


class DATA_OT_debug_material(bpy.types.Operator):

  bl_idname = "data.coluichesbatteleporte"
  bl_label = "Mona"
  bl_description = "Sbatto la porta"

  def execute(this, context):

    print('sbatto la porta')

    return { 'FINISHED' }


class VIEW3D_PT_debug_panel(bpy.types.Panel):

  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"

  bl_category = "Debug" #sidebar label
  bl_label = "Debug Panel" #head label

  def draw(this, ctx):

    row = this.layout.row()
    row.operator('data.coluichesbatteleporte', text="Sbatti la Porta")
    
