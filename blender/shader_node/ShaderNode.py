

class ShaderNode:

  def __init__(this):
    this.name: str = ''
    this.type: str = ''

    this.inputs: list[tuple[str, ShaderNode]] = []
    this.settings = {}
    this.material = None
    this.node = None

  
  def init_node(this):

    if not this.name:
      # get from blender node
      this.name = getattr(this.node, 'name')
    else:
      # set to blender node
      setattr(this.node, 'name', this.name)

    for key, value in this.settings:
      setattr(this.node, key, value)
    
    pass