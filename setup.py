#! /usr/bin/python
from setuptools import setup

# to install type:
# python setup.py install --root=/
def readme():
    with open('README.rst') as f:
        return f.read()
        
setup (name='tagmanager', version='0.6.4',
      author='Taha Zerrouki',
      author_email='taha_zerrouki@hotmail.com',
      url='http://pypi.python.com/projects/mysam-tagmanager/',
      license='GPL',
      description="Mysam: Arabic tags manager, ميسم: إدارة الوسوم  العربية",
      long_description = readme(),
      package_dir={'mysam': 'mysam',},
      packages=['mysam'],
      package_data = {
        'pyarabic': ['doc/*.*','doc/html/*'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Natural Language :: Arabic',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Linguistic',
          ],
    );

