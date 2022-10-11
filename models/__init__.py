#!/usr/bin/python3
"""Engine init"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
