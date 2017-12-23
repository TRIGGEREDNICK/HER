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
from .encoder import Encoder
# It imports the JSON class, it
# is needed for JSON-HER converter.
import json


class Json2HER:

    """
    JSON -> HER converter class
    """

    def __init__(self, JSON):
        # It stores the passed JSON
        # under self.JSON.
        self.JSON = json.loads(JSON)
        # It calls the convert() function
        # that will store the HER Document under
        # self.HER.
        self.convert()

    def convert(self):
        # It initializes the Encoder class
        # (from encoder.py), creating an
        # object that will store
        # the HER Document.
        self.encoderObject = Encoder(self.JSON)
        # It assigns to self.HER the HER Document taken
        # from self.encoderObject Object.
        self.HER = self.encoderObject.HER
