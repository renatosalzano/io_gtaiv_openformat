import os
import json
import pickle

def debug_object(object, path = '.debug/'):

  class_name = object.__class__.__name__
  class_dict = object.__dict__

  os.makedirs(path, exist_ok=True)

  debug_path = os.path.join(path, f'{class_name}.json')

  with open(debug_path, 'w') as file:
    json_string = json.dumps(object.to_JSON(), indent=2)
    file.write(json_string)

    print(f'saved {class_name}')

  pass


import os
from datetime import datetime

class DebugLogger:

  def __init__(self, log_file=".debug.log"):
    self.log_file = log_file
    self._initialize_log_file()

  def _initialize_log_file(self):
    # Pulisce il file di log all'avvio se esiste, o lo crea
    with open(self.log_file, "w") as f:
      f.write(f"--- Debug Log Started: {datetime.now()} ---\n")

  def log_message(self, message):
    """Scrive un messaggio nel file di log con un timestamp."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(self.log_file, "a") as f:
      f.write(f"[{timestamp}] {message}\n")

# --- Creazione dell'istanza globale ---
# Questo assicura che ci sia una sola istanza di DebugLogger
# accessibile da qualsiasi parte del tuo progetto.
debug_instance = DebugLogger()

def log(message):
    """Funzione helper per accedere all'istanza globale e loggare un messaggio."""
    debug_instance.log_message(message)