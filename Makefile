

run-tests:
	coverage run --source=lestest -m unittest tests/test_* 
    coverage html 
    coverage report -m 
    coverage-badge -o coverage.svg