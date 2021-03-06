from types import ModuleType
from lestest.base_jinja import BaseJinja
from lestest import templates


class PytestIniCreator:
    def __init__(
        self,
        base: BaseJinja = None,
        filename: str = "pytest.ini",
        filepath: str = None,
        template_filename: str = "pytest.ini.jinja",
        template_resource: ModuleType = templates,
        **template_vars
    ) -> None:
        self.base = base or BaseJinja
        self.filename = filename
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

        print("File `pytest_ini` ready")

        return path
