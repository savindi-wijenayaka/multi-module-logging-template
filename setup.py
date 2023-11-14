from setuptools import setup, find_packages

setup(
    name="your-application-name",
    version="0.1.0",
    url="https://blah",
    author="Savindi Wijenayaka",
    author_email="author@gmail.com",
    description="blah blah blah",
    packages=find_packages(),
    py_modules=["application"],
    install_requires=[
        "matplotlib==3.8.0",  # example of required packages
    ],
    entry_points="""
            [console_scripts]
            application=application.mainfile:main
    """,
)
