from setuptools import setup, find_packages

setup(
    name="gpt-cli",
    version="0.1",
    packages=find_packages(),  # Ensure this captures your package correctly
    install_requires=[
        "python-dotenv",
        "openai",
        "typer[all]",
    ],
    entry_points={
        'console_scripts': [
            'gpt=gpt_cli.gpt:main',
        ],
    },
    author="Pulkit Sharma",
    author_email="pulkitsh1@outlook.com",
    description="A simple CLI tool to interact with ChatGPT",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/pulkitsh1/AI-Chat-App",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
