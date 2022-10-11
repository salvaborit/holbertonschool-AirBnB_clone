#!/usr/bin/python3
from models.engine.file_storage import FileStorage

try:
    print(type(FileStorage._FileStorage__objects))
except:
    fs = FileStorage()
    print(type(fs._FileStorage__objects))
