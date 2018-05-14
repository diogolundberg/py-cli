from setuptools import setup

setup(
    name='dataviva-scripts',
    version='1.0',
    py_modules=['metadata'],
    install_requires=['click', 'boto3', 'redis', 'pandas'],
    entry_points='''
        [console_scripts]
        metadata=metadata:load
    ''',
)
