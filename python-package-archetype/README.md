# python-package-archetype

Python boiler plate project for creating PyPI packages
https://www.youtube.com/watch?v=nelRslDOK_Y 
https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/ 

### Useful commands

* python setup.py check
* python setup.py sdist

#### Create a wheel distribution

* pip install wheel
* python setup.py bdist_wheel

#### Test the source code locally

* pip install .
* pip install --upgrade .

# CLI to release the package

Under python-package-archetype, run: 
`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

## Installation

## License

MIT
