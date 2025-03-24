from setuptools import find_packages, setup
from typing import List


HYPHEN_SEPARATOR = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    Reads a requirements.txt file and returns a list of all the package names.
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:

        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_SEPARATOR in requirements:
            requirements.remove(HYPHEN_SEPARATOR)
    return requirements



setup(
    name='examPerformancePredictor',
    version='0.0.1',
    author='Mukhar Satsangi',
    author_email='mukharsatsangi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)