from setuptools import setup

setup(
    name="list_func",
    version="0.0.1",
    entry_points={
        "console_scripts": [
            "list_func=list_func.main:main",
        ]
    },
)