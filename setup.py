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

setup(
    name='her',
    packages=['her'],
    package_dir={'': 'src'},
    version='1.2',
    description='A new file format',
    long_description='HER, a new Text Format |Build Status|\n=====================================\n\nSearch informations about the Syntax and Types using the `Wiki\nsection <https://github.com/hearot/HER/wiki>`__.\n\nContent table\n-------------\n\n-  `What\'s HER? <#whats-her>`__\n-  `Why shall I use HER? <#why-shall-i-use-her>`__\n-  `Why HER? <#why-her>`__\n-  **Python Module**\n\n   -  `Installation <#installation>`__\n   -  `Import Module <#import-module>`__\n   -  `Encode a Dictionary <#encode-a-dictionary>`__\n   -  `Decode a String <#decode-a-string>`__\n   -  `Decode a File <#decode-a-file>`__\n   -  `Convert HER to JSON <#convert-her-to-json>`__\n   -  `Convert JSON to HER <#convert-json-to-her>`__\n\nWhat\'s HER?\n-----------\n\nHER is text format, like XML/Json. The difference is that HER is easier\nthan others. Just see:\n\n::\n\n    - Category -\n        >> Array[]\n        * Array[] = "Umh, that\'s pretty good!"\n\nWhy shall I use HER?\n--------------------\n\nAs I said before, HER is **simple** and **easy to use**. You can pass\ninformations, or better, store informations\\* and document them.\n\nFeel the difference:\n\n**XML:**\n\n.. code:: xml\n\n    <category>Christmas\n        <greetings>Merry christmas!</greetings>\n        <greetings>Spam, Python, Eggs</greetings>\n    </category>\n\n**HER:**\n\n::\n\n    - Christmas -\n        >> Greetings[]\n        * Greetings[] = "Merry christmas!"\n        * Greetings[] = "Spam, Python, Eggs"\n\nWhy HER?\n~~~~~~~~\n\n**Because, however, if it isn\'t right, it\'s right.**\n\nPython Module\n=============\n\nInstallation\n------------\n\nYou can easily install that module using PiP:\n\n.. code:: bash\n\n    pip install her\n\nOr, if you want to upgrade the module:\n\n.. code:: bash\n\n    pip install --upgrade her\n\nImport Module\n-------------\n\nYou must use ``import her`` to import all HER module.\n\n.. code:: python\n\n    import her\n    encoderObject = her.Encoder({\'Category\':{\'hello world\':True}})\n    ...\n\nEncode a Dictionary\n-------------------\n\nJust use the ``Encoder`` class. Call the ``__init__`` function assigning\nthe object to a variable, then the ``Encoded String`` will be available\ninto the ``self.HER`` variable of the object.\n\n.. code:: python\n\n    import her\n    encoderObject = her.Encoder({\'Category\':{\'hello world\':True}})\n    print(encoderObject.HER)\n\nOutput:\n\n::\n\n    - Category -\n        * hello world = True\n\nDecode a String\n---------------\n\nJust use the ``Decoder`` class. Call the ``__init__`` function assigning\nthe object to a variable, then the ``Decoded Dictionary`` will be\navailable into the ``self.HER`` variable of the object.\n\n.. code:: python\n\n    import her\n    decoderObject = her.Decoder("- Category -\\n    * hello world = True")\n    print(decoderObject.HER)\n\nOutput:\n\n::\n\n    {\'Category\':{\'hello world\':True}}\n\nDecode a File\n-------------\n\nJust use the ``Decoder`` class. Call the ``__init__`` function assigning\nthe object to a variable, then the ``Decoded Dictionary`` will be\navailable into the ``self.HER`` variable of the object.\n\nRemember:the first\nparameter must be a ``File`` object.\n\n.. code:: python\n\n    import her\n    decoderObject = her.Decoder(open("file_path", "r"))\n    print(decoderObject.HER)\n\nOutput:\n\n::\n\n    {\'Category\':{\'hello world\':True}}\n\nConvert JSON to HER\n-------------------\n\nJust use the ``Json2HER`` class. Call the ``__init__`` function\nassigning the object to a variable, then the ``HER Document`` will be\navailable into the ``self.HER`` variable of the object.\n\n.. code:: python\n\n    import her\n    json2HERObject = her.Json2HER("{\\"Category\\":{\\"Cool\\":true}}")\n    print(json2HERObject.HER)\n\nOutput:\n\n::\n\n    - Category -\n        * Cool = True\n\nConvert HER to JSON\n-------------------\n\nJust use the ``HER2Json`` class. Call the ``__init__`` function\nassigning the object to a variable, then the ``JSON`` will be available\ninto the ``self.JSON`` variable of the object.\n\n\n.. code:: python\n\n    import her\n    HER2JsonObject = her.HER2Json("- Category -\\n    * Cool = True")\n    print(HER2JsonObject.JSON)\n\nOutput:\n\n::\n\n    {"Category":{"Cool":true}}\n\n.. |Build Status| image:: https://travis-ci.org/hearot/HER.svg?branch=master\n   :target: https://travis-ci.org/hearot/HER\n',
    author='Gabriel Hearot',
    author_email='gabriel@hearot.it',
    url='https://github.com/hearot/HER',
    download_url='https://github.com/hearot/HER/archive/v1.2.tar.gz',
    keywords=['python', 'her'],
    classifiers=[]
)
