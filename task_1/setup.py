from setuptools import setup, find_packages

setup(
    name="geometrylib",
    version="0.1.0",
    author="David Akopyan",
    author_email="dg.akopyan@gmail.com",
    description="A geometry library to compute areas of shapes",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Davillas/Mindbox_Tasks/tree/dev/task_1",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)