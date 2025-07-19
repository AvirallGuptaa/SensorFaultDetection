from setuptools import find_packages,setup
from typing import List

hypenE='-e.'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as fileobj:
        req=fileobj.readlines()
        req=[r.replace('\n',"") for r in req]
    if hypenE in requirements:
        requirements.remove(hypenE)
    return requirements
setup(
    name='Fault Detection',
    version='0.0.1',
    author='Aviral',
    author_email='aviralgupta1624@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()    
)