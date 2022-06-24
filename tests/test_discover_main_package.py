import unittest
import os
from lestest import DiscoverPackage

# python3 -m unittest tests/test_discover_main_package.py

module_paths = [
    "./package/nested_module.py",
    "./package/n1/n1_module.py",
    "./package/n2/n2_module.py",
    "./package/n2/n3/n3_module.py",
]


class TestDiscoverPackage(unittest.TestCase):
    def test_get_package_name(self):

        pkg_name = DiscoverPackage.get_package_name("package")

        assert pkg_name == "package"

    def test_get_module_paths(self):

        module_paths = DiscoverPackage.get_module_paths("package")

        for mp in module_paths:
            assert os.path.exists(mp)

        # print(module_paths)

    def test_nested_discovery(self):

        module_members = DiscoverPackage.get_module_members("./package/n1/n1_module.py")

        assert len(module_members) == 3

        for mm in module_members:
            assert mm.object_name in ["func2", "cofunc2", "Class2"]
            assert mm.import_statement in [
                "from package.n1.n1_module import func2",
                "from package.n1.n1_module import cofunc2",
                "from package.n1.n1_module import Class2",
            ]

    def test_super_nested_discovery(self):

        module_members = DiscoverPackage.get_module_members(
            "./package/n2/n3/n3_module.py"
        )

        assert len(module_members) == 3

        for mm in module_members:
            assert mm.object_name in ["func4", "cofunc4", "Class4"]
            assert mm.import_statement in [
                "from package.n2.n3.n3_module import Class4",
                "from package.n2.n3.n3_module import cofunc4",
                "from package.n2.n3.n3_module import func4",
            ]

    def test_get_package_members(self):

        pkg_members = DiscoverPackage.get_package_members("package")

        for mm in pkg_members:

            assert mm.object_name in [
                "Class1",
                "Class2",
                "Class3",
                "Class4",
                "cofunc1",
                "cofunc2",
                "cofunc3",
                "cofunc4",
                "func1",
                "func2",
                "func3",
                "func4",
            ]

            assert mm.import_statement in [
                "from package.nested_module import Class1",
                "from package.nested_module import cofunc1",
                "from package.nested_module import func1",
                "from package.n1.n1_module import Class2",
                "from package.n1.n1_module import cofunc2",
                "from package.n1.n1_module import func2",
                "from package.n2.n2_module import Class3",
                "from package.n2.n2_module import cofunc3",
                "from package.n2.n2_module import func3",
                "from package.n2.n3.n3_module import Class4",
                "from package.n2.n3.n3_module import cofunc4",
                "from package.n2.n3.n3_module import func4",
            ]
