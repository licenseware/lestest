from types import ModuleType
from lestest.base_jinja import BaseJinja
from lestest.discover_package import DiscoverPackage
from lestest.test_metadata import TestMetadata
from lestest import templates


class UnittestCreator:
    def __init__(
        self,
        package_name: str = None,
        base: BaseJinja = None,
        inspector: DiscoverPackage = None,
        template_handler: TestMetadata = None,
        filepath: str = "./tests",
        template_filename: str = "test_template.py.jinja",
        template_resource: ModuleType = templates,
        **template_vars,
    ) -> None:
        self.base = base or BaseJinja
        self.inspector = inspector or DiscoverPackage
        self.template_handler = template_handler or TestMetadata
        self.filepath = filepath
        self.package_name = package_name
        self.template_filename = template_filename
        self.template_resource = template_resource
        self.template_vars = template_vars

    def generate(self):

        pkg_members = self.inspector.get_package_members(self.package_name)

        paths = []
        for pm in pkg_members:

            tv = self.template_handler.get_test_template_vars(pm)

            path, content = self.base.get_filepath_and_contents(
                filename=tv.filename,
                filepath=self.filepath,
                template_resource=self.template_resource,
                template_filename=self.template_filename,
                import_object_statement=tv.import_object_statement,
                object_name_lower=tv.object_name_lower,
                file_test_name=tv.file_test_name,
                object_call_statement=tv.object_call_statement,
                class_methods=tv.class_methods,
            )

            self.base.save_file(path, content)
            paths.append(path)

            print(f"Unittest file `{path}` ready")

        return paths
