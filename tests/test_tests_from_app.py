import unittest
import os
import lestest


# python3 -m unittest tests/test_tests_from_app.py


class TestAppTestGeneration(unittest.TestCase):
    def test_app_test_generation(self):

        if not os.path.exists("app"):
            return

        lt = lestest.Lestest(
            tox=lestest.ToxCreator(),
            pytestini=lestest.PytestIniCreator(),
            requirements=lestest.RequirementsCreator(),
            unittest=lestest.UnittestCreator("app"),
        )

        paths = lt.generate()

        assert os.path.isfile(paths.tox)
        assert os.path.isfile(paths.pytestini)
        assert os.path.isfile(paths.requirements)

        os.remove(paths.tox)
        os.remove(paths.pytestini)
        os.remove(paths.requirements)

        for path in paths.unittests:
            assert os.path.isfile(path)
            os.remove(path)
