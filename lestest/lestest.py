from lestest.tox_creator import ToxCreator
from lestest.pytest_ini_creator import PytestIniCreator
from lestest.requirements_creator import RequirementsCreator


class Lestest:
    def __init__(
        self,
        tox: ToxCreator,
        pytestini: PytestIniCreator,
        requirements: RequirementsCreator,
    ) -> None:
        self.tox = tox
        self.pytestini = pytestini
        self.requirements = requirements

    def boilerplate(self):
        """
        Create a `lestest_templates` with all jinja templates used by lestest
        Going forward this templates instead of the default ones will be used to generate tests.

        """
        pass

    def generate(self):
        """Generate unittests from the discovered packages in the current directory"""

        self.tox.generate()
        self.pytestini.generate()
        self.requirements.generate()
