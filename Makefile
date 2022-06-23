
run-tests:
	coverage run --source=lestest -m unittest tests/test_* 
	coverage html 
	coverage report -m 
	rm coverage.svg
	coverage-badge -o coverage.svg