import sys
import os

project_path = '/home/путь_к_директории_с_app.py'
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from app import app as application
