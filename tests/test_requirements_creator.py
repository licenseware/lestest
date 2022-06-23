import os
import unittest

from lestest import RequirementsCreator

# python3 -m unittest tests/test_requirements_creator.py


class TestRequirementsCreator(unittest.TestCase):

    def tearDown(self) -> None:
        os.remove("requirements-dev.txt")

    def test_tox_creator(self):

        req = RequirementsCreator()
        req.generate()

        assert os.path.isfile("requirements-dev.txt")

