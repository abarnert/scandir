"""Run "python setup.py install" to install scandir."""

from distutils.core import setup

import scandir

setup(
    name='scandir',
    version=scandir.__version__,
    author='Ben Hoyt',
    author_email='benhoyt@gmail.com',
    url='https://github.com/benhoyt/scandir',
    license='New BSD License',
    description='scandir, a better directory iterator that exposes all file info OS provides',
    long_description="scandir is a generator version of os.listdir() that returns an iterator over "
                     "files in a directory, and also exposes the extra information most OSes provide "
                     "while iterating files in a directory. Read more at the GitHub project page.",
    py_modules=['scandir'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Operating System',
    ]
)