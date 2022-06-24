import unittest
import inspect

from pytest import param

from lestest import DiscoverPackage, BaseJinja, templates, TestMetadata

# python3 -m unittest tests/test_inspect_objects.py


class TestInspectObjects(unittest.TestCase):
    def test_inspect_object(self):

        pkg_members = DiscoverPackage.get_package_members("package")

        for pm in pkg_members:

            # if pm.object_name != "func1":
            #     continue

            if pm.object_name != "Class1":
                continue

            tv = TestMetadata.get_test_template_vars(pm)

            filepath, filecontents = BaseJinja.get_filepath_and_contents(
                filename=tv.filename,
                filepath="./demo",
                template_resource=templates,
                template_filename="test_template.py.jinja",
                import_object_statement=tv.import_object_statement,
                object_name_lower=tv.object_name_lower,
                file_test_name=tv.file_test_name,
                object_call_statement=tv.object_call_statement,
                class_methods=tv.class_methods,
            )

            print(filepath)
            print(filecontents)

            break
