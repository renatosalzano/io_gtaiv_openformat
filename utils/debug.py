import os
import json
import pickle

from .parser import ParserMethods

def debug_object(object: ParserMethods, path = '.debug/'):

  class_name = object.__class__.__name__
  class_dict = object.__dict__

  os.makedirs(path, exist_ok=True)

  debug_path = os.path.join(path, f'{class_name}.json')

  with open(debug_path, 'w') as file:
    json_string = json.dumps(object.to_JSON(), indent=2)
    file.write(json_string)

    print(f'saved {class_name}')

  pass