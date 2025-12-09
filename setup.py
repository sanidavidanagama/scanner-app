from setuptools import setup, find_packages

setup(
    name='scanner_app',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['pillow', 'comtypes'],
    entry_points={
        'console_scripts': [
            'scanner-app = scanner_app.main:main',
        ],
    },
)