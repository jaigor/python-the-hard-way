try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Test Project: this is a test to know how make a project run',
    'author': 'Igor Quintela',
    'url': 'https://github.com/jaigor/python-the-hard-way',
    'download_url': 'https://github.com/jaigor/python-the-hard-way',
    'author_email': 'jaigor@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['testing'],
    'scripts': [],
    'name': 'testing'
}

setup(**config)