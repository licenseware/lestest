import unittest
import os
from lestest import UnittestCreator

# python3 -m unittest tests/test_unittest_creator.py


class TestUnittestCreator(unittest.TestCase):
    def test_unittest_creator(self):

        ut = UnittestCreator(package_name="package")

        paths = ut.generate()

        for path in paths:
            assert os.path.exists(path)
            os.remove(path)
