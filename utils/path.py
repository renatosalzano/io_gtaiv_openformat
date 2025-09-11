import os
from pathlib import Path

def dirname(path: str):
  return os.path.dirname(path)


def basename(path: str):
  '''return with ext'''
  return os.path.basename(path)


def filename(path: str):
  '''return without ext'''
  name, _ = os.path.splitext(path)
  return name


def ext(path: str):
  _, extension = os.path.splitext(path)
  return extension


def normalize(path: str):
  return os.path.normpath(path)


def join(*path):
  return os.path.join(*path)


def dirname(path: str):
  return os.path.dirname(path)


def is_dir(path: str):
  return os.path.isdir(path)

def exist(path: str):
  return os.path.exists(path)

def find_file(filename: str, to: list[str], extensions: list[str]):

  path = ''
  found = False

  for dir in to:

    if found:
      break

    for ext in extensions:
      test_path = f'{dir}/{filename}{ext}'
      
      if exist(test_path):
        path = test_path
        filename = f'{filename}{ext}'
        found = True
        break

  if not found:
    print(filename, 'not found')

  return (path, filename)