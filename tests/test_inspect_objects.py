import unittest
from lestest import DiscoverPackage

# python3 -m unittest tests/test_inspect_objects.py


class TestInspectObjects(unittest.TestCase):
    def test_inspect_object(self):

        dp = DiscoverPackage()
        module_members = dp.get_module_members("./package/nested_module.py")
        assert len(module_members) == 3

        for mm in module_members:

            print(mm.object)
            print(dir(mm.object))

            break
