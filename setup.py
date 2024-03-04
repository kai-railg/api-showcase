from setuptools import setup, find_packages

setup(
    name='openapi-request-showcase',
    version='0.1.0',
    description='chainboot-request-showcase is a centralized API directory and interactive platform designed to catalog and demonstrate all HTTP requests across various modules within a project, facilitating easy access and real-time API invocation for developers and stakeholders.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    author='Kai W',
    author_email='kai.wang@westwell-lab.com',
    license='MIT',
    packages=find_packages(
        # include=['api', 'schemas', "README.md"]
    ),
    install_requires=[
        "chain-http",
        "requests",
        "datamodel-code-generator",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11.0',
)
