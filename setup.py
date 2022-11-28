from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name = 'LIME (Long read Isoform Mapping to Events',
    version = '0.1',
    author = 'Sheynkman Lab',
    author_email = 'sheynkman.lab@gmail.com',
    url = 'https://github.com/sheynkman-lab/splice-event-to-isoform-pipeline',
    license='MIT',
    zip_safe = False,
    include_package_data = True,
    install_requires=[
        'Click',
        'gtfparse',
        'pandas',
    ],
    packages =
        ['LIME'],
    python_requires = '>=3',
    entry_points = {
        'console_scripts':[
            'lime=LIME.main:cli',
        ],
    },
)