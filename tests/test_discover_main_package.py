import unittest
import os
from lestest import DiscoverPackage

# python3 -m unittest tests/test_discover_main_package.py


class TestDiscoverPackage(unittest.TestCase):
    def test_get_package_name(self):

        dp = DiscoverPackage()
        pkg_name = dp.get_package_name()

        assert pkg_name == "lestest"

    def test_get_module_paths(self):

        dp = DiscoverPackage()
        module_paths = dp.get_module_paths("lestest")

        for mp in module_paths:
            assert os.path.exists(mp)

        # print(module_paths)

    def test_get_module_imports(self):

        # module_paths = [
        #     "./lestest/pytest_ini_creator.py",
        #     "./lestest/discover_package.py",
        #     "./lestest/tox_creator.py",
        #     "./lestest/base_jinja.py",
        #     "./lestest/cli.py",
        #     "./lestest/lestest.py",
        #     "./lestest/requirements_creator.py",
        # ]

        dp = DiscoverPackage()
        module_members = dp.get_module_members("./lestest/tox_creator.py")

        assert "ToxCreator" == module_members.classes[0].object_name
        assert len(module_members.classes) == 1

        # print(module_members)

        package_name = dp.get_package_name()
        module_imports = dp.get_module_imports(package_name, module_members)

        # print(module_imports)

        assert "from lestest.tox_creator import ToxCreator" in module_imports
