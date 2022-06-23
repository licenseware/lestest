import os
import unittest
from lestest import Lestest, ToxCreator, PytestIniCreator, RequirementsCreator

# python3 -m unittest tests/test_lestest_generate.py


class TestGenerateLestest(unittest.TestCase):
    def tearDown(self) -> None:
        os.remove("tox.ini")
        os.remove("pytest.ini")
        os.remove("requirements-dev.txt")

    def test_lestest_generate(self):

        lestest = Lestest(
            tox=ToxCreator(),
            pytestini=PytestIniCreator(),
            requirements=RequirementsCreator(),
        )

        lestest.generate()

        assert os.path.isfile("tox.ini")
        assert os.path.isfile("pytest.ini")
        assert os.path.isfile("requirements-dev.txt")
