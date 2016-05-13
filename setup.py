from setuptools import setup, find_packages

VERSION = (0, 0, 1)
__version__ = '.'.join(map(str, VERSION))

setup(
    name='safe_eval',
    version=__version__,
    description='safe_eval provides more restricted alternatives to evaluate simple and/or untrusted code than python`s eval.',
    long_description=open('README.md').read(),
    author='http://www.openerp.com',
    url='https://github.com/Atishay4294/safe_eval',
    license='GNU Affero General Public License',
    py_modules=["safe_eval"],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: GNU Affero General Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
