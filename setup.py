from setuptools import setup

setup(name='prometheus_metrics_analyzer',
      version='0.1',
      description='A simple library for supporting simple analytic services upon metrics hosted at Prometheus monitoring system and time series database.',
      url='https://github.com/efotopoulou/prometheus_metrics_analyzer',
      author='Eleni Fotopoulou',
      author_email='fwtopoulou@gmail.com',
      license='MIT',
      packages=['prometheus_metrics_analyzer'],
      install_requires=[
      'fuzzywuzzy',
      'pandas',
      'requests',
      'seaborn',
      'sklearn'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)

#setup(
#    ...
#    dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'],
#    ...
#)