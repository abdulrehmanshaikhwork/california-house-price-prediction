"""
WSGI entry point for PythonAnywhere
"""
import sys
import os

# Add the project directory to the path
project_directory = os.path.dirname(os.path.abspath(__file__))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

# Import the Flask app
from app import app

# Application object for WSGI server
application = app

if __name__ == "__main__":
    application.run()
