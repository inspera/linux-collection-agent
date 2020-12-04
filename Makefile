PYTHON=python3

all: 
		

python-dependencies:
		curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | $(PYTHON) -
		~/.poetry/bin/poetry install

dump-dependencies: 
		sudo apt install inxi
