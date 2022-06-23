import os
import unittest
from typer.testing import CliRunner
from lestest.cli import app


# python3 -m unittest tests/test_cli_lestest_generate.py


class TestGenerateBaseFiles(unittest.TestCase):
    def setUp(self) -> None:
        self.cli = CliRunner()

    def tearDown(self) -> None:
        os.remove("tox.ini")
        os.remove("pytest.ini")
        os.remove("requirements-dev.txt")

    def test_cli_lestest_generate(self):

        result = self.cli.invoke(app, ["generate"])
        print(result.stdout)
        assert result.exit_code == 0
        assert "Generated unittest boilerplate files" in result.stdout

        assert os.path.isfile("tox.ini")
        assert os.path.isfile("pytest.ini")
        assert os.path.isfile("requirements-dev.txt")
