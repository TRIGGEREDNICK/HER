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
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# It imports the Encoder class
# from encoder.py.
from her.core.encoder import Encoder
# It imports the json class, it
# is needed for json-HER converter.
import json

"""
her.json_her.json_converter.JSON
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
It contains the JSON class.

It could be used to convert JSON to
HER text.
"""


class JSON:

    """
    JSON to HER converter.
    """

    def __init__(self, json_string):
        """
        It initializes the object and
        tries to convert the JSON into HER
        text.

        :param json_string: The JSON string.
        :type json_string: str
        """
        # It stores the passed JSON
        # under self.json.
        self.json = json.loads(json_string)
        # It calls the convert() function
        # that will store the HER Document under
        # self.HER.
        self.encoder_object = None
        self.HER = None
        self.convert()

    def convert(self):
        """
        It converts the JSON into HER text.
        """
        # It initializes the Encoder class
        # (from encoder.py), creating an
        # object that will store
        # the HER Document.
        self.encoder_object = Encoder(self.json)
        # It assigns to self.HER the HER Document taken
        # from self.encoderObject Object.
        self.HER = self.encoder_object.HER
