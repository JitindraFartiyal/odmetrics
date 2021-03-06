
from setuptools import setup 
  
# reading long description from file 
with open('DESCRIPTION.txt') as file: 
    long_description = file.read() 
  
  
# specify requirements of your package here 
REQUIREMENTS = ['requests'] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 1 - Beta', 
    'Intended Audience :: Developers', 
    'Topic :: Internet', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python', 
    'Programming Language :: Python :: 2', 
    'Programming Language :: Python :: 2.6', 
    'Programming Language :: Python :: 2.7', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.3', 
    'Programming Language :: Python :: 3.4', 
    'Programming Language :: Python :: 3.5', 
    ] 
  
# calling the setup function  
setup(name='odmetrics', 
      version='1.0.0', 
      description='Metrics for Object Detection', 
      long_description=long_description, 
      url='https://github.com/JitindraFartiyal/odmetrics', 
      author='Jitindra Fartiyal', 
      author_email='jayfartiyal@hotmail.com', 
      license='MIT', 
      packages=['metrics'], 
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='Metrics for Object Detection'
      )