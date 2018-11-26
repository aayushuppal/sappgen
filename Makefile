test:
	python3.7 -m pytest -s tests

run:
	python3.7 -c 'from sappgen import process; process(project="proj1", app="app1")'

clean:
	find . -name *.pyc -exec rm -f {} \;
	rm -rf proj1
	rm -rf 	build \
			dist \
			.cache \
			*.egg-info \
			.pytest_cache
