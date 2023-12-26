from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in usaepay_integration/__init__.py
from usaepay_integration import __version__ as version

setup(
	name="usaepay_integration",
	version=version,
	description="USAePay and ERPNext integration module",
	author="Natnael Tilaye",
	author_email="natnaeltilaye30@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
