from setuptools import setup
from setuptools import find_packages

REQUIREMENTS = [
  "thumbor",
  "gcloud",
  "protorpc",
]

setup(
  name="thumbor_cloud_storage",
  version="2.0.1",
  author="Andrei Tij",
  author_email="me@pedro.bz",
  description="Thumbor's Google Cloud Storage loader and result storage",
  url="https://github.com/atij/thumbor-cloud-storage",
  license="MIT",
  include_package_data=True,
  packages=find_packages(),
  install_requires=REQUIREMENTS,
  zip_safe=False
)
