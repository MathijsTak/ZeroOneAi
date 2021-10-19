from setuptools import find_packages, setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10/11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='zerooneai',
    version='0.0.1',
    description='Whith this package you can make an simple AI that can predict a zero or a one.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELONG.txt').read(),
    url='https://github.com/MathijsTak/Pacemaker-ai',
    author='MathijsTak',
    author_email='mathijs.tak@outlook.com',
    license='MIT',
    classifiers=classifiers,
    keywords='zeroone zero one ai zerooneai zeroai oneai',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'sklearn',
        'pickle'
    ]
)