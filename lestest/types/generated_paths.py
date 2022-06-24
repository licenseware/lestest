from dataclasses import dataclass


@dataclass
class GeneratedPaths:
    tox: str
    pytestini: str
    requirements: str
    unittests: tuple
