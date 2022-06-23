import unittest
import os
from lestest import ToxCreator

# python3 -m unittest tests/test_tox_creator.py


class TestToxCreator(unittest.TestCase):
    def tearDown(self) -> None:
        os.remove("tox.ini")

    def test_tox_creator(self):

        tox = ToxCreator()
        tox.generate()

        assert os.path.isfile("tox.ini")
