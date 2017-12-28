# This file is a part of HER
#
# Copyright (c) 2017 The HER Authors (see AUTHORS)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from distutils.core import setup
import sys

try:
    if sys.argv[1] == "egg_info":
        long_description = "A new file format"
    else:
        try:
            import pypandoc
            long_description = pypandoc.convert('README.md', 'rst')
        except(IOError, ImportError):
            long_description = open('README.md').read()

except(IndexError):
    try:
        import pypandoc
        long_description = pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        long_description = open('README.md').read()

setup(
    name='her',
    packages=['her'],
    package_dir={'': 'src'},
    version='1.1.2',
    description='A new file format',
    long_description=long_description,
    author='Gabriel Hearot',
    author_email='gabriel@hearot.it',
    url='https://github.com/hearot/HER',
    download_url='https://github.com/hearot/HER/archive/v1.1.2.tar.gz',
    keywords=['python', 'her'],
    classifiers=[]
)
