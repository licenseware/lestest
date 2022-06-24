from types import ModuleType
from lestest.base_jinja import BaseJinja
from lestest import templates


class UnittestCreator:
    def __init__(
        self,
        base: BaseJinja = None,
        filepath: str = "./tests",
        template_filename: str = "test_template.py.jinja",
        template_resource: ModuleType = templates,
        **template_vars
    ) -> None:
        self.base = base or BaseJinja
        self.filepath = filepath
        self.template_filename = template_filename
        self.template_resource = template_resource
        self.template_vars = template_vars

    def generate(self):

        path, content = self.base.get_filepath_and_contents(
            filename=self.filename,
            filepath=self.filepath or "",
            template_filename=self.template_filename,
            template_resource=self.template_resource,
            **self.template_vars
        )

        self.base.save_file(path, content)

        return path