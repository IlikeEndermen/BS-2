import subprocess
import json
import os
from pathlib import Path

from jinja2 import Template

from app.core.feature_interface import BaseFeature

def register():
    instance = Feature()
    return {
        "instance": instance,
        "self_test": None,
        "shutdown": lambda: print("Shutting down Feature_2..."),
    }

class Feature(BaseFeature):
    def run(self, file_path) -> str:
        if not file_path or not os.path.isfile(file_path):
            return "<p>No file selected or invalid path.</p>"
        

        template_str = """
        <h2>Feature_2</h2>
        <p>Provided path: {{ file_path }}</p>
        """
        template = Template(template_str)
        return template.render(file_path=file_path)