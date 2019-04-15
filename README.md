# Advance Whatsapp web spammer

Using Python selenium to spam your friends in whatsapp.

There are 3 modes for spamming:
* random image spamming from [unsplash](https://source.unsplash.com/)
* text spamming
* stickers spamming

## Set Up

* Install [Python](https://www.python.org/)

* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium and the other packages 📦.

## Packages installation

After installing pip and python run theses commands in your bash to install the needed packages:

First get into the folder:
```bash
cd ../whatsapp_web_spammer
```

Then Install the packages with this command:

```bash
pip install --user -r requirements.txt
```

## Imports

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from distutils.util import strtobool
from selenium.webdriver.common.action_chains import ActionChains

import time
import platform
import os, sys
```

## Get Started

Get into the folder in your bash with the command:
```bash
cd ../whatsapp_web_spammer
```
And then Run the python running command:
```
python spammer.py
```

That’s it! Good luck.

## Author

Created by Ido Sharon 🐶 

Written in Python 🐍

## License
```
MIT License

Copyright (c) 2019 Ido Sharon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
