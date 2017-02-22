try:
    from setuptools import setup

except ImportError:
    from distutile.core import setup

config = {
    'description': 'My very first project',
    'author': 'Yusuke Takeuchi',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)