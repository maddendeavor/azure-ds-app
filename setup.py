from setuptools import setup

setup(
    name='azure_ds_app',
    version='0.0',
    description='Basic project to deploy a Machine Learning Model on Azure',
    long_description=open('README.md').read(),
    author='Christine Madden',
    license=open('LICENSE').read(),
    author_email='',
    packages=['project_name'],
    install_requires=[
    ],
    extras_require={
            "dev": [
                "black",  # lint & formatting helper
                "flake8",  # lint & formatting helper
                "isort",  # lint & formatting helper
                "sphinx",  # documentation
                "sphinx-autoapi",  # documentation
                "sphinx-mdinclude",  # documentation
                "sphinx-rtd-theme",  # read-the-docs theme
                "docstr-coverage",  # doc string coverage
                "wily",
                "coverage",
                "coverage-badge",
                "docstr-coverage",
                "pybadges",
                "pylint",
                "pytest",
        ],
    },
    entry_points={
        'console_scripts':
        [
            'project_name = project_name.__main__:main',
        ]
    }
)
