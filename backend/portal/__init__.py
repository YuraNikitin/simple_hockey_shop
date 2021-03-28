import os


__version__ = os.environ.get('VERSION', 'undefined')
print(f'Version of project: {__version__}')
