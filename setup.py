# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

long_description = ''

install_requires = []
with open('requirements.txt') as requirements_file:
    for line in requirements_file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        pinned_version = line.split()[0]
        install_requires.append(pinned_version)

setup(
    name='workflow-interop',
    description='Interoperable execution of workflows using GA4GH APIs',
    packages=['wfinterop'],
    package_data={
        'wfinterop': [
            'logging_config.ini'
            'workflow_execution_service.swagger.yaml',
            'ga4gh-tool-discovery.yaml'
        ]
    },
    url='https://github.com/Sage-Bionetworks/workflow-interop',
    download_url='https://github.com/Sage-Bionetworks/workflow-interop',
    long_description=long_description,
    install_requires=install_requires,
    entry_points={
        'console_scripts': 'ga4gh-testbed = wfinterop.__main__:main'
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'mock'],
    license='Apache 2.0',
    zip_safe=False,
    author='Sage Bionetworks CompOnc Team',
    author_email='james.a.eddy@gmail.com',
    version='0.2.0'
)
