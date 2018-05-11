from setuptools import setup

setup(
    name='es-export-csv',
    author='Casey Weed',
    author_email='cweed@caseyweed.com',
    version='0.1',
    description='Export match all query to CSV',
    url='https://github.com/battleroid/es-export-csv',
    py_modules=['es_export_csv'],
    install_requires=[
        'elasticsearch',
        'certifi'
    ],
    entry_points="""
        [console_scripts]
        es-export-csv=es_export_csv:main
    """
)
