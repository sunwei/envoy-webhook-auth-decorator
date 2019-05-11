venv:
	virtualenv -p `which python3` venv && \
    source venv/bin/activate

develop: venv
	venv/bin/pip install -e . -r requirements.txt

clean:
	-rm -rf venv

test:
	tox

require:
	pip freeze > requirements.txt
