from setuptools import setup

setup(
    name="PyZFS",
    version="dev",  # set as dev for development commits
    author="He Ma, Marco Govoni",
    author_email="mahe@uchicago.edu, mgovoni@anl.gov",
    description="A python code to compute zero-field splitting tensors",
    packages=["pyzfs"],
    classifiers=[],
    install_requires=[
        'numpy', 'scipy', 'mpi4py', 'ase', 'lxml',
    ]
)

