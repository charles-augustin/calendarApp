from setuptools import setup, find_packages

setup(
    name='calendar_app_setup',
    version='1.0.0',
    install_requires=[
        'selenium',
        'pytest',
        'webdriver-manager',
        'pytest-html',
        'pytest-xdist',
        'openpyxl',
        'allure-pytest'
    ],
    packages=find_packages()
)
