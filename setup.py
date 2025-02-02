from setuptools import setup, find_packages

setup(
    name='topsis-sarthaksachdeva-102203493',
    version='1.0.0',
    description='A Python package to apply TOPSIS for multi-criteria decision making.',
    author='Sarthak Sachdeva',
    author_email='sarthak@example.com',
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    entry_points={
        'console_scripts': [
            'topsis = topsis.topsis:topsis'
        ]
    },
)
