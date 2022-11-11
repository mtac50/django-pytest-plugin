import codecs
import os

from setuptools import setup

PACKAGE = 'django_pytest_plugin'

pkg_vars  = {}

with open(PACKAGE + '/_version.py') as fp:
    exec(fp.read(), pkg_vars)


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='django-pytest-plugin',
    version=pkg_vars['__version__'],
    description='A plugin for running django tests through Pytest',
    author='Michael Clancy',
    author_email='michael.clancy50@gmail.com',
    maintainer="Michael Clancy",
    maintainer_email="michael.clancy50@gmail.com",
    license='MIT',
    packages=['django_pytest_plugin'],
    long_description=read('README.md'),
    setup_requires=['setuptools', 'wheel'],
    install_requires=['pytest>=2.9'],
    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: MIT License',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Testing',
                 'Programming Language :: Python :: 2.7',
                 ],
    # the following makes a plugin available to pytest
    entry_points={'pytest11': ['django = django_pytest_plugin.plugin']})