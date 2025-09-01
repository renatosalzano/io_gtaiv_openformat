def vector_to_string(vector, invert_xy = True):
  x,y,z = vector
  # invert XY
  if invert_xy:
    x *= -1
    y *= -1
  return f'{x:.8f} {y:.8f} {z:.8f}'

