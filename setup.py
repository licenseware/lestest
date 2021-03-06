from setuptools import setup, find_packages

# https://packaging.python.org/guides/distributing-packages-using-setuptools/?highlight=setup.py#setup-py
# Distribute py wheels
# python3 setup.py bdist_wheel sdist
# twine check dist/*
# cd dist
# twine upload *


with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    REQUIREMENTS = f.readlines()


VERSION = "0.0.1"

setup(
    name="lestest",
    version=VERSION,
    description="Generate boilerplate unittests from given package.",
    url="https://licenseware.io/",
    author="Licenseware",
    author_email="contact@licenseware.io",
    license="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=REQUIREMENTS,
    packages=find_packages(where=".", exclude=["tests", "package", "app"]),
    include_package_data=True,
    package_data={"": ["*"]},
    entry_points={
        "console_scripts": [
            "lestest=lestest.cli:cli_entrypoint",
        ],
    },
)
