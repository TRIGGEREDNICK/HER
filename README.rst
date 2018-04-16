HER, a new Text Format |Build Status|
=====================================

Search informations about the Syntax and Types using the `Wiki
section`_.

Content table
-------------

-  `What’s HER?`_
-  `Why shall I use HER?`_
-  `Why HER?`_
-  **Python Module**

   -  `Installation`_
   -  `Import Module`_
   -  `Encode a Dictionary`_
   -  `Decode a String`_
   -  `Decode a File`_
   -  `Convert HER to JSON`_
   -  `Convert JSON to HER`_
   -  `Documentation`_

What’s HER?
-----------

HER is text format, like XML/Json. The difference is that HER is easier
than others. Just see:

::

    - Category -
        >> Array[]
        * Array[] = "Umh, that's pretty good!"

Why shall I use HER?
--------------------

As I said before, HER is **simple** and **easy to use**. You can pass
informations, or better, store informations\* and document them.

Feel the difference:

**XML:**

.. code:: xml

    <category>Christmas
        <greetings>Merry christmas!</greetings>
        <greetings>Spam, Python, Eggs</greetings>
    </category>

**HER:**

::

    - Christmas -
        >> Greetings[]
        * Greetings[] = "Merry christmas!"
        * Greetings[] = "Spam, Python, Eggs"

Why HER?
~~~~~~~~

**Because, however, if it isn’t right, it’s right.**

Python Module
=============

Installation
------------

You can easily install that module using PiP:

.. code:: bash

    pip install her

Or, if you want to upgrade the module:

.. code:: bash

    pip install --upgrade her

Import Module
-------------

You must use ``import her`` to import all HER module.

.. code:: python

    from her.core import Encoder 
    encoderObject = Encoder({'Category':{'hello world':True}})
    ...

Encode a Dictionary
-------------------

Just use the ``Encoder`` class. Call the ``__init__`` function assigning
the object to a variable, then the ``Encoded String`` will be available
into the ``self.HER`` variable of the object.

.. code:: python

    from her.core import Encoder
    encoderObject = Encoder({'Category':{'hello world':True}})
    print(encoderObject.HER)

Output:

::

    - Category -
        * hello world = True

Decode a String
---------------

Just use the ``Decoder`` class. Call the ``__init__`` function assigning
the object to a variable, then the ``Decoded Dictionary`` will be
available into the ``self.HER`` variable of the object.

.. code:: python

    from her.core import Decoder
    decoderObject = Decoder("- Category -\n    * hello world = True")
    print(decoderObject.HER)

Output:

::

    {'Category':{'hello world':True}}

Decode a File
-------------

Just use the ``Decoder`` class. Call the ``__init__`` function assigning
the object to a variable, then the ``Decoded Dictionary`` will be
available into the ``self.HER`` variable of the object.

Remember: The first parameter must be a ``File`` object and it must have
a ``readlines`` attribute.

.. code:: python

    from her.core import Decoder
    decoderObject = Decoder(open("file_path", "r"))
    print(decoderObject.HER)

Output:

::

    {'Category':{'hello world':True}}

Convert JSON to HER
-------------------

Just use the ``JSON`` class. Call the ``__init__`` function assigning
the object to a variable, then the ``HER Document`` will be available
into the ``self.HER`` variable of the object.

.. code:: python

    from her.json_her import JSON
    json2HERObject = JSON("{\"Category\":{\"Cool\":true}}")
    print(json2HERObject.HER)

Output:

::

    - Category -
        * Cool = True

Convert HER to JSON
-------------------

Just use the ``HER`` class. Call the ``__init__`` function assigning the
object to a variable, then the ``JSON`` will be available into the
``self.JSON`` variable of the object.

.. code:: python

    from her.json_her import HER
    HER2JsonObject = HER("- Category -\n    * Cool = True")
    print(HER2JsonObject.JSON)

Output:

::

    {"Category":{"Cool":true}}

.. _Wiki section: https://github.com/hearot/HER/wiki
.. _What’s HER?: #whats-her
.. _Why shall I use HER?: #why-shall-i-use-her
.. _Why HER?: #why-her
.. _Installation: #installation
.. _Import Module: #import-module
.. _Encode a Dictionary: #encode-a-dictionary
.. _Decode a String: #decode-a-string
.. _Decode a File: #decode-a-file
.. _Convert HER to JSON: #convert-her-to-json
.. _Convert JSON to HER: #convert-json-to-her
.. _Documentation: http://her.readthedocs.org

.. |Build Status| image:: https://travis-ci.org/hearot/HER.svg?branch=master
   :target: https://travis-ci.org/hearot/HER