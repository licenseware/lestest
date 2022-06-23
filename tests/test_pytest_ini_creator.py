import unittest
import os
from lestest import PytestIniCreator

# python3 -m unittest tests/test_pytest_ini_creator.py


class TestPytestIniCreator(unittest.TestCase):
    def tearDown(self) -> None:
        os.remove("pytest.ini")

    def test_tox_creator(self):

        pyini = PytestIniCreator()
        pyini.generate()

        assert os.path.isfile("pytest.ini")
