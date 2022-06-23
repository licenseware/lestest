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

        dp = DiscoverPackage()
        pkg_name = dp.get_package_name("package")

        assert pkg_name == "package"

    def test_get_module_paths(self):

        dp = DiscoverPackage()
        module_paths = dp.get_module_paths("package")

        for mp in module_paths:
            assert os.path.exists(mp)

        # print(module_paths)

    def test_nested_discovery(self):

        dp = DiscoverPackage()
        module_members = dp.get_module_members("./package/n1/n1_module.py")

        # print("module_members.functions: ", module_members.functions)
        # print("module_members.classes: ", module_members.classes)

        assert "func2" in [
            module_members.functions[0].object_name,
            module_members.functions[1].object_name,
        ]
        assert len(module_members.functions) == 2

        module_imports = dp.get_module_imports(module_members)

        # print(module_imports)

        assert "from package.n1.n1_module import Class2" in module_imports

    def test_super_nested_discovery(self):

        dp = DiscoverPackage()
        module_members = dp.get_module_members("./package/n2/n3/n3_module.py")

        # print("module_members.functions: ", module_members.functions)
        # print("module_members.classes: ", module_members.classes)

        assert "func4" in [
            module_members.functions[0].object_name,
            module_members.functions[1].object_name,
        ]
        assert len(module_members.functions) == 2

        module_imports = dp.get_module_imports(module_members)

        # print(module_imports)

        assert "from package.n2.n3.n3_module import Class4" in module_imports
