from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='zerooneai',
    version='0.1',
    description='Whith this package you can make an simple AI that can predict a zero or a one.',
    long_description=readme(),
    url='https://github.com/MathijsTak/Pacemaker-ai',
    author='MathijsTak',
    author_email='mathijs.tak@outlook.com',
    license='Open source',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'sklearn',
        'pickle'
    ],
    keywords='zeroone zero one ai zerooneai zeroai oneai',
    packages=['zerooneai'],
    package_dir={'zerooneai': 'src/zerooneai'}
)