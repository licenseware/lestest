import os
import unittest
from lestest import (
    Lestest,
    ToxCreator,
    PytestIniCreator,
    RequirementsCreator,
    UnittestCreator,
)

# python3 -m unittest tests/test_lestest_generate.py


class TestGenerateLestest(unittest.TestCase):
    def test_lestest_generate(self):

        lestest = Lestest(
            tox=ToxCreator(),
            pytestini=PytestIniCreator(),
            requirements=RequirementsCreator(),
            unittest=UnittestCreator(package_name="package"),
        )

        paths = lestest.generate()

        assert os.path.isfile(paths.tox)
        assert os.path.isfile(paths.pytestini)
        assert os.path.isfile(paths.requirements)

        os.remove(paths.tox)
        os.remove(paths.pytestini)
        os.remove(paths.requirements)

        for path in paths.unittests:
            assert os.path.isfile(path)
            os.remove(path)
