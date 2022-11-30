import os
import setuptools

setuptools.setup(
    name="LeagueHelper",
    version="0.0.0",
    author="Tobias Gerlach",
    author_email="me@tobias-gerlach.de",
    description=(
        "Helper tool for League of Legends. DO NOT USE INGAME. Just for demonstartion purposes."
    ),
    license="I dont know or care, do what you like with the code",
    keywords="league of legends helper tool",
    url="",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
)
