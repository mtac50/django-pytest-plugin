# Welcome to django-pytest-plugin!

This is a basic pytest plugin that allows the user to run django tests through the visual studio code (VSCode) test explorer using pytest.

The plugin is essentially a proxy for the django `manage.py test` command and was designed to allow use of the VSCode python test explorer with legacy python (2.7) and django.

## Notes

Due to the legacy nature of the python version older version of the VSCode test explorer need to be used. The current version of the plugin works with VSCode Python extension `ms-python.python@2021.9.1246542782`.

## Development

This repository is setup for Dockerised development in VSCode using the Dev Containers extension. There is a dockerfile and devcontainer.json file defined within the `./.devcontainer` folder. If you are using a different IDE then simply build the docker containers manually and attach to it.

If you don't wish to use docker then setup a virtual environment.

```
virtualenv -p python2.7 env
source env/bin/activate
```

Update pip to the latest version:

```
pip install -U pip
```

Install python dependencies:

```
pip install -r requirements.txt
```

## Building Package

To build the package run 

```
python setup.py sdist bdist_wheel
```

This will produce a wheel file `dist/django_pytest_plugin-<version>-py2-none-any.whl`. 

## Package Installation

The wheel file produced in the build phase can be installed via pip in the required projects

```
pip install <path-to-wheel>
```
