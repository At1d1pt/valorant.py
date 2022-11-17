import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="valorant.py",
    version="1.0",
    author="At1d1pt",
    description="A python wrapper for https://valorant-api.com/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/At1d1pt/valorant.py",
    project_urls={
        "Bug Tracker": "https://github.com/MaybeSleight/At1d1pt/valorant.py",
    },
    package_dir={"": "valorant"},
    packages=setuptools.find_packages(where="valorant"),
    python_requires=">=3.6",
    install_requires=['requests']
)