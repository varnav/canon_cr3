#!/usr/bin/env python
'''
This file is part of cannon_cr3.

cannon_cr3 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

cannon_cr3 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with cannon_cr3. If not, see <http://www.gnu.org/licenses/>.

'''
from setuptools import setup

description = '''Package for extracting images and metadata out of Canon CR3 RAW image files'''
long_description = '''## IMPORTANT

[Original repo](https://github.com/lclevy/canon_cr3) was cloned and several patches that were breaking the build of Python lib were applied. It's now [available at PyPi](https://pypi.org/project/canon-cr3/). This means you can do this:

```sh
pip install canon-cr3
```

and then

```python
from canon_cr3 import Image as Image3
from PIL import Image

im = Image3('/tmp/myphoto.cr3')
im = Image.open(io.BytesIO(im.jpeg_image))
```

Please [mail me](varnavruz@gmail.com) if you want to be the maintainer of this.'''

setup(
    name='canon_cr3',
    version='2019.3.2',
    maintainer="Evgeny Varnavskiy",
    maintainer_email="varnavruz@gmail.com",
    packages=['canon_cr3'],
    keywords='Canon cr3',
    url='https://github.com/varnav/canon_cr3',
    license='GPLv3',
    description='Package for extracting images and metadata out of Canon CR3 RAW image files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Multimedia :: Graphics",
        "Programming Language :: Python :: 3",
    ],
)
