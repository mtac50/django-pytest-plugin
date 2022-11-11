"""A pytest plugin which helps testing Django applications

This plugin handles creating and destroying the test environment and
test database and provides some useful text fixtures.
"""

import os
import sys

from django.core.management import call_command
import pytest

from exceptions import DjangoTestSetupError

SETTINGS_MODULE_ENV = 'DJANGO_SETTINGS_MODULE'
CONFIGURATION_ENV = 'DJANGO_CONFIGURATION'

# ############### pytest hooks ################


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    corrected_test_name = item.nodeid.replace(".py", "").replace("::", ".").replace("/", ".")

    def _run_override():
        call_command("test", corrected_test_name, interactive=False)
        return

    item.runtest = _run_override


def pytest_addoption(parser):

    parser.addini(SETTINGS_MODULE_ENV,
                  'Django settings module to use by pytest-django.')


def _add_django_project_to_path():

    base_directory = os.getcwd()
    manage_py_try = os.path.join(base_directory, 'manage.py')

    if not os.path.isfile(manage_py_try):
        raise DjangoTestSetupError("No django project found in base directory.")

    sys.path.insert(0, str(base_directory))


def _setup_django():
    if 'django' not in sys.modules:
        return

    import django.conf

    if not django.conf.settings.configured:
        return

    django.setup()


def pytest_load_initial_conftests(early_config, parser, args):

    _add_django_project_to_path()

    django_settings = _get_django_settings_module(early_config)

    if django_settings:
        os.environ[SETTINGS_MODULE_ENV] = django_settings

        from django.conf import settings as dj_settings
        dj_settings.DATABASES

    _setup_django()

def _get_django_settings_module(early_config):
    settings = early_config.getini(SETTINGS_MODULE_ENV)

    if not settings:
        raise DjangoTestSetupError("No django settings module define in the pytest.ini file.")
    
    return settings
