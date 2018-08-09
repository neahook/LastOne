from setuptools import setup, find_packages


setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    package_data={
        'myproject': ['url.txt']
    },
    entry_points = {'scrapy': ['settings = A337311.settings']},
    zip_safe=False,
)

