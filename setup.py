from setuptools import setup, find_packages

with open("requirements.txt", "r") as fh:
   requirements = fh.readlines()

setup(name='pytorch2timeloop',
      version='0.2',
      url='https://github.com/jaylenwang7/pytorch2timeloop-converter',
      license='MIT',
      install_requires=[req for req in requirements if req[:2] != "# "],
      python_requires='>=3.6',
      include_package_data=True,
      packages=find_packages())
