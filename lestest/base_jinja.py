import os
from typing import Tuple
from types import ModuleType
from jinja2 import Template
import importlib.resources as pkg_resources


class BaseJinja:
    @staticmethod
    def get_filepath_and_contents(
        filename: str,
        filepath: str,
        template_resource: ModuleType,
        template_filename: str = None,
        **template_vars
    ) -> Tuple[str]:

        """

        This methods uses the jinja template to generate a new file.

        :filename - the filename of the output
        :filepath - the path where the file should be saved
        :template_resource - the resource module which contains the .jinja template
        :template_filename - the jinja template filename
        (if not provided will look for filename.jinja in the template_resource package)
        :template_vars - the variables that should be passed to the jinja template

        """

        raw_contents = pkg_resources.read_text(
            template_resource, template_filename or filename + ".jinja"
        )
        filecontents = Template(raw_contents).render(**template_vars)

        return os.path.join(filepath, filename), filecontents

    @staticmethod
    def save_file(filepath: str, filecontents: str):
        """Save file to disk"""

        if os.path.exists(filepath):
            return  # don't overwrite

        if os.path.basename(filepath).startswith("_"):
            if os.path.exists(
                os.path.join(os.path.dirname(filepath), os.path.basename(filepath)[1:])
            ):
                return  # don't overwrite

        # if not os.path.isdir(filepath):
        #     os.makedirs(filepath)

        with open(filepath, "w") as f:
            f.write(filecontents)

        return filepath
