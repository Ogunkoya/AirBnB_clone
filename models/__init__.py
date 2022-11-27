#!/usr/bin/python3
"""
Module: __init__.py
"""
from . import engine
from . import base_model




from models.engine.file_storage import FileStorage


storage = file_storage.FileStorage()

storage.reload()
