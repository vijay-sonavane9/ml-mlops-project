from setuptools import find_packages, setup
from typing import List  # For following function to return list 


def get_requirements(file_path:str)-> List[str]:
    
    '''
    
    This function will return the list of requirements
    
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] # replace the new line character in requirement.txt
    
    return requirements  # -> List[str]:


setup(
    name = "mlproject",
    author="Vijay Sonavane",
    author_email="vijaysonawane00001@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirement.txt")#['numpy', 'pandas']
    
)