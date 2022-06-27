
run-tests:
	coverage run --source=lestest -m unittest tests/test_* 
	coverage html 
	coverage report -m 
	rm coverage.svg
	coverage-badge -o coverage.svg


build:
	python3 setup.py bdist_wheel sdist
	rm -rf build


install:
	python3 setup.py bdist_wheel sdist
	rm -rf build
	pip3 install dist/lestest-0.0.1-py3-none-any.whl

uninstall:
	pip3 uninstall lestest