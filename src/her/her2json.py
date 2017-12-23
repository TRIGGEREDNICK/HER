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

# It imports the Decoder class
# from decoder.py.
from .decoder import Decoder
# It imports the JSON class, it
# is needed for JSON-HER converter.
import json


class HER2Json:

    """
    HER -> JSON converter class
    """

    def __init__(self, HERLines, isFile=False):
        # It declares self.isFile, that
        # will be used to store
        # a boolean that depends on the second parameter
        # (isFile).
        self.isFile = isFile
        # It declares self.HERLines, that
        # will be used to store the first
        # parameter (HERLines).
        self.HERLines = HERLines
        # It calls the convert() function,
        # that will convert HER to JSON and
        # it will store the JSON into
        # self.JSON.
        self.convert()

    def convert(self):
        # It initializes an object using
        # Decoder class (from decoder.py) and
        # pass self.HERLines (see line 42) and
        # self.isFile (see line 37) as
        # parameters.
        self.decoderObject = Decoder(self.HERLines, self.isFile)
        # It stores the JSON
        # under self.JSON.
        self.JSON = json.dumps(self.decoderObject.HER, ensure_ascii=False)
