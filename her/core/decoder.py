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

"""
her.core.decoder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
It contains the Decoder class.

It could be used to decode HER and convert it into
a dictionary.
"""


class Decoder:

    """
    Class for HER decoding, or better,
    converting it into a dictionary.
    """

    def __init__(self, her_string):
        """
        It initializes the object by trying
        to parse the given parameter.

        :param her_string: A file or a string coded in HER.
        :type her_string: file or str
        """
        try:
            # It checks if her_string
            # is a file.
            her_string = her_string.readlines()
        except AttributeError:
            # It's not a File, I try to
            # read it using splitlines()
            # function.
            her_string = her_string.splitlines()
        # It's got the content, but there are
        # blank characters before a normal character,
        # so It strips them.
        content = [x.strip() for x in her_string]
        # It declares the HER
        # Dictionary, that will contain
        # the parsed Dictionary.
        self.HER = {}
        # It calls the parseString function
        # that will parse the String
        # and store it as self.HER
        self.parse_string(content)

    def parse_string(self, her_lines):
        """
        It parses the string and convert it
        into a dictionary.

        :param her_lines: A list of the lines of the string.
        :type her_lines: list
        """
        # It declares a string that will
        # be used for storing the
        # current section, or category.
        current_section = ""
        # The "for-each" starts
        for line in her_lines:
            # It checks if the line is
            # a comment or not.
            if line.startswith("#"):
                # If it is, we don't parse
                # this line and we continue the
                # loop.
                continue
            # It checks if the line is
            # a Category declaration.
            elif line.startswith("- "):
                # It strips the "-" and then
                # it store the Category into
                # current_section variable.
                current_section = line[2:-2]
                # It declare a Dictionary, that
                # will contain Category elements.
                self.HER[current_section] = {}
            # It checks if the line is
            # a List Declaration.
            elif line.startswith(">> "):
                # It checks if the line is
                # a List.
                if line.split(" =", 1)[0][-2:] == "[]":
                    # It declares the List.
                    self.HER[current_section][
                        line.split("[] =", 1)[0][3:-2]] = []
            # It checks if the line is
            # a variable assignment
            # or declaration.
            elif line.startswith("* "):
                # It checks if the line
                # assigns a value to
                # a list.
                if line.split(" =", 1)[0][-2:] == "[]":
                    # It uses the exec function
                    # to assign the value to the
                    # list.
                    exec(
                        "self.HER[current_section][line.split" +
                        "(\" =\")[0][2:-2]].append(" +
                        line.split(" = ", 1)[1] +
                        ")"
                    )
                # Then, if it isn't a
                # variable assignment into
                # a list, it declares
                # a variable and then
                # it assigns a value into it.
                else:
                    # It uses the exec function
                    # to assign the value to a
                    # variable.
                    exec(
                        "self.HER[current_section][line.split"
                        "(\" =\")[0][2:]] = " + line.split(" = ", 1)[1]
                    )
