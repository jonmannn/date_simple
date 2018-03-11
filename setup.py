from setuptools import setup

setup ( name='date_simple',
       version='0.1',
       description='This module is a wrapper for datetime.  ',
       url='git@github.com:jonmannn/date_simple.git',                # usually a github URL
       author='Jon Mann',
       author_email='jonmannn@gmail.com',
       license='MIT',
       packages=['date_simple'],
       install_requires=['date_time'],
       zip_safe=False,
       test_suite='pytest',
        setup_requires = ['pytest-runner'],
        tests_require = ['pytest']
        )