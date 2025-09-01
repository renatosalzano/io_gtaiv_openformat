import os
from pathlib import Path

def dirname(path: str):
  return os.path.dirname(path)


def basename(path: str):
  return os.path.basename(path)


def filename(path: str):
  name, _ = os.path.splitext(path)
  return name


def ext(path: str):
  _, extension = os.path.splitext(path)
  return extension


def normalize(path: str):
  return os.path.normpath(path)


def join(*path):
  return os.path.join(*path)